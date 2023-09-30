import webbrowser
import pyautogui as pag
import time

#https://www.youtube.com/watch?v=I_uk8NPnarU source used for how to use the pag library (not much, but it works)

#IMPORTANT NOTE: This is most likely display-dependent and would need to be tweeked for use on any other sized monitor
def Handspeak_search(word):
    #open the webpage
    webbrowser.open("https://www.handspeak.com/word/")
    time.sleep(1.0)

    pag.moveTo(500,620)
    pag.click()
    time.sleep(1)

    #perform search
    divided = list(word)
    for letter in divided:
        pag.write(letter)

    #filter by letter
    pag.scroll(-400, x=350, y=600)
    #get first letter of word
    char = divided[0]
    x,y,start = 0,0,0
    if ord(char) < 107:
        start,y,buffer = 537,500,97#377
    elif ord(char) >= 117:
        start,y,buffer = 440,530,117#280
    else:
        start,y,buffer = 515,500,97#355

    x = start+33*(ord(char)-buffer)
    pag.moveTo(x,y)
    pag.click()
    time.sleep(1.5)

    #ord('a') #97


    #click on the word
    pag.moveTo(460,600)
    time.sleep(0.5)
    pag.click()

def testing(word):
    webbrowser.open("https://www.handspeak.com/word/")
    pag.moveTo(430,600)
    time.sleep(0.5)
    pag.click()