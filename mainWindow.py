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
from DB import *

data = getData()

class mainWindow:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.master.geometry("800x600")
        self.uart = uart()
        self.state = 0
        self.toggle_fullscreen();
        #self.master.overrideredirect(True)

        # Logo
        self.logoImage = ImageTk.PhotoImage(Image.open(resource_path('ressources/logo.gif')).resize((150, 125)))
        self.logo = tk.Label(self.master, image=self.logoImage)
        self.logo.place(x=6, y=80)

        # Labels
        self.pounds = StringVar()
        self.price = StringVar()
        self.pounds.set("lb")
        self.price.set("$")
        self.priceLabel = Label(self.master, bg="#ffffff", fg='#014E7E',textvariable=self.price, font=("Helvetica", 113,"bold"))
        self.poundsLabel = Label(self.master, bg="#ffffff",fg='#014E7E',textvariable=self.pounds, font=("Helvetica", 44,"bold"))

        self.priceLabel.place(x=9, y=370)
        self.poundsLabel.place(x=9, y=295)

        # Settings Button
        self.settingsImage = ImageTk.PhotoImage(Image.open(resource_path('ressources/settings.png')).resize((50, 50)))
        self.settingsButton = Button(self.master,bg="#ffffff", image=self.settingsImage, command=self.open_settings)
        self.settingsButton.place(x=0, y=0)

        # Fruit Selector
        self.selectedFruit = StringVar()
        self.selectedFruit.set("Pomme")

        #Quality Frame
        qualityFrame = Frame(self.master)
        qualityFrame.configure(background="white")
        qualityFrame.place(x=720, y=300, anchor='c')

        # Apple
        self.appleImage = ImageTk.PhotoImage(Image.open(resource_path('ressources/apple.gif')).resize((189, 189)))
        self.appleSelectImage = ImageTk.PhotoImage(Image.open(resource_path('ressources/appleSelect.gif')).resize((189, 189)))
        self.fruitApple = Radiobutton(self.master, image=self.appleImage, selectimage=self.appleSelectImage,
                                      value="Pomme", variable=self.selectedFruit, indicatoron=0)
        self.fruitApple.place(x=180,y=10)

        # Pear
        self.pearImage = ImageTk.PhotoImage(Image.open(resource_path('ressources/pear.gif')).resize((189, 189)))
        self.pearSelectImage = ImageTk.PhotoImage(Image.open(resource_path('ressources/pearSelect.gif')).resize((189, 189)))
        self.fruitPear = Radiobutton(self.master, image=self.pearImage, selectimage=self.pearSelectImage, value="Poire", variable=self.selectedFruit,
                                       indicatoron=0)
        self.fruitPear.place(x=400,y=10)

        # Quality Selector
        self.selectedQuality = StringVar()
        self.selectedQuality.set("Arbre")


        # Tree
        self.qualityTree = Radiobutton(qualityFrame, text="ARBRE",  height= 2, width = 10,value="Arbre", variable=self.selectedQuality,
                                       indicatoron=0,font=("Helvetica", 25, "bold"),
                                       pady=50, relief=SUNKEN, bg='white', selectcolor='#014E7E')
        self.qualityTree.pack(anchor=CENTER)

        # Ground
        self.qualityGround = Radiobutton(qualityFrame, height= 2, width = 10, text="SOL", value="Sol", variable=self.selectedQuality,
                                       indicatoron=0, font=("Helvetica", 25, "bold"),
                                         pady=50, relief=SUNKEN, bg='white', selectcolor='#014E7E')
        self.qualityGround.pack(anchor=CENTER)

        # Store
        self.qualityStore = Radiobutton(qualityFrame,  height= 2,  width = 10, text="KIOSQUE", value="Kiosque", variable=self.selectedQuality,
                                       indicatoron=0, font=("Helvetica", 25, "bold"),
                                        pady=50, relief=SUNKEN, bg='white', selectcolor='#014E7E')
        self.qualityStore.pack(anchor=CENTER)

    def toggle_fullscreen(self):
        print("toggle Fullscreen")
        self.state = not self.state  # Just toggling the boolean
        self.master.attributes("-fullscreen", self.state)
        return "break"

    def end_fullscreen(self):
        print("FullScreen")
        self.state = False
        self.master.attributes("-fullscreen", False)
        return "break"

    def on_closing(self):
        global data
        self.toggle_fullscreen()
        data = getData()
        self.master.overrideredirect(True)

    def open_settings(self):
        self.toggle_fullscreen();
        self.settingsWindow = tk.Toplevel(self.master)
        self.master.overrideredirect(False)
        self.app = settingsWindow(self)

    def resize_image(self, event):
        new_width = event.width
        new_height = event.height
        image = self.copy_of_image.resize((new_width, new_height))
        photo = ImageTk.PhotoImage(image)
        self.label.config(image = photo)
        self.label.image = photo #avoid garbage collection

    def get_unit_price(self):
        price = data[keyFruitIndex(self.selectedFruit.get())][self.selectedQuality.get()]
        return price

    def render(self):
        try:
            with Timeout(1):
                rx = self.uart.readlineCR();
                pounds_on_balance = rx.value;
                unit_price = self.get_unit_price();
                total = pounds_on_balance * unit_price;
                total = "%.2f" %total
                self.pounds.set(str("%.1f" %pounds_on_balance)+" lb")
                self.price.set(str(total)+" $")
        except Exception as e:
            print(e)
            self.pounds.set("Check connection")
            self.price.set("No data.")

        self.master.after(refreshPeriod, self.render)
