# -*- coding: utf-8 -*-
from tkinter import *
import tkinter as tk
import tkinter.font
from PIL import ImageTk, Image
import random
import time
import collections
from constant import *
from uart import *
from time import sleep
from DB import *

size = 29
textFont1 = ("Arial", size, "bold")
textFont2 = ("Arial", size, "bold")
textFont3 = ("Arial", size, "bold")
data = getData();

class settingsWindow:
    def __init__(self, master):
        self.EXIT = False;
        self.parent = master
        self.master = master.settingsWindow

        # Settings Button
        self.settingsImage = ImageTk.PhotoImage(Image.open(resource_path('ressources/quit.png')).resize((50, 75)))
        self.button1 = Button(self.master, bg="#ffffff", image=self.settingsImage, command=self.close_windows)
        self.button1.place(x=5*rationX, y=5)

        # Logo
        self.logoImage = ImageTk.PhotoImage(Image.open(resource_path('ressources/logo.gif')).resize((200, 150)))
        self.logo = tk.Label(self.master, image=self.logoImage)
        self.logo.place(x=284, y=10)

        # Algorithme Solutions Inc.
        self.algoImage = ImageTk.PhotoImage(Image.open(resource_path('ressources/algorithmeSolutionsinc.gif')).resize((75, 75)))
        self.algologo = tk.Label(self.master, image=self.algoImage)
        self.algologo.place(x=650, y=390)
        self.algo = StringVar()
        self.algo.set("par Algorithme Solutions inc.")
        self.algoLabel = Label(self.master, bg="#ffffff", fg='#2A2C2D',textvariable=self.algo, font=("Helvetica", 25,"bold"))
        self.algoLabel.place(x=170, y=430)

        #self.master.overrideredirect(True)
        self.master.geometry("1184x624")

        self.cols = quality[:]
        self.quality = quality[:]
        self.quality.insert(0, "")
        self.fruit = fruit

        self.mainFrame = self.master
        self.mainFrame.configure(background="white")
        self.mainFrame.config(padx='3.0m', pady='3.0m')

        self.make_header()
        self.gridDict = {}
        for i in range(1, len(self.quality)):
            for j in range(len(self.fruit)):
                w = EntryWidget(self.mainFrame, i, j+1)
                w.value.set(data[j][keyQualityName(i-1)])
                self.gridDict[(i-1,j)] =w.value
                def handler(event, col=i-1, row=j):
                    return self.__entryhandler(col, row)
                w.place(x=((180*i)+13), y=((size+20)*j)+224)
                w.bind(sequence="<FocusOut>", func=handler)
                if i == len(self.quality)-1 and j == len(self.fruit)-1:
                    w.focus_set()

    def make_header(self):
        self.hdrDict = {}
        for i, label in enumerate(self.quality):
            def handler(event, col=i, row=0, text=label):
                return self.__headerhandler(col, row, text)
            w = LabelWidget(self.mainFrame, i, 0, label)
            w.place(x=((180*i)+13), y=180)
            self.hdrDict[(i,0)] = w
            #w.bind(sequence="<KeyRelease>", func=handler)

        for i, label in enumerate(self.fruit):
            def handler(event, col=0, row=i+1, text=label):
                return self.__headerhandler(col, row, text)
            w = LabelWidget(self.mainFrame, 0, i+1, label)
            w.place(x=13, y=((size+20)*i)+224)
            self.hdrDict[(0,i+1)] = w
            #w.bind(sequence="<KeyRelease>", func=handler)

    def __entryhandler(self, col, row):
        print(self.gridDict[col,row].get())
        data[row][keyQualityName(col)] = self.gridDict[col,row].get();
        print(data);
        writeJSON(data);

        print(self.EXIT)
        if self.EXIT == True:
            self.parent.on_closing() # Make DB change in MainWindow
            self.master.destroy()

    def demo(self):
        ''' enter a number into each Entry field '''
        for i in range(len(self.cols)):
            for j in range(len(self.fruit)):
                sleep(0.25)
                self.set(i,j,"")
                self.update_idletasks()
                sleep(0.1)
                self.set(i,j,i+1+j)
                self.update_idletasks()

    def __headerhandler(self, col, row, text):
        ''' has no effect when Entry state=readonly '''
        self.hdrDict[(col,row)].text.set(text)

    def get(self, x, y):
        return self.gridDict[(x,y)].get()

    def set(self, x, y, v):
        self.gridDict[(x,y)].set(v)
        return v

    def resize_image(self, event):
        new_width = event.width
        new_height = event.height
        image = self.copy_of_image.resize((weight, height))
        photo = ImageTk.PhotoImage(image)
        self.label.config(image = photo)
        self.label.image = photo

    def close_windows(self):
        self.EXIT =True;
        self.button1.focus_set()

class LabelWidget(tkinter.Entry):
    def __init__(self, master, x, y, text):
        self.text = tkinter.StringVar()
        self.text.set(text)
        tkinter.Entry.__init__(self, master=master)
        self.config(relief="ridge", font=textFont1,
                    bg="#014e7e", fg="#ffffff",
                    readonlybackground="#014e7e",
                    justify='center',width=8,
                    textvariable=self.text,
                    state="readonly")
        self.grid(column=x, row=y)

class EntryWidget(tkinter.Entry):
    def __init__(self, master, x, y):
        tkinter.Entry.__init__(self, master=master)
        self.value = tkinter.DoubleVar()
        self.config(textvariable=self.value, width=8,
                    relief="ridge", font=textFont1,
                    bg="#ffffff", fg="#000000000",
                    justify='center')
        self.grid(column=x, row=y)
