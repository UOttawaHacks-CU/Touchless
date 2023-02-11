import speech_recognition
import pyaudio

sr = speech_recognition.Recognizer();
with speech_recognition.Microphone() as source:
    print("Initializing...")
    sr.adjust_for_ambient_noise(source, 2)
    print("Speak now please... ")
    audio = sr.listen(source)
    text = sr.recognize_google(audio).lower()
    print("Did you say: " + text)

