# -*- coding: utf-8 -*-

# Muntaha Chowdhury 12SDD2


import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
from tkinter import messagebox 




# setting up a window
root = Tk()
root.title("DiviWorld")
root.geometry("1150x700") 


def show_instructions():
    instructions = (
        "1. You will be presented with 10 division questions.\n"
        "2. Enter your answer in the text box.\n"
        "3. Click the 'Submit' button to submit your answer.\n"
        "4. If your answer is wrong, click the 'Try Again' button to reattempt the question.\n"
        "5. Your score will be displayed at the end of the quiz.\n"
        "                        Good luck!"
        )
    messagebox.showinfo("DiviWorld Instructions", instructions)



# creating font objects
fontobj1 = tkFont.Font(family="Comic Sans MS", size=25, weight="bold")
fontobj2 = tkFont.Font(family="Comic Sans MS", size=40, weight="bold")

# the messages on the welcome screen
welcome_label_1 = Label(root, text="Welcome to DiviWorld!", font=fontobj1)
welcome_label_1.grid(pady=20, row=5, column=2, sticky="WE")

welcome_label_2 = Label(root, text="Ready to amaze the world with your division skills? ʕ •`ᴥ•´ʔᕤ", font=fontobj1)
welcome_label_2.grid(pady=20, row=7, column=2, sticky="WE")

welcome_label_3 = Label(root, text="Click on the Bear to view instructions!", font=fontobj1)
welcome_label_3.grid(pady=60, row=9, column=2, sticky="WE")

instructions_button = Button(root, text="🐻", font=fontobj2, command=show_instructions)
instructions_button.grid(row=20, column=2)

# creating a frame to view instructions

# instructions_frame = tk.Frame(root)
# instructions_frame.grid(pady=30)

# instructions_label = Label(instructions_frame, text="Instructions:")
# instructions_label.grid(row=10, column=2)

# instructions_list = Label(instructions_frame, text="1. First, calculate your answer to the question displayed. \n2. Click the 'Submit' button." )

# creating a frame for the questions
# questions_frame = tkFrame(root)
# questions_frame.grid(pady=30)

# question_label = Label(questions_frame, text="")
 


















root.mainloop()