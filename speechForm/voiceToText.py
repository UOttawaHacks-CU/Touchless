import speech_recognition
import pyttsx3
import beepy
import sys

def audioToText():
    speak("Initializing")
    sr = speech_recognition.Recognizer();
    with speech_recognition.Microphone() as source:
        sr.adjust_for_ambient_noise(source, 2)
        speak("Please speak after the beep")
        beepy.beep(sound='ready')
        audio = sr.listen(source)
        text = sr.recognize_google(audio)
        speak("Did you say: " + text)
        return(text)

def speak(input):
    voice = pyttsx3.init()
    voice.say(input)
    voice.runAndWait()

audioToText()
sys.stdout.flush()