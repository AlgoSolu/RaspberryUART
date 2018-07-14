# -*- coding: utf-8 -*-
from tkinter import *
import tkinter as tk
import tkinter.font
from PIL import ImageTk, Image
import time
from mainWindow import mainWindow
from constant import *

def exit():
    root.quit()

def initScreen():
    root = tk.Tk()
    print("width:", root.winfo_screenwidth(), "height:", root.winfo_screenheight())
    return root

def main():
    root =initScreen();
    app  = mainWindow(root)
    root.after(refreshPeriod, app.render)
    root.mainloop()

if __name__ == '__main__':
    main();
