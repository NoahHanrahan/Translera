#if this does not work, go into terminal and install the libraries
#pip install SpeechRecognition
#pip install pyttsx3
#pip install pyaudio
#pip install requests
import speech_recognition as sr
import pyttsx3
import requests


try:
    from googlesearch import search
except ImportError:
    print("No Module named 'google' found")
from tkinter import *

#############################################################################################################################################################################################################################################################
#Noah's stuff taking in audio and usiing speech recognition
#############################################################################################################################################################################################################################################################

def TakeInAudio():
    #initialize recognizer
    r = sr.Recognizer()

    #now use mnicrophone as source of input
    with sr.Microphone() as source2:
        #wait a bit to let recognizer adjust to ambient noise
        r.adjust_for_ambient_noise(source2, duration = 0.5)
        r.dynamic_energy_threshold = True
        print("Please provide audio input:")
        #listen to user input
        audio2 = r.listen(source2)
        print("Processing...")

        #try to use google when there is internet (maybe, might slow it down)
        url = "https://www.google.com/"
        timeout = 1
        try:
            #use google as default speech recognition (online)
            request = requests.get(url, timeout=timeout)
            print("using google speech recognition")
            text = r.recognize_google(audio2)
            # use cmusphinx to recognize audio when offline
        except (requests.ConnectionError, requests.Timeout) as exception:
            print("using sphinx speech recognition (offline)")
            text = r.recognize_sphinx(audio2)

        #make all the text lowercase
        text = text.lower()
        print(text)
    return text

def testing():
    return "hello, made it out"