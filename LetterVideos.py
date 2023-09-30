import os
from tkinter import *

#TODO first copy everything down from the old letter translation now need to change everything to work with videos

#maybe repurpose this to be an array of strings that other code can use as a url to the video or something else
global_url_array = [];


#TODO replace getting image with getting video url (i think this works)
#note: if a space or ' is passed in, it gives the url to the sign for space, make sure this is accounted for when displaying
def get_video(letter):
    pathtofile = os.getcwd()

    if letter == ' ' or letter == "'":
        thepath = os.path.join(pathtofile, "ASL Letter Videos", "Space.mp4")

    else:
        ltr = str(letter)
        ltrp = ltr + ".mp4"
        thepath = os.path.join(pathtofile, "ASL Letter Videos", ltrp)
    print(thepath)
    return thepath

#turns the input into a list
def Make_list(sentence):
    letter_list = list(sentence)
    return letter_list

#does the same as above, but has root as argument and removes newline character
#This version is for audio input(i think) because how speech recognition adds newline character
#(I think, this might not actually be used)
def Make_List(root, sentence):
    letter_list = list(sentence)
    letter_list.remove('\n')
    return letter_list


def Check_for_Space(x, y, input_list, flag):
    dist = input_list.index(' ')
    test = input_list.pop(0)
    #reset flag to false to indicate new word
    if(test == ' '):
        flag = False

    if (100 * dist + x >= 1520 and 100*dist < 1500):
        # smart wrap around
        x = 20
        y += 230
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
    return x, y



def Get_Video_List(input_list):
    for j in input_list:
        image = get_video(j)
        global_url_array.append(image)



def DoJonahs_Stuff():
    input = "this is a long sentence to test the smart wrap around of the code and also what happens when the phrase is too big"
    intermidiate = Make_List(input)
    Display(intermidiate)


def Clear():
    global_url_array.clear()

def Translate(root, audio_text):
    intermidiate = Make_List(audio_text)
    Display(root, intermidiate)

def Translate(audio_text):
    intermidiate = Make_List(audio_text)
    Display(intermidiate)
    
#pretty sure this is a ghost function, test to see if this is used.
def Display(input_list):
    root = Tk()
    canvas = Canvas(root, width=1600, height=800)
    canvas.pack()
    # Change All Images Created to Relative Pathing for further iterations

    #put images on 'canvas'/window
    Get_Video_List(input_list)
    x = 20
    y = 20
    flag = False
    for i in global_url_array:
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

