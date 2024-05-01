from threading import Thread
from time import sleep
import speech_recognition as sr
import config


class SpeechRecognizer(object):

    STOP_PHRASES = [
        "stop recording",
        "stop listening",
        "закончи аудиозапись",
        "останови аудиозапись",
        "закінчи запис",
        "зупини запис",
    ]

    def __init__(self, whisper_model: str, output_file_path: str) -> None:
        self.output_file_path = output_file_path
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self._recognized_speech = ""
        self._recognition_finished = False
        self._stop_listening = False
        self.full_recognized_speech = ""
        self.whisper_model = whisper_model

        # Adjust microphone to the environment
        with self.microphone as source:
            print("Adjusting the microphone...")
            self.recognizer.adjust_for_ambient_noise(source, duration=2)
            self.recognizer.dynamic_energy_threshold = False
            self.recognizer.energy_adjustment_during_recognition = False
            self.recognizer.energy_threshold = config.ENERGY_TRESHOLD
            self.recognizer.pause_threshold = config.PAUSE_TRESHOLD
            self.recognizer.phrase_threshold = config.PHRASE_TRESHOLD
            print("Microphone adjusted.")

    def _recognize_speech(self, audio: sr.AudioData) -> None:
        """Used for the main speech recognition"""

        try:
            self._recognized_speech = self.recognizer.recognize_whisper(
                audio_data=audio, model=self.whisper_model
            )
            self._recognition_finished = True
            return
        except Exception:
            return None

    def _recognize_speech_in_background(self, audio: sr.AudioData) -> str:
        """Uses `self._recognize_speech` to recognize speech from the given audio"""

        # Start speech recognition
        thread = Thread(target=self._recognize_speech, args=(audio,))
        thread.start()

        # Wait until the speech is recognized
        while not self._recognition_finished:
            sleep(1)

        self._recognition_finished = False

        return self._recognized_speech

    def start_speech_recognition(self) -> None:
        print("Listening:")
        while not self._stop_listening:
            # Listen to a single phrase
            with self.microphone as source:
                audio = self.recognizer.listen(
                    source=self.microphone, phrase_time_limit=170
                )

            # Recognize speech
            recognized_speech = self._recognize_speech_in_background(audio)

            if recognized_speech:
                print(recognized_speech, end=" ", flush=True)
                self.full_recognized_speech += f" {recognized_speech}"

            # Check for stop phrase
            for stop_phrase in self.STOP_PHRASES:
                if stop_phrase in recognized_speech.lower():
                    self._stop_listening = True

        # Write everything to the file
        if self.full_recognized_speech:
            # Prepare `full_recognized_speech` for writing
            self.full_recognized_speech.replace("  ", " ")
            for stop_phrase in self.STOP_PHRASES:
                self.full_recognized_speech = self.full_recognized_speech.replace(
                    stop_phrase, ""
                )

            # Write to file
            with open(self.output_file_path, "w", encoding="utf-8") as file:
                file.write(self.full_recognized_speech)
