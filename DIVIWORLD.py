# Muntaha Chowdhury 12SDD2


import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
from tkinter import messagebox 
from functools import partial
import random



# setting up a window
root = Tk()
root.resizable(0, 0)
root.title("DiviWorld")
root.geometry("750x600") 


# initialising variables
num_questions = 10
current_question = 1
correct_answers = 0
questions = []
question_history = []
text_size = 12
font_name = "Comic Sans MS"

def set_text_size(size):
    global text_size
    text_size = size
    for widget in widgets_to_configure:
        try:
            current_font = widget.cget("font")
            font_family = current_font.split()[0]
            widget.config(font=(font_family, text_size))
        except tk.TclError:
            pass
        
 

# this function hides other frames and only displays the main frame (welcome page)
def show_main_frame():
    question_frame.pack_forget()
    instructions_frame.pack_forget()
    feedback_frame.pack_forget()
    results_frame.pack_forget()
    main_frame.pack(side='top', fill='both', expand=True)

# this function hides the other frames and only displays the instruction frame
def show_instructions():
    main_frame.pack_forget()
    question_frame.pack_forget()
    instructions_frame.pack(side='top', fill='both', expand=True)
    
    
# this function generates a random dividend between 1-100 and a random divisor between 1-10
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
    feedback_frame.pack_forget()
    question_frame.pack(fill='both', expand=True)
        
def show_results():
    question_frame.pack_forget()
    feedback_frame.pack_forget()
    results_frame.pack(fill='both', expand=True)
    results_label.config(text=f"You got {correct_answers} out of {num_questions} correct!")
    
def ok_button():
    show_questions()
    
def set_text_size(size):
    global text_size
    text_size = size
    for widget in widgets_to_configure:
        try:
            current_font = widget.cget("font")
            font_family = current_font.split()[0]
            widget.config(font=(font_family, text_size))
        except tk.TclError:
            pass

def change_font(new_font_name):
    global font_name
    font_name = new_font_name
    for widget in widgets_to_configure:
        try:
            widget.config(font=(font_name, text_size))
        except tk.TclError:
            pass

def change_theme(theme_name):
    theme = theme_colors.get(theme_name)
    if theme:
        for widget in widgets_to_configure:
            try:
                widget.config(bg=theme["bg"], fg=theme["fg"])
            except tk.TclError:
                pass
        for frame in frames_to_configure:
            frame.config(bg=theme["bg"])
        root.config(bg=theme["bg"])

def create_menu(root):
    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)
    
    parent_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Edit", menu=parent_menu)
    
    # Text size submenu
    text_size_menu = tk.Menu(parent_menu, tearoff=0)
    parent_menu.add_cascade(label="Text Size", menu=text_size_menu)
    
    text_sizes = [10, 12, 14, 16, 18, 20]  
    for size in text_sizes:
        text_size_menu.add_command(label=str(size), command=lambda size=size: set_text_size(size))
         
    # Font submenu
    font_menu = tk.Menu(parent_menu, tearoff=0)
    parent_menu.add_cascade(label="Font", menu=font_menu)
   
    font_families = tkFont.families()
    for font_family in font_families:
        font_menu.add_command(label=font_family, command=lambda font_family=font_family: change_font(font_family))
        
    # Theme submenu
    theme_menu = tk.Menu(parent_menu, tearoff=0)
    parent_menu.add_cascade(label="Themes", menu=theme_menu)
   
    for theme_name in theme_colors:
        theme_menu.add_command(label=theme_name, command=lambda theme_name=theme_name: change_theme(theme_name))

# defining theme colors
theme_colors = {
    "Default": {"bg": "#F8C8DC", "fg": "#770737"},
    "Dark": {"bg": "black", "fg": "white"},
    "High Contrast": {"bg": "purple", "fg": "yellow"},
    "Blue": {"bg": "#7393B3", "fg": "#00008B"},
    "Light": {"bg":"white", "fg":"black"}
    
}



# creating the main frame, which includes welcome messages
main_frame = tk.Frame(root)
main_frame.pack(pady=20, fill="both", expand=True)

# the welcome messages on the main frame
welcome_label_1 = Label(main_frame, text="Welcome to DiviWorld!")
welcome_label_1.pack(pady=20)

welcome_label_2 = Label(main_frame, text="Ready to amaze the world with your division skills? ʕ •`ᴥ•´ʔ")
welcome_label_2.pack(pady=20)

welcome_label_3 = Label(main_frame, text="Click on the Bear to view instructions!")
welcome_label_3.pack(pady=20)

instructions_button = Button(main_frame, text="🐻", command=show_instructions)
instructions_button.pack(pady=150)

# creating a frame to view instructions

instructions_frame = tk.Frame(root)
instructions_frame.pack(pady=20)

instructions_label = Label(instructions_frame, text="Instructions:")
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
    )
instructions_list.pack(padx=20, pady=20)


# ok button to proceed to first question
ok_button = Button(instructions_frame, text="OK", command=ok_button)
ok_button.pack(pady=20)


#creating a frame for questions and answers
question_frame = tk.Frame(root)

question_label = tk.Label(question_frame, text="")
question_label.pack(pady=20)

answer_entry = tk.Entry(question_frame)
answer_entry.pack(pady=20)

submit_button = Button(question_frame, text="Submit", command=check_answer)
submit_button.pack(pady=20)


# creating a frame for feedback from each question
feedback_frame = tk.Frame(root)

feedback_label = Label(feedback_frame, text="")
feedback_label.pack(pady=20)


# proceed and back button
proceed_button = Button(feedback_frame, text="") 
proceed_button.pack(pady=20)

back_button = Button(feedback_frame, text="")
back_button.pack(pady=20)


# creating a frame to show results
results_frame = tk.Frame(root)

results_label = Label(results_frame, text="")
results_label.pack(pady=20)

restart_button = Button(results_frame, text="Back to Home", command=show_main_frame)
restart_button.pack(pady=20)



#  quit button
quit_button = Button(root, text="Quit", command=root.destroy)
quit_button.pack(side=tk.BOTTOM, anchor=tk.SE, padx=5, pady=5)

# list of widgets to configure
widgets_to_configure = [root, 
                        main_frame, 
                        welcome_label_1, 
                        welcome_label_2, 
                        welcome_label_3, 
                        instructions_button, 
                        instructions_frame, 
                        instructions_label,
                        instructions_list,
                        ok_button,
                        question_frame,
                        question_label,
                        answer_entry,
                        submit_button,
                        feedback_frame,
                        feedback_label,
                        proceed_button,
                        back_button,
                        results_frame,
                        results_label,
                        restart_button,
                        quit_button
                        ]

# list of frames to configure
frames_to_configure = [
    main_frame,
    instructions_frame,
    question_frame,
    feedback_frame,
    results_frame
]

widgets_to_configure_for_fonts = [welcome_label_1, 
                                  welcome_label_2, 
                                   welcome_label_3, 
                                   instructions_label, 
                                   feedback_label, 
                                   results_label, 
                                  instructions_button, 
                                  ok_button, 
                                  submit_button, 
                                  proceed_button, 
                                  back_button, 
                                  restart_button, 
                                  quit_button,
                                  answer_entry
    ]

for widget in widgets_to_configure_for_fonts:
    widget.config(font=(font_name, text_size))

create_menu(root)

root.mainloop()