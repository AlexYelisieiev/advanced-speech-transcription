import speech_recognition as sr
from os import system
from threading import Thread

from text_recognition import recognize_text_in_background


STOP_PHRASES = [
    "stop recording",
    "stop listening",
    "закончи аудиозапись",
    "останови аудиозапись",
]


def main():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    full_recognized_text = ""

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source=microphone, duration=2)

        # Listen and try to recognize continiously
        system("cls")
        print("Listening:")

        stop_listening = False
        while not stop_listening:
            # Listen to a single phrase
            audio = recognizer.listen(source=microphone, phrase_time_limit=170)
            # Recognize audio
            recognized_text = recognize_text_in_background(recognizer, audio)

            if recognized_text:
                print(recognized_text, end=" ")
                full_recognized_text += f" {recognized_text}"

            # Chech for stop phrase
            for stop_phrase in STOP_PHRASES:
                if stop_phrase in recognized_text.lower():
                    stop_listening = True

    # Write everything to the file
    if full_recognized_text:
        with open("./full_recognized_text.txt", "w", encoding="utf-8") as file:
            file.write(full_recognized_text)


if __name__ == "__main__":
    main()
