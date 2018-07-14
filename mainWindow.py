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
from settingsWindow import settingsWindow

class mainWindow:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)

#self.master.overrideredirect(True)
        self.master.geometry("1184x624")
        self.uart = uart()
        
        # Background
        image = Image.open('poire.gif')
        self.copy_of_image = image.copy()
        self.photo = ImageTk.PhotoImage(image)
        self.label = tk.Label(self.master, image = self.photo)
        self.label.bind('<Configure>', self.resize_image)
        self.label.pack(fill=BOTH, expand = YES)
        
        # Labels
        self.pounds = StringVar()
        self.price = StringVar()
        self.pounds.set("lbs")		
        self.price.set("$")
        self.poundsLabel = Label(self.master, fg="white", background="#00dbde", textvariable=self.pounds, font=("Helvetica", 80,"bold"))
        self.priceLabel = Label(self.master, fg="white", background="#121212", textvariable=self.price, font=("Helvetica", 150,"bold"))
        self.poundsLabel.place(x=15, y=250)
        self.priceLabel.place(x=15, y=385)
        
        ## buttons
        #setting
        image = ImageTk.PhotoImage(Image.open('settings.png').resize((50, 50)))
        self.settingsLabel = Label(self.master,bg="white", height=50,image= image, width=50)
        self.settingsLabel.image = image
        self.settingsLabel.place(x=10, y=10)
        self.settingsLabel.bind("<Button>", self.open_settings)
        
        #Pomme
        image = ImageTk.PhotoImage(Image.open('settings.png').resize((200, 200)))
        self.pommeLabel = Label(self.master, height=200, width=200, image=image)
        self.pommeLabel.image = image
        self.pommeLabel.place(x=370, y=10)
        self.pommeLabel.bind("<Button>", self.open_settings)
        
        #Poire
        image = ImageTk.PhotoImage(Image.open('settings.png').resize((200, 200)))
        self.poireLabel = Label(self.master, height=200, width=200, image=image)
        self.poireLabel.image = image
        self.poireLabel.place(x=670, y=10)
        self.poireLabel.bind("<Button>", self.open_settings)
        
        #Prune
        image = ImageTk.PhotoImage(Image.open('settings.png').resize((200, 200)))
        self.pruneLabel = Label(self.master, height=200, width=200, image=image)
        self.pruneLabel.image = image
        self.pruneLabel.place(x=970, y=10)
        self.pruneLabel.bind("<Button>", self.open_settings)
        
        #Quality 1
        image = ImageTk.PhotoImage(Image.open('settings.png').resize((100, 100)))
        self.quality1Label = Label(self.master, height=100, width=100, image=image)
        self.quality1Label.image = image
        self.quality1Label.place(x=970, y=200)
        self.quality1Label.bind("<Button>", self.open_settings)
                
        #Quality 2
        image = ImageTk.PhotoImage(Image.open('settings.png').resize((100, 100)))
        self.quality2Label = Label(self.master, height=100, width=100, image=image)
        self.quality2Label.image = image
        self.quality2Label.place(x=970, y=300)
        self.quality2Label.bind("<Button>", self.open_settings)
                
        #Quality 3
        image = ImageTk.PhotoImage(Image.open('settings.png').resize((100, 100)))
        self.quality3Label = Label(self.master, height=100, width=100, image=image)
        self.quality3Label.image = image
        self.quality3Label.place(x=970, y=400)
        self.quality3Label.bind("<Button>", self.open_settings)
        
        
    def open_settings(self,event):
        self.settingsWindow = tk.Toplevel(self.master)
        self.app = settingsWindow(self.settingsWindow) 

    def resize_image(self, event):
        new_width = event.width
        new_height = event.height
        image = self.copy_of_image.resize((new_width, new_height))
        photo = ImageTk.PhotoImage(image)
        self.label.config(image = photo)
        self.label.image = photo #avoid garbage collection
    
    def render(self):
        try:
            rx = self.uart.readlineCR();
            pounds_on_balance = rx.value;
        except:
            pounds_on_balance = random.uniform(0.01, 999.99);
            print("Unexpected error:",sys.exc_info()[0])
    
        unit_price = 10.1;
        total = pounds_on_balance * unit_price;
        total = "%.2f" %total
        self.pounds.set(str("%.1f" %pounds_on_balance)+" lbs")
        self.price.set(str(total)+" $")
        
        self.master.after(refreshPeriod, self.render)