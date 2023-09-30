import tkinter as tk
from PIL import ImageTk, Image
import Audio_Input
import TranslationInterface
import Letter_Translation
import LetterVideos
import tkvideo
import time


class MyGUI:

    def __init__(self):
        # starting stuff like initializing, size and title
        self.root = tk.Tk()
        self.root.geometry("1600x800")
        self.root.title("Translera")

        #making the forest background
        self.path = 'forestbackground2.png'
        self.icon = Image.open(self.path)
        self.icon2 = self.icon.resize((1600, 800), Image.ANTIALIAS)
        self.background = ImageTk.PhotoImage(self.icon2)
        self.b = tk.Label(self.root, image = self.background)
        self.b.pack(side = "bottom", fill = "both", expand = "yes")

        #setting variables to be used for input and output type
        self.inputtype = tk.IntVar(self.root, value = 1, name = "1")
        self.outputtype = tk.IntVar(self.root, value = 0, name = "2")

        self.LabelArray = []
        self.img_count = 0
        self.text_list = []

    #starting fuction to run the 'application' by creating the settings button and running the mainloop
    def run(self):
        self.Settingsbutton()
        self.Translatebutton()
        self.root.mainloop()

    #functions to initialize the starting screen buttons
    def Settingsbutton(self):
        self.settingbutton = tk.Button(self.root, text = "Settings", font = ('Arial', 18), command = self.OpenSettings)
        self.settingbutton.place(x = 650, y = 500, height = 100, width = 200)
    def Translatebutton(self):
        self.translatebutton = tk.Button(self.root, text="Translate", font=('Arial', 18), command=self.Translate)
        self.translatebutton.place(x=650, y=300, height=100, width=200)
    def CloseTextbutton(self):
        self.closetextbutton = tk.Button(self.root, text="Return to menu", font=('Arial', 18), command=self.CloseText)
        self.closetextbutton.place(x=0, y=700, height=100, width=200)
    def NextTextbutton(self):
        self.nexttextbutton = tk.Button(self.root, text="Next ->", font=('Arial', 18), command=self.NextScreen)
        self.nexttextbutton.place(x=1400, y=700, height=100, width=200)

    def Translate(self):
        print("starting")
        inputtext = ""
        # remove main menu buttons
        #self.settingbutton.destroy()
        #self.translatebutton.destroy()
        self.CloseMainMenu()
        if (str(self.inputtype.get()) == "0"):
            self.prepAudioInput()
            self.root.update_idletasks()
            #self.AudioTranslate()
            #self.CloseAudioMenu()
        elif (str(self.inputtype.get()) == "1"):
            self.inputtext = self.TextInput(inputtext)
        else:
            print("Invalid input method")
            print(self.inputtype)

    def CloseMainMenu(self):
        self.settingbutton.destroy()
        self.translatebutton.destroy()

    def TextInput(self, text):
        #insert textbox and button
        self.text = tk.Text(self.root,height = 3, font=('Arial', 18),)
        self.text.place(x =100, y = 100)
        self.textgo = tk.Button(self.root, text = "Go", font=('Arial', 18), command = self.TextPrint)
        self.textgo.place(x = 600, y = 500, height = 100, width = 300)

    def CloseText(self):
        self.closetextbutton.destroy()
        #for one screen translations, the nexttext buton does not exist so added a try/catch
        try:
            self.nexttextbutton.destroy()
        except:
            z = 0
        for i in self.LabelArray:
            i.destroy()
        self.LabelArray.clear()
        Letter_Translation.Clear()
        # replace the main menu buttons
        self.Settingsbutton()
        self.Translatebutton()

    def TextPrint(self):
        #send forward the text
        self.inputtext = self.text.get('1.0', tk.END)
        print("inputtext = " + self.inputtext)
        self.text_list = TranslationInterface.TranslationInterface(self.root, self.inputtype.get(), self.outputtype.get(), self.inputtext)
        #print(self.text_list)

        if (str(self.outputtype.get()) == "0"):
            self.Display(self.text_list)
        elif(str(self.outputtype.get()) == "3"):
            self.DisplayVideos(self.text_list)
        self.text.destroy()
        self.textgo.destroy()
        #add 'return to main menu button, dont immediatly add main menu buttons
        self.CloseTextbutton()

    def NextScreen(self):
        for i in self.LabelArray:
            i.destroy()
        self.LabelArray.clear()
        Letter_Translation.Clear()
        self.nexttextbutton.destroy()
        self.Display(self.text_list)

    def prepAudioInput(self):
        self.Makenewbackground()
        self.audiobutton = tk.Button(self.root, text="Press Button Then Speak", font=('Arial', 18), command = self.Listen)
        self.audiobutton.place(x=500, y=400, height=100, width=500)#was 400, added new words
        self.root.update_idletasks()
        return 0.5

    def Listen(self):
        #audiospeak button doesnt actually load due to how the broken nature of the code is with the audio_inout stuff, but it is here
        self.audiospeak = tk.Label(self.root, text="Please Speak Now", font=('Arial', 18),)
        self.audiospeak.place(x=500, y=600, height=100, width=500)  # was 400, added new words
        self.AudioTranslate()

    def AudioTranslate(self):
        self.audiobutton.destroy()
        self.inputtext = Audio_Input.TakeInAudio()
        self.CloseAudioMenu()

    def CloseAudioMenu(self):
        self.b2.destroy()
        self.audiospeak.destroy()
        self.text_list = TranslationInterface.TranslationInterface(self.root, self.inputtype.get(), self.outputtype.get(), self.inputtext)
        # print(self.text_list)
        if (str(self.outputtype.get()) == "0"):
            self.Display(self.text_list)
        elif(str(self.outputtype.get()) == "3"):
            self.DisplayVideos(self.text_list)
        self.CloseTextbutton()

    #basically need to render a new background for 'provide audio input' sreen because main menu is being annoying
    def Makenewbackground(self):
        self.icon3 = Image.open(self.path)
        self.icon4 = self.icon.resize((1600, 800), Image.ANTIALIAS)
        self.background2 = ImageTk.PhotoImage(self.icon2)
        self.b2 = tk.Label(self.root, image = self.background)
        self.b2.pack(side = "bottom", fill = "both", expand = "yes")

    #opens all the settings buttons, inlcuding input type, output type and a close settings button
    def OpenSettings(self):
        #testing things
        print("settings")
        #setting background
        self.stnback = tk.Label(self.root, text = ' ', font = ('Arial', 18))
        self.stnback.place(x = 400, y = 100, height = 650, width = 800)
        #OUTPUT SETTINGS
        #letter Translation
        self.stn1 = tk.Button(self.root, text = "Letter", font = ('Arial', 18), command = self.SetOutput0)
        self.stn1.place(x = 550, y = 500, height = 100, width = 140)
        #ASL-Lex Translation
        self.stn2 = tk.Button(self.root, text="ASL-Lex", font=('Arial', 18), command = self.SetOutput1)
        self.stn2.place(x=750, y=500, height=100, width=140)
        #Handspeak Translation
        self.stn3 = tk.Button(self.root, text="Handspeak", font=('Arial', 18), command = self.SetOutput2)
        self.stn3.place(x=950, y=500, height=100, width=140)
        # letters(but with videos)
        self.stn6 = tk.Button(self.root, text="letter Videos", font=('Arial', 18), command=self.SetOutput3)
        self.stn6.place(x=550, y=610, height=100, width=140)

        #INPUT SETTINGS
        #audio input
        self.stn4 = tk.Button(self.root, text="Audio", font=('Arial', 18), command = self.SetInput0)
        self.stn4.place(x=600, y=300, height=100, width=140)
        #text input
        self.stn5 = tk.Button(self.root, text="Text", font=('Arial', 18), command = self.SetInput1)
        self.stn5.place(x=900, y=300, height=100, width=140)
        #close settings
        self.stnc = tk.Button(self.root, text="Close", font=('Arial', 18), command = self.CloseSettings)
        self.stnc.place(x=1100, y=100, height=100, width=100)

    def CloseSettings(self):
        self.stn1.destroy()
        self.stn2.destroy()
        self.stn3.destroy()
        self.stn4.destroy()
        self.stn5.destroy()
        self.stn6.destroy()
        self.stnback.destroy()
        self.stnc.destroy()

    #functions for changing input
    def SetInput0(self):
        self.inputtype.set(0)
        print(self.inputtype)
        return self.inputtype
    def SetInput1(self):
        self.inputtype.set(1)
        return self.inputtype

    #functions for changing output
    def SetOutput0(self):
        self.outputtype.set(0)
        return self.outputtype
    def SetOutput1(self):
        self.outputtype.set(1)
        return self.outputtype
    def SetOutput2(self):
        self.outputtype.set(2)
        return self.outputtype
    def SetOutput3(self):
        self.outputtype.set(3)
        return self.outputtype

    #function used in letter transltion (images), copy from letter_translation.py because it doesnt work when ran from there
    def Display(self, input_list):
        # Change All Images Created to Relative Pathing for further iterations
        print("in display, the input list is: ")
        print(input_list)
        # put images on 'canvas'/window
        Letter_Translation.Get_Images(input_list)
        for i in Letter_Translation.global_photo_array:
            #add label to label list
            self.LetterLabel = tk.Label(self.root, image = i)
            self.LabelArray.append(self.LetterLabel)
        X = 20
        Y = 20
        flag = False

        for i in self.LabelArray:
            # check for appropriate distance for word
            X, Y = Letter_Translation.Check_for_Space(X, Y, input_list, flag)
            # wrap-around
            if X >= 1520:
                X = 20
                Y += 140
            if Y >= 651:
                print("Out of Window bounds")
                self.NextTextbutton()
                return
            i.place(x = X, y = Y, height = 100, width = 100)
            self.img_count += 1
            #self.stnback.place(x = 400, y = 100, height = 650, width = 800)
            X += 100
    ##end of Display


    def DisplayVideos(self, input_list):
        #initialize a counter to tell which url should be used
        count = 0
        # Change All Images Created to Relative Pathing for further iterations
        print("in display, the input list is: ")
        print(input_list)
        # put images on 'canvas'/window
        LetterVideos.Get_Video_List(input_list)
        for i in LetterVideos.global_url_array:
            #add label to label list
            self.LetterLabel = tk.Label(self.root)
            self.LabelArray.append(self.LetterLabel)
        X = 20
        Y = 20
        flag = False

        for i in self.LabelArray:
            # check for appropriate distance for word
            X, Y = LetterVideos.Check_for_Space(X, Y, input_list, flag)
            # wrap-around
            if X >= 1520:
                X = 20
                Y += 240
            if Y >= 651:
                print("Out of Window bounds")
                self.NextTextbutton()
                return
            i.place(x = X, y = Y, height = 200, width = 200)
            self.tkvideolabel = tkvideo.tkvideo(LetterVideos.global_url_array[count], i, loop=1, size=(200, 200))
            self.tkvideolabel.play()
            count +=1
            self.img_count += 1
            #self.stnback.place(x = 400, y = 100, height = 650, width = 800)
            X += 210


MyGUI