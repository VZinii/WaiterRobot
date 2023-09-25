import pyttsx3
import time

from gtts import gTTS
import os

# def act(str):
    # str = "Pessoa falante aqui"
    # engine = pyttsx3.init()
    # engine.say(str)
    # time.sleep(3)
    # engine.runAndWait()
    # time.sleep(3)
    # audio = gTTS(text=str, lang="pt", slow=False)
    # audio.save("example.mp3")
    # os.system("start example.mp3")

    # play(audio)
    # time.sleep(3)

from elevenlabs import clone, generate, play, set_api_key
from elevenlabs.api import History

set_api_key("c7f8ff1ea7527c73e4015f9f9e1917ff")

def speak(str):
    audio = generate(
        text=str,
        voice="Daniel",
        model="eleven_multilingual_v2"
    )

    play(audio)
