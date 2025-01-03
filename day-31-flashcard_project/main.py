import time
from tkinter import *
from tkinter import Canvas

import pandas
import pandas as pd
from PyInstaller.compat import system
from pandas.core.interchange.dataframe_protocol import DataFrame
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
words_to_learn = {}

window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flashcards")


canvas = Canvas(width=800, height=526)
canvas_card_front = PhotoImage(file="images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=canvas_card_front)
canvas_card_back = PhotoImage(file="images/card_back.png")
canvas.grid(column=0, row=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

language_text = canvas.create_text(400, 150, text="Japanese", font=("Arial", 40, "italic"))

language_word = canvas.create_text(400, 263, text="Words", font=("Arial", 30, "bold"))

#data = pd.read_csv("data/japanese_words_2.csv")
try:
    data = pd.read_csv("data/learned_words.csv")
except FileNotFoundError:
    data = pd.read_csv("data/japanese_words_2.csv")
    words_to_learn = data.to_dict(orient="records")
else:
    words_to_learn = data.to_dict(orient="records")



#print(data["japanese"][0])         this prints the FIRST position in JAPANESE column
#random_number = random.randint(0, 2999)



def next_card():
    #global random_number
    global other_side
    global current_card
    window.after_cancel(other_side)
    #random_number = random.randint(0, 2999)
    canvas.itemconfig(canvas_image, image = canvas_card_front)
    #jap_word = data["japanese"][random_number]
    current_card = random.choice(words_to_learn)
    canvas.itemconfig(language_word, text=current_card["japanese"], fill = "black")
    canvas.itemconfig(language_text, text="Japanese", fill = "black")
    other_side = window.after(3000, func=flip_card)


    #window.after_cancel(other_side)


def flip_card():

    canvas.itemconfig(language_text, text="English", fill = "white")
    canvas.itemconfig(canvas_image, image = canvas_card_back)
    #eng_word = data["English"][random_number]
    canvas.itemconfig(language_word, text=current_card["English"], fill = "white")

def is_known():

    words_to_learn.remove(current_card)
    #print(len(words_to_learn))
    learned_words = pandas.DataFrame(words_to_learn)
    learned_words.to_csv("data/learned_words.csv")
    next_card()


other_side = window.after(3000, func=next_card)

correct_image = PhotoImage(file="images/right.png")
button_correct = Button(image=correct_image, highlightthickness=0, command=is_known)
button_correct.grid(column=0, row=1)

wrong_image = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=wrong_image, highlightthickness=0, command=next_card)
button_wrong.grid(column=1, row=1)





window.mainloop()
