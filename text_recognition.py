from threading import Thread
from time import sleep
import speech_recognition as sr


recognized_text = ""
recognition_finished = False


def recognize_text(recognizer, audio) -> str:
    global recognized_text
    global recognition_finished
    
    recognized_text = recognizer.recognize_whisper(audio_data=audio, model="base")
    recognition_finished = True
    return


def recognize_text_in_background(recognizer, audio) -> str:
    global recognized_text
    global recognition_finished

    # Start text recognition
    thread = Thread(target=recognize_text, args=(recognizer, audio))
    thread.start()

    # Wait until the text is recognized
    while not recognition_finished:
        sleep(1)

    return recognized_text
