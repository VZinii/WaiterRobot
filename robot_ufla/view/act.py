# import pyttsx3
import time

from elevenlabs import generate, play



def act(str):
    # engine = pyttsx3.init()
    # engine.say(str)
    # time.sleep(3)
    # engine.runAndWait()
    # time.sleep(3)
    audio = generate(text=str, voice="Daniel", model="eleven_multilingual_v2")
    play(audio)
    time.sleep(3)
