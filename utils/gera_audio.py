from gtts import gTTS
from playsound import playsound


def transforma_texto_audio(translated_text):
    tts = gTTS(translated_text)
    tts.save("exemplo.mp3")
    playsound("exemplo.mp3")
