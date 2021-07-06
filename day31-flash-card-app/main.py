from tkinter import *
import pandas as pd
import random
import csv

BACKGROUND_COLOR = "#B1DDC6"

data = pd.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")

# functions
last_word = None
eng_word = None
words_learner = {}

try:
    learner = pd.read_csv("./words_learner.csv")
    words_learner = learner.to_dict(orient="records")
except FileNotFoundError:
    q = pd.DataFrame(words_learner)
    q.to_csv("./words_learner.csv")


def i_knew():
    global last_word, words_learner
    words_learner += str(last_word)

    with open("./words_learner.csv", mode="a") as data1:
        writer = csv.writer(data1, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([last_word])

    print(f"word added {last_word}")
    next_card()


def next_card():
    global eng_word, flip_timer, words_learner, last_word
    window.after_cancel(flip_timer)

    set_of_words = random.choice(to_learn)

    eng_word = set_of_words["English"]
    fr_word = set_of_words["French"]

    if fr_word not in words_learner:
        canvas.itemconfig(card_title, text="French", fill="black")
        canvas.itemconfig(card_title2, text=fr_word, fill="black")
        canvas.itemconfig(face_of_card, image=card_front)
        flip_timer = window.after(3000, func=flip_card)
        last_word = fr_word
    else:
        next_card()


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_title2, text=eng_word, fill="white")
    canvas.itemconfig(face_of_card, image=card_back)


# Screen

window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# images
x_image = PhotoImage(file="./images/wrong.png")
ok_image = PhotoImage(file="./images/right.png")

card_back = PhotoImage(file="./images/card_back.png")
card_front = PhotoImage(file="./images/card_front.png")

# Buttons
x_button = Button(image=x_image, highlightthickness=0, command=next_card)
x_button.grid(column=0, row=1)
ok_button = Button(image=ok_image, highlightthickness=0, command=i_knew)
ok_button.grid(column=1, row=1)

# card font
canvas = Canvas(width=800, height=526, highlightthickness=0)
face_of_card = canvas.create_image(400, 263, image=card_front)
canvas.config(bg=BACKGROUND_COLOR)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_title2 = canvas.create_text(400, 263, text="", font=("Ariel", 40, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

next_card()

window.mainloop()
