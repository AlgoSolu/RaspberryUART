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
import json

size = 58
textFont1 = ("Arial", size, "bold italic")
textFont2 = ("Arial", size, "bold")
textFont3 = ("Arial", size, "bold")

colList = ['Pomme', 'Poire', 'Prune']
rowList = ['Arbre', 'Sol', 'Kiosque']
def keyQuality(x):
    return {
        0:'Arbre',
        1:'Sol',
        2:'Kiosque'
    }[x]

def writeJSON():
    with open('data.txt', 'w') as outfile:
        json.dump(data, outfile)
data =[]
for c in colList:
    data1 = {}
    data1['name'] = c
    for r in rowList:
        data1[r] = 0.0
    data.append(data1)

try :
    with open('data.txt') as json_file:
        data = json.load(json_file)
        i=0
        for c in colList:
            print(data[i])
            i=i+1
except:
    writeJSON()

class settingsWindow:
    def __init__(self, master):
        self.EXIT =False;
        self.master = master
        # Background
        image = Image.open('poire.gif')
        if image.size != (width, height):
            image = image.resize((width, height), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)
        bg_label = tk.Label(self.master, image = image)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        bg_label.image = image

        #self.master.overrideredirect(True)
        self.master.geometry("1184x624")

        self.cols = colList[:]
        self.colList = colList[:]
        self.colList.insert(0, "")
        self.rowList = rowList

        self.mainFrame = self.master
        self.mainFrame.config(padx='3.0m', pady='3.0m')

        # buttons
        self.button1 = Button(self.master, text= 'Quit', height= 5, width= 5, command = self.close_windows)
        self.button1.place(x=5, y=5)

        self.make_header()
        self.gridDict = {}
        for i in range(1, len(self.colList)):
            for j in range(len(self.rowList)):
                w = EntryWidget(self.mainFrame, i, j+1)
                w.value.set(data[i-1][keyQuality(j)])
                self.gridDict[(i-1,j)] =w.value
                def handler(event, col=i-1, row=j):
                    return self.__entryhandler(col, row)
                w.place(x=(276*i)+40, y=((size+20)*j)+330)
                w.bind(sequence="<FocusOut>", func=handler)
                if i == len(self.colList)-1 and j == len(self.rowList)-1:
                    w.focus_set()

    def make_header(self):
        self.hdrDict = {}
        for i, label in enumerate(self.colList):
            def handler(event, col=i, row=0, text=label):
                return self.__headerhandler(col, row, text)
            w = LabelWidget(self.mainFrame, i, 0, label)
            w.place(x=(276*i)+40, y=255)
            self.hdrDict[(i,0)] = w
            #w.bind(sequence="<KeyRelease>", func=handler)

        for i, label in enumerate(self.rowList):
            def handler(event, col=0, row=i+1, text=label):
                return self.__headerhandler(col, row, text)
            w = LabelWidget(self.mainFrame, 0, i+1, label)
            w.place(x=40, y=((size+20)*i)+330)
            self.hdrDict[(0,i+1)] = w
            #w.bind(sequence="<KeyRelease>", func=handler)

    def __entryhandler(self, col, row):
        print(self.gridDict[col,row].get())
        data[col][keyQuality(row)] = self.gridDict[col,row].get();
        print(data);
        writeJSON();

        print(self.EXIT)
        if self.EXIT == True:
            self.master.destroy()

    def demo(self):
        ''' enter a number into each Entry field '''
        for i in range(len(self.cols)):
            for j in range(len(self.rowList)):
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
        self.label.image = photo #avoid garbage collection

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
