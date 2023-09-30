#if this does not work, go into terminal and install the libraries
#pip install SpeechRecognition
#pip install pyttsx3
#pip install pyaudio
#pip install requests

import Audio_Input
import Letter_Translation
import HandSpeak_Translation
import ASL_LEX_Translation
import New_Handspeak
import GUI


def tkrun():
    test = GUI.MyGUI()
    test.run()

def MainCall():
    #audiotext = Audio_Input.TakeInAudio()
    audiotext = "Hello World"
    print("What Translation Output Do You Desire?")
    print("     1 - Letter-by-letter")
    print("     2 - Handspeak")
    print("     3 - ASL-LEX")
    print("     4 - Handspeak 2")
    mode = input()
    print(str(type(mode)))
    if(mode == "1"):
        Translate_Letter(audiotext)
    elif(mode == "2"):
        Translate_HandSpeak(audiotext)
    elif(mode == "3"):
        Translate_ASL_LEX(audiotext)
    elif(mode == "4"):
        Translate_New_Handspeak(audiotext)
    else:
        print("not a valid answer")

def Translate_Letter(text):
    new_text = text + ' '
    Letter_Translation.Translate(new_text)
    Letter_Translation.mainloop()

def Translate_HandSpeak(text):
    HandSpeak_Translation.Translate(text)

def Translate_ASL_LEX(text):
    altered = text.lower()
    altered2 = altered.split()
    for input in altered2:
        ASL_LEX_Translation.ASL_lex_search(input)

def Translate_New_Handspeak(text):
    altered = text.split()
    for input in altered:
        #New_Handspeak.Handspeak_search(input)
        New_Handspeak.Handspeak_search(input)





#MainCall()
tkrun()
