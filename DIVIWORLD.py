# -*- coding: utf-8 -*-


import tkinter as tk
from tkinter import *
import tkinter.font as tkFont




root = Tk()
root.title("DiviWorld")



# creating a font object
fontobj = tkFont.Font(family="Comic Sans MS", size=30, weight="bold")

# the messages on the welcome screen
welcome_label_1 = Label(root, text="Welcome to DiviWorld!", font=fontobj).grid(row=5, column=1, sticky="WE")
welcome_label_2 = Label(root, text="Ready to amaze the world with your division skills?", font=fontobj).grid(row=7, column=1, sticky="WE")
welcome_label_3 = Label(root, text="Click on the Bear to view instructions!", font=fontobj).grid(row=9, column=1, sticky="WE")






root.grid_columnconfigure(0, weight=1) 


root.geometry("1000x700")















root.mainloop()