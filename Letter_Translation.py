import os
from tkinter import *

global_photo_array = [];

#function to get image of letter from a character
def get_image(letter):
    pathtofile = os.getcwd()

    if letter == ' ' or letter == "'":
        spacepath = os.path.join(pathtofile, "ASL Alphabet", "Space.png")
        img = PhotoImage(file=spacepath)

    else:
        ltr = str(letter)
        ltrp = ltr + ".png"
        alphapath = os.path.join(pathtofile, "ASL Alphabet", ltrp)
        img = PhotoImage(file=alphapath)

    return img
##end of get_img

def Make_list(sentence):
    letter_list = list(sentence)
    #print(letter_list)
    return letter_list

def Make_List(root, sentence):
    letter_list = list(sentence)
    letter_list.remove('\n')
    #print(letter_list)
    return letter_list

#end of make_list

#pretty sure this is a ghost function, isnt used
def Display(input_list):
    root = Tk()
    canvas = Canvas(root, width=1600, height=800)
    canvas.pack()
    # Change All Images Created to Relative Pathing for further iterations

    #put images on 'canvas'/window
    Get_Images(input_list)
    x = 20
    y = 20
    flag = False
    for i in global_photo_array:
        #check for appropriate distance for word
        x,y = Check_for_Space(x, y, input_list, flag)
        canvas.create_image(x, y, anchor=NW, image=i)
        x+= 100
        #wrap-around
        if x >= 1520:
            x = 20
            y += 150
        if y >= 651:
            print("Out of Window bounds")
            return
##end of Display

def Check_for_Space(x, y, input_list, flag):
    dist = input_list.index(' ')
    test = input_list.pop(0)
    #reset flag to false to indicate new word
    if(test == ' '):
        flag = False

    if (100 * dist + x >= 1520 and 100*dist < 1500):
        # smart wrap around
        x = 20
        y += 130
        if (y > 651):
            input_list.insert(0, test)
        else:
            z = 0
    elif(100*dist + x <= 1520 or flag):
        #normal process for the word fitting, process normally, also covers when word too big for wrap around
        z = 0
    elif(100*dist > 1500):
        #if word is too big, wrap leter by letter by setting flag true
        flag = True
    else:
        #a bunch of printing to tell what is going on when stuff isnt right, this shouldnt be executed ever
        print("something isn't right, letter = " + str(test))
        print(input_list)
        print("dist:  " + str(dist))
        print("current x:  " + str(x))
    return x,y

#end of Check_for_Space

def Get_Images(input_list):
    for j in input_list:
        image = get_image(j)
        global_photo_array.append(image)
#end of Get_Images

def DoJonahs_Stuff():
    input = "this is a long sentence to test the smart wrap around of the code and also what happens when the phrase is too big"
    intermidiate = Make_List(input)
    Display(intermidiate)

def Clear():
    global_photo_array.clear()

def Translate(root, audio_text):
    intermidiate = Make_List(audio_text)
    Display(root, intermidiate)

def Translate(audio_text):
    intermidiate = Make_List(audio_text)

    Display(intermidiate)

