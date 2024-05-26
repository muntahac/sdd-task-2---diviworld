# -*- coding: utf-8 -*-

# Muntaha Chowdhury 12SDD2


import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
from tkinter import messagebox 
import random



# setting up a window
root = Tk()
root.title("DiviWorld")
root.geometry("1150x700") 

# initialising variables
num_questions = 10
current_question = 1
correct_answers = 0
questions = []
question_history = []

# this function hides other frames and only displays the main frame (welcome page)
def show_main_frame():
    question_frame.pack_forget()
    instructions_frame.pack_forget()
    feedback_frame.pack_forget()
    results_frame.pack_forget()
    main_frame.pack(side='top', fill='both', expand=True)


def show_instructions():
    main_frame.pack_forget()
    question_frame.pack_forget()
    instructions_frame.pack(side='top', fill='both', expand=True)
    
def generate_questions():
    global questions
    questions = []
    for i in range(1, num_questions + 1):
        b = random.randint(1, 10)
        max_a = 100
        max_multiplier = max_a // b
        multiplier = random.randint(1, max_multiplier)
        a = b * multiplier
        correct_answer = a // b
        questions.append((a, b, correct_answer))

def show_questions():
    global current_question, correct_answers, question_history
    main_frame.pack_forget()
    instructions_frame.pack_forget()
    feedback_frame.pack_forget()
    question_frame.pack(fill='both', expand=True)
    
    correct_answers = 0
    current_question = 1
    question_history = []
    generate_questions()
    display_question()

    
def display_question():
    global current_question
    if current_question <= num_questions:
        a, b, _ = questions[current_question - 1]
        question_label.config(text=f"Question {current_question}: What is {a} ÷ {b}?")
        answer_entry.delete(0, tk.END)
    else:
        show_results()
        
def check_answer():
    global current_question, correct_answers
    try:
        user_answer = int(answer_entry.get())
        _, _, correct_answer = questions[current_question - 1]
        if user_answer == correct_answer:
            correct_answers += 1
            show_feedback(True)
        else:
            show_feedback(False)
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number.")
        
def show_feedback(is_correct):
    question_frame.pack_forget()
    feedback_frame.pack(fill='both', expand=True)
    if is_correct:
        feedback_label.config(text="Correct!\n"
                              "Great job!")
        proceed_button.config(text="Proceed", command=next_question)
        back_button.config(text="Try Again", command=back_to_previous_question)
    else:
        feedback_label.config(text="Incorrect!\n"
                              "Please try again.")
        proceed_button.config(text="Proceed", command=next_question)
        back_button.config(text="Try Again", command=back_to_previous_question)
    
def next_question():
   global current_question
   current_question += 1
   if current_question > num_questions:
        show_results()
   else:
        display_question()
        feedback_frame.pack_forget()
        question_frame.pack(fill='both', expand=True)
        
def back_to_previous_question():
    global current_question
    display_question()
    # if current_question > 1:
        # current_question -= 1
        # display_question()
    feedback_frame.pack_forget()
    question_frame.pack(fill='both', expand=True)
        
def show_results():
    question_frame.pack_forget()
    feedback_frame.pack_forget()
    results_frame.pack(fill='both', expand=True)
    results_label.config(text=f"You got {correct_answers} out of {num_questions} correct!")
    
def ok_button():
    show_questions()
    
def create_menu(root):
    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)
    
    

# creating font objects
fontobj1 = tkFont.Font(family="Comic Sans MS", size=25, weight="bold")
fontobj2 = tkFont.Font(family="Comic Sans MS", size=40, weight="bold")


# creating the main frame, which includes welcome messages
main_frame = tk.Frame(root, bg="Pink")
main_frame.pack(pady=20, fill="both", expand=True)

# the welcome messages on the main frame
welcome_label_1 = Label(main_frame, text="Welcome to DiviWorld!", font=fontobj1)
welcome_label_1.pack(pady=20)

welcome_label_2 = Label(main_frame, text="Ready to amaze the world with your division skills? ʕ •`ᴥ•´ʔ", font=fontobj1)
welcome_label_2.pack(pady=20)

welcome_label_3 = Label(main_frame, text="Click on the Bear to view instructions!", font=fontobj1)
welcome_label_3.pack(pady=20)

instructions_button = Button(main_frame, text="🐻", font=fontobj2, command=show_instructions)
instructions_button.pack(pady=120)

# creating a frame to view instructions

instructions_frame = tk.Frame(root, bg="Pink")
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


# ok button to proceed to first question
ok_button = Button(instructions_frame, text="OK", font=fontobj2, command=ok_button)
ok_button.place(relx=1.0, rely=1.0, anchor='se', x=-200, y=-60)


#creating a frame for questions and answers
question_frame = tk.Frame(root, bg="Pink")

question_label = tk.Label(question_frame, text="", font=("Comic Sans MS", 15))
question_label.pack(pady=20)

answer_entry = tk.Entry(question_frame, font=("Comic Sans MS", 15))
answer_entry.pack(pady=20)

submit_button = Button(question_frame, text="Submit", font=fontobj1, command=check_answer)
submit_button.pack(pady=20)


# creating a frame for feedback from each question
feedback_frame = tk.Frame(root, bg="Pink")

feedback_label = Label(feedback_frame, text="", font=fontobj1)
feedback_label.pack(pady=20)


# proceed and back button
proceed_button = Button(feedback_frame, text="", font=fontobj1) 
proceed_button.pack(pady=20)

back_button = Button(feedback_frame, text="", font=fontobj1)
back_button.pack(pady=20)


# creating a frame to show results
results_frame = tk.Frame(root, bg="Pink")

results_label = Label(results_frame, text="", font=fontobj1)
results_label.pack(pady=20)

restart_button = Button(results_frame, text="Back to Home", font=fontobj1, command=show_main_frame)
restart_button.pack(pady=20)



#  quit button
quit_button = Button(root, text="Quit", font=fontobj1, command=root.destroy)
quit_button.pack(side=tk.BOTTOM, anchor=tk.SE, padx=5, pady=5)





root.mainloop()