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

class settingsWindow:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        #self.master.overrideredirect(True)
        self.master.geometry("1184x624")
        
        # Background
        image = Image.open('poire.gif')
        self.copy_of_image = image.copy()
        self.photo = ImageTk.PhotoImage(image)
        self.label = tk.Label(self.master, image = self.photo)
        self.label.bind('<Configure>', self.resize_image)
        self.label.pack(fill=BOTH, expand = YES)
        
        # buttons
        self.button1 = Button(self.master, text= 'Quit', height= 5, width= 5, command = self.close_windows)
        self.button1.place(x=5, y=5)
        #self.button1.pack()
        #self.frame.pack()
        
    def resize_image(self, event):
        new_width = event.width
        new_height = event.height
        image = self.copy_of_image.resize((new_width, new_height))
        photo = ImageTk.PhotoImage(image)
        self.label.config(image = photo)
        self.label.image = photo #avoid garbage collection
    
    def close_windows(self):
        self.master.destroy()
