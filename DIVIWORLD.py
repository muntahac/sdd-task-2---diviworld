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

def show_main_frame():
    questions_frame.pack_forget()
    instructions_frame.pack_forget()
    main_frame.pack(fill='both', expand=True)
    
def show_instructions():
    main_frame.pack_forget()
    question_frame.pack_forget()
    instructions_frame.pack(fill='both', expand=True)
    instructions_label.config()
    instructions_list.config()
    
    # messagebox.showinfo("DiviWorld Instructions", instructions)
    # show_questions()

def show_questions():
    main_frame.pack_forget()
    instructions_frame.pack_forget()
    question_frame.pack(fill='both', expand=True)

    question_label.config(text="Question 1: What is 10 ÷ 2?")
    answer_entry.delete(0, tk.END)
    
def ok_button():
    instructions_frame.pack_forget()
    main_frame.pack_forget()
    question_frame.pack(fill='both', expand=True)
    
    question_label.config(text="Question 1: What is 10 ÷ 2?")
    answer_entry.delete(0, tk.END)

# creating font objects
fontobj1 = tkFont.Font(family="Comic Sans MS", size=25, weight="bold")
fontobj2 = tkFont.Font(family="Comic Sans MS", size=40, weight="bold")


# creating the main frame
main_frame = tk.Frame(root)
main_frame.pack(pady=20, fill="both", expand=True)

# the messages on the welcome screen
welcome_label_1 = Label(main_frame, text="Welcome to DiviWorld!", font=fontobj1)
welcome_label_1.pack(pady=20)

welcome_label_2 = Label(main_frame, text="Ready to amaze the world with your division skills? ʕ •`ᴥ•´ʔ", font=fontobj1)
welcome_label_2.pack(pady=20)

welcome_label_3 = Label(main_frame, text="Click on the Bear to view instructions!", font=fontobj1)
welcome_label_3.pack(pady=20)

instructions_button = Button(main_frame, text="🐻", font=fontobj2, command=show_instructions)
instructions_button.pack(pady=120)


#creating a frame for questions and answers
question_frame = tk.Frame(root)

question_label = tk.Label(question_frame, text="", font=("Comic Sans MS", 15))
question_label.pack(pady=20)

answer_entry = tk.Entry(question_frame, font=("Comic Sans MS", 15))
answer_entry.pack(pady=20)




# creating a frame to view instructions

instructions_frame = tk.Frame(root)
instructions_frame.pack(pady=20)

instructions_label = Label(instructions_frame, text="Instructions:", font=fontobj2)
instructions_label.pack(pady=20)

instructions_list = Label(instructions_frame, text=
    "1. You will be presented with 10 division questions.\n"
    "2. Enter your answer in the text box.\n"
    "3. Click the 'Submit' button to submit your answer.\n"
    "4. If your answer is wrong, click the 'Try Again' button to reattempt the question.\n"
    "5. Your score will be displayed at the end of the quiz.\n"
    "6. Click 'OK' to proceed.\n"
    "                                            \n"
    "Good luck!",
    font=("Comic Sans MS", 16))
instructions_list.pack(padx=20, pady=20)

ok_button = Button(instructions_frame, text="OK", font=fontobj2, command=ok_button)
ok_button.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-10)

# instructions_list = Label(instructions_frame, text="1. First, calculate your answer to the question displayed. \n2. Click the 'Submit' button." )




















root.mainloop()