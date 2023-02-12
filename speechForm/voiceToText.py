import speech_recognition
import pyttsx3
import beepy
import json
import os
import requests


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
    text_value = audioToText()
    addToPerson(text_value)
    return text_value


def addToPerson(text):
    try:
        with open('speechForm/person.json', 'r') as openfile:
            person = json.load(openfile)
    except:
        person = {}
 
    if (len(person) == 4):
        person["medication"] = text
        sendInfo(person)

        os.remove("speechForm/person.json")
        person = {}
        json_object = json.dumps(person, indent=4)

        with open("speechForm/person.json", "w") as outfile:
            outfile.write(json_object)

    elif (len(person) == 0):
        person["name"] = text
        json_object = json.dumps(person, indent=4)

        with open("speechForm/person.json", "w") as outfile:
            outfile.write(json_object)

    elif (len(person) == 1):
        person["medical history"] = text
        json_object = json.dumps(person, indent=4)

        with open("speechForm/person.json", "w") as outfile:
            outfile.write(json_object)

    elif (len(person) == 2):
        person["q3"] = text
        json_object = json.dumps(person, indent=4)
        
        with open("speechForm/person.json", "w") as outfile:
            outfile.write(json_object)

    elif (len(person) == 3):
        person["allergies"] = text
        json_object = json.dumps(person, indent=4)
        
        with open("speechForm/person.json", "w") as outfile:
            outfile.write(json_object)


def sendInfo(dict):
    print(json.dumps(dict, indent=4))
    try:
        url = 'https://n6bwdl0hp3.execute-api.ca-central-1.amazonaws.com/CUdynamodemo'
        myobj = json.dumps(dict, indent=4)

        x = requests.post(url, body = myobj)

        print(x.text)
        
    except:
        print('Error : Data not sent to server')


if __name__ == '__main__':
    controller()