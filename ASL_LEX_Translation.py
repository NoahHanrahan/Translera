import webbrowser
import pyautogui as pag
import time

#https://www.youtube.com/watch?v=I_uk8NPnarU source used for how to use the pag library (not much, but it works)

#IMPORTANT NOTE: This is most likely display-dependent and would need to be tweeked for use on any other sized monitor
def ASL_lex_search(word):
    #open the webpage
    webbrowser.open("https://asl-lex.org/visualization/")
    pag.moveTo(60, 260)
    time.sleep(2)

    pag.moveTo(60,140)
    pag.click()
    time.sleep(4)

    pag.moveTo(60,230)
    pag.click()
    time.sleep(3)

    #perform search
    pag.write(word)
    pag.keyDown('return')

    pag.moveTo(60,260)
    pag.click()
    time.sleep(2)
#end of ASL_lex_search


