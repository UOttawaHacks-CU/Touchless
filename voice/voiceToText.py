import speech_recognition
import pyaudio

def speech():
    sr = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Initializing...")
        sr.adjust_for_ambient_noise(source, 2)
        print("Speak now please... ")
        audio = sr.listen(source)
        text = sr.recognize_google(audio).lower()
        print("Did you say: " + text)
        audio = sr.listen(source)
        result = sr.recognize_google(audio).lower()
        words = result.split()

        for word in words:
            if (word == 'yes' or word == 'yeah' or word=='yep' or word=='mmhmm' or word==''):
                return text
        speech()


def main():
    speech()


if __name__ =='__main__':
    main()