import tkinter as tk
from PIL import ImageTk, Image
import Audio_Input
import TranslationInterface
import Letter_Translation
import time
import LetterVideos
import tkvideo
from moviepy.editor import *
import pyautogui as pag


import os

class MyGUI:

    def __init__(self):
        # starting stuff like initializing, size and title
        self.root = tk.Tk()
        self.root.geometry("1600x800")
        self.root.title("Translera")

        #making the initial background
        self.path = "Backgrounds/Bruneau Center Blurry.png"
        self.icon = Image.open(self.path)
        self.icon2 = self.icon.resize((1600, 800), Image.ANTIALIAS)
        self.background = ImageTk.PhotoImage(self.icon2)

        #removed , image = self.background from b,
        self.b = tk.Label(self.root, image = self.background)
        self.b.pack(side = "bottom", fill = "both", expand = "yes")

        #setting variables to be used for input and output type
        self.inputtype = tk.IntVar(self.root, value = 1, name = "1")
        self.outputtype = tk.IntVar(self.root, value = 4, name = "2")

        self.LabelArray = []
        self.img_count = 0
        self.text_list = []
        self.loop = 0

        #Making Title label
        self.Titlepath = "Button Styles/Bruneau_Sliver_Copperplate_Yellow.png"
        self.Titleicon = Image.open(self.Titlepath)
        self.TitleResize = self.icon.resize((1600, 200), Image.ANTIALIAS)
        self.TitleImage = ImageTk.PhotoImage(self.Titleicon)

        self.Title = tk.Label(self.root, image = self.TitleImage, border = "0")
        self.Title.place(x=3, y=0)

        #setting up buttons
        self.TranslateButtonBack = self.SetupButton("Button Styles/MUN Translate.png", 300, 102)
        self.SettingsButtonBack = self.SetupButton("Button Styles/MUN Settings.png", 300, 102)
        self.CloseButtonBack = self.SetupButton("Button Styles/MUN Menu.png", 300, 102)
        self.ProceedButtonBack = self.SetupButton("Button Styles/MUN Proceed.png", 300, 102)
        self.NextButtonBack = self.SetupButton("Button Styles/MUN Next.png", 300, 102)
        #will need to fine-tune the numbers once Noah's button is integrated
        self.PressThenSpeak = self.SetupButton("Button Styles/MUN PressThenSpeak.png", 500, 100)
        self.RepeatButtonBack = self.SetupButton("Button Styles/MUN Repeat.png", 300, 102)
        self.InputSettingButtonBack = self.SetupButton("Button Styles/MUN Input.png", 300, 102)
        self.OutputSettingButtonBack = self.SetupButton("Button Styles/MUN Output.png", 300, 102)


    #starting fuction to run the 'application' by creating the settings button and running the mainloop
    def run(self):
        self.Settingsbutton()
        self.Translatebutton()
        self.root.mainloop()

    #functions to initialize the starting screen buttons
    def Translatebutton(self):
        self.translatebutton = tk.Button(self.root, image = self.TranslateButtonBack, border = "0", command=self.Translate)
        self.translatebutton.place(x=650, y=300, height=100, width=300)
    def Settingsbutton(self):
        self.settingbutton = tk.Button(self.root, image = self.SettingsButtonBack, border = "0", command = self.OpenSettings)
        self.settingbutton.place(x = 650, y = 500, height = 100, width = 300)
    def CloseTextbutton(self):
        self.closetextbutton = tk.Button(self.root, image = self.CloseButtonBack, border = "0", command=self.CloseText)
        self.closetextbutton.place(x=0, y=700, height=100, width=300)
    def NextTextbutton(self):
        self.nexttextbutton = tk.Button(self.root, image = self.NextButtonBack, border = "0", command=self.NextScreen)
        self.nexttextbutton.place(x=1300, y=700, height=100, width=300)

    def Translate(self):
        print("starting")
        inputtext = ""
        if (str(self.inputtype.get()) == "0"):
            self.CloseMainMenu()
            self.prepAudioInput()
            self.root.update_idletasks()
            #old code
            #x = self.prepAudioInput()
            #self.inputtext = Audio_Input.TakeInAudio(x)
            #self.CloseAudioMenu()
        elif (str(self.inputtype.get()) == "1"):
            self.inputtext = self.TextInput(inputtext)
        else:
            print("Invalid input method")
            print(self.inputtype)

    #TODO added from noah's, maybe here is where the title label should die as well
    def CloseMainMenu(self):
        self.settingbutton.destroy()
        self.translatebutton.destroy()
        self.Title.destroy()

    def CloseText(self):
        self.closetextbutton.destroy()
        #for one screen translations, the nexttext buton does not exist so added a try/catch
        try:
            self.nexttextbutton.destroy()
        except:
            z = 0
        try:
            self.SentenceLabel.destroy()
        except:
            z = 0
        try:
            self.repeatbutton.destroy()
            self.videosentence.destroy()
        except:
            z = 0
        try:
            for i in self.LabelArray:
                i.destroy()
            self.LabelArray.clear()
            Letter_Translation.Clear()
        except:
            z = 0
        # replace the main menu buttons and title
        self.Settingsbutton()
        self.Translatebutton()
        self.Title = tk.Label(self.root, image=self.TitleImage, border="0")
        self.Title.place(x=3, y=0)


    def TextInput(self, text):
        #remove main menu buttons
        self.settingbutton.destroy()
        self.translatebutton.destroy()
        self.Title.destroy()

        #insert textbox and button
        self.text = tk.Text(self.root,height = 3, font=('Arial', 18))
        self.text.place(x =275, y = 100)
        self.textgo = tk.Button(self.root, image = self.ProceedButtonBack, border = "0", command = self.TextPrint)
        self.textgo.place(x = 650, y = 500, height = 100, width = 300)

    def TextPrint(self):
        #send forward the text
        self.inputtext = self.text.get('1.0', tk.END)
        #print("inputtext = " + self.inputtext)
        self.text_list = TranslationInterface.TranslationInterface(self.root, self.inputtype.get(), self.outputtype.get(), self.inputtext)
        #print(self.text_list)

        if (str(self.outputtype.get()) == "0"):
            self.Display(self.text_list)
        elif(str(self.outputtype.get()) == "4"):
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
        if (str(self.outputtype.get()) == "0"):
            self.Display(self.text_list)
        elif (str(self.outputtype.get()) == "3"):  # new
            self.DisplayVideos(self.text_list)

    def prepAudioInput(self):
        self.Makenewbackground()
        self.audiobutton = tk.Button(self.root, image = self.PressThenSpeak, border = "0", command = self.Listen)
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

    #Old Audio Input
    '''def prepAudioInput2(self):
        # remove main menu buttons
        self.settingbutton.destroy()
        self.translatebutton.destroy()
        self.Title.destroy()
        self.audiobox = tk.Label(self.root, text="Please Provide Audio Input", font=('Arial', 18))
        self.audiobox.place(x=600, y=400, height=100, width=400)
        return 1;
        ##self.inputtext = Audio_Input.TakeInAudio()
    '''

    def CloseAudioMenu(self):
        self.b2.destroy()
        self.audiospeak.destroy() #new
        self.text_list = TranslationInterface.TranslationInterface(self.root, self.inputtype.get(), self.outputtype.get(), self.inputtext)
        # print(self.text_list)
        if (str(self.outputtype.get()) == "0"):
            self.Display(self.text_list)
        elif (str(self.outputtype.get()) == "4"): #new
            self.DisplayVideos(self.text_list)
        self.CloseTextbutton()

    #TODO New function noah added in order to work his audio UI thing
    #basically need to render a new background for 'provide audio input' sreen because main menu is being annoying
    def Makenewbackground(self):
        self.icon3 = Image.open(self.path)
        self.icon4 = self.icon.resize((1600, 800), Image.ANTIALIAS)
        self.background2 = ImageTk.PhotoImage(self.icon2)
        self.b2 = tk.Label(self.root, image = self.background)
        self.b2.pack(side = "bottom", fill = "both", expand = "yes")

    def OpenSettings(self):
        #testing things
        print("Settings")
        self.translatebutton.destroy()
        self.settingbutton.destroy()
        self.Title.destroy()
        #setting background
       # self.stnback = tk.Label(self.root, text = ' ', font = ('Arial', 18))
        #self.stnback.place(x = 400, y = 100, height = 650, width = 800)

        #OUTPUT SETTINGS
        #letter Translation
        self.stn1 = tk.Button(self.root, text = "Letters", font = ('Arial', 18), command = self.SetOutput0)
        self.stn1.place(x = 750, y = 450, height = 100, width = 140)
        #Word Videos, was the button for ASL_Lex
        self.stn2 = tk.Button(self.root, text="Videos", font=('Arial', 18), command = self.SetOutput4)
        self.stn2.place(x=950, y=450, height=100, width=140)
        #Handspeak Translation
        #self.stn3 = tk.Button(self.root, text="Handspeak", font=('Arial', 18), command = self.SetOutput2)
        #self.stn3.place(x=950, y=450, height=100, width=140)

        #letters(but with videos)
        #self.stn6 = tk.Button(self.root, text="letter Videos", font=('Arial', 18), command=self.SetOutput3)
        #self.stn6.place(x=550, y=610, height=100, width=140)
        #INPUT SETTINGS
        #audio input
        self.stn4 = tk.Button(self.root, text="Audio", font=('Arial', 18), command = self.SetInput0)
        self.stn4.place(x=750, y=250, height=100, width=140)
        #text input
        self.stn5 = tk.Button(self.root, text="Text", font=('Arial', 18), command = self.SetInput1)
        self.stn5.place(x=950, y=250, height=100, width=140)

        #BACKGROUND COLOURS
        #MUN (commented out so the button doesn't appear)
        #self.MUNButton = tk.Button(self.root, bg = "purple", command = self.SetUIMUN)
        #self.MUNButton.place(x=500, y=650, height=50, width=50)

        #FOREST
        #self.ForestButton = tk.Button(self.root, bg="green", command=self.SetUIForest)
        #self.ForestButton.place(x=600, y=650, height=50, width=50)

        #close settings
        self.stnc = tk.Button(self.root, image = self.CloseButtonBack, border = "0", command=self.CloseSettings)
        self.stnc.place(x=0, y=700, height=100, width=300)
        #inout and output header labels
        self.stninput = tk.Label(self.root, image = self.InputSettingButtonBack)
        self.stninput.place(x=300, y=250, height=100, width=300)
        self.stnoutput = tk.Label(self.root, image = self.OutputSettingButtonBack)
        self.stnoutput.place(x=300, y=450, height=100, width=300)

        #set apropriate buttons to green
        self.SetSettingsButtonColours()

    def CloseSettings(self):
        self.stn1.destroy()
        self.stn2.destroy()
        #self.stn3.destroy()
        self.stn4.destroy()
        self.stn5.destroy()
        #self.stn6.destroy()
        #self.stnback.destroy()
        self.stnc.destroy()
        self.stninput.destroy()
        self.stnoutput.destroy()
        #self.MUNButton.destroy()
        #self.ForestButton.destroy()
        self.Title = tk.Label(self.root, image=self.TitleImage, border="0")
        self.Title.place(x=3, y=0)
        self.Translatebutton()
        self.Settingsbutton()


    #settings changing functions for determining the translation method and output
    def SetInput0(self):
        self.inputtype.set(0)
        self.SetSettingsButtonColours()
        return self.inputtype
    def SetInput1(self):
        self.inputtype.set(1)
        self.SetSettingsButtonColours()
        return self.inputtype

    def SetOutput0(self):
        self.outputtype.set(0)
        self.SetSettingsButtonColours()
        return self.outputtype
    def SetOutput1(self):
        self.outputtype.set(1)
        self.SetSettingsButtonColours()
        return self.outputtype
    def SetOutput2(self):
        self.outputtype.set(2)
        self.SetSettingsButtonColours()
        return self.outputtype
    def SetOutput3(self):
        self.outputtype.set(3)
        self.SetSettingsButtonColours()
        return self.outputtype
    def SetOutput4(self):
        self.outputtype.set(4)
        self.SetSettingsButtonColours()
        return self.outputtype

    #TODO Rework if the is any other buttons added/removed
    def SetSettingsButtonColours(self):
        if(self.inputtype.get() == 0):
            self.stn4.configure(bg = "green")
            self.stn5.configure(bg = "#802433")
        elif(self.inputtype.get() == 1):
            self.stn5.configure(bg = "green")
            self.stn4.configure(bg = "#802433")
        else:
            print("Not Valid Input Type")

        if (self.outputtype.get() == 0):
            self.stn1.configure(bg="green")
            self.stn2.configure(bg="#802433")
            #self.stn3.configure(bg="#802433")
            #self.stn6.configure(bg="#802433")
        elif (self.outputtype.get() == 4):
            self.stn2.configure(bg="green")
            self.stn1.configure(bg="#802433")
            #self.stn3.configure(bg="#802433")
            #self.stn6.configure(bg="#802433")
        elif (self.outputtype.get() == 2):
            #self.stn3.configure(bg="green")
            self.stn1.configure(bg="#802433")
            self.stn2.configure(bg="#802433")
            #self.stn6.configure(bg="#802433")
        elif(self.outputtype.get() == 3):
            #self.stn6.configure(bg="green")
            #self.stn3.configure(bg="#802433")
            self.stn1.configure(bg="#802433")
            self.stn2.configure(bg="#802433")
        else:
            print("Not Valid Input Type")
        return

    #set button size and the image to "string"
    def SetupButton(self, string, w, h):
        img = Image.open(string)
        resize = img.resize((w, h), Image.ANTIALIAS)
        button = ImageTk.PhotoImage(resize)
        return button


    def SetUIMUN(self):
        self.TranslateButtonBack = self.SetupButton("Button Styles/MUN Translate.png")
        self.translatebutton.configure(image = self.TranslateButtonBack)
        self.SettingsButtonBack = self.SetupButton("Button Styles/MUN Settings.png")
        self.settingbutton.configure(image= self.SettingsButtonBack)
        self.CloseButtonBack = self.SetupButton("Button Styles/MUN Menu.png")
        #self.closetextbutton.configure(image= self.CloseButtonBack)
        self.ProceedButtonBack = self.SetupButton("Button Styles/MUN Proceed.png")
        #self.textgo.configure(image= self.ProceedButtonBack)
        self.NextButtonBack = self.SetupButton("Button Styles/MUN Next.png")
        #self.nexttextbutton.configure(image= self.NextButtonBack)
        self.SetBackground("Backgrounds/Bruneau Center Blurry.png")
        return

    def SetBackground(self, back):
        self.path = back
        self.icon = Image.open(self.path)
        self.icon2 = self.icon.resize((1600, 800), Image.ANTIALIAS)
        self.background = ImageTk.PhotoImage(self.icon2)
        self.b.configure(image = self.background)
        return

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

    def RepeatVideos(self):
        self.tkvideolabel.play()

    def DisplayVideos(self, input_list):
        print("This is where all of the Video work will be done")
        sentence = self.MergeVideos(input_list)
        self.videosentence = tk.Label(self.root, text = self.inputtext, font=('Arial', 24),padx = 5, wraplength = 1600, justify=tk.CENTER, borderwidth = 4, relief = "solid")
        self.videosentence.place( relx = 0.50, rely = 0, anchor = tk.N)
        self.SentenceLabel = tk.Label(self.root)
        self.SentenceLabel.place(x = 450, y = 100, height = 700, width = 700)
        self.tkvideolabel = tkvideo.tkvideo("sentence.mp4", self.SentenceLabel, loop=0, size=(700, 700))
        self.tkvideolabel.play()
        #TODO change function to repeat video
        self.repeatbutton = tk.Button(self.root, image=self.RepeatButtonBack, border="0", command=self.RepeatVideos)
        self.repeatbutton.place(x=1300, y=700, height=100, width=300)

        #self.stnback.place(x = 400, y = 100, height = 650, width = 800)

    def MergeVideos(self, input):
        mp4input = []

        for i in input:
            # check if the video is in our dictionary
            if (os.path.isfile("ASL Words/" + i + ".mp4")):
                i = "ASL Words/" + i + ".mp4"
                vi = VideoFileClip(i)
                mp4input.append(vi)
            else:
                list(i)
                for j in i:
                    j = "ASL Words/" + j + ".mp4"
                    vi = VideoFileClip(j)
                    mp4input.append(vi)

        final = concatenate_videoclips(mp4input, method='compose')
        final.write_videofile("sentence.mp4")
        return final


MyGUI