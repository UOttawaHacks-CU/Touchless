import speech_recognition
import pyttsx3
import beepy


def audioToText():
    with speech_recognition.Microphone() as source:
        sr = speech_recognition.Recognizer()
        sr.adjust_for_ambient_noise(source, 2)
        speak("Please speak after the beep")

        while True:
            try:
                beepy.beep(sound='ready')
                audio = sr.listen(source)
                speak("Processing")
                text = sr.recognize_google(audio)
                break
            except:
                speak("Error capturing. Try again after the beep")

        speak("Did you say: " + text)
        audio = sr.listen(source)
        result = sr.recognize_google(audio).lower()
        words = result.split()
        for word in words:
            if (word == 'yes' or word == 'yeah' or word=='yep' or word=='mmhmm' or word==''):
                # print('Returning : ' + text)
                return text
        audioToText()


def speak(input):
    voice = pyttsx3.init()
    voice.say(input)
    voice.runAndWait()


def controller():
    speak("Initializing")
    sr = speech_recognition.Recognizer()
    text_value = audioToText()
    # print(text_value)
    return text_value


if __name__ == '__main__':
    controller()