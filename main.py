from tkinter import *
from pandas import *
from random import *

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------------- GENERATE RANDOM ----------------------------------#
try:
    data = read_csv("data/learn.csv")
except FileNotFoundError:
    data = read_csv("data/french_words.csv")
    language = data.to_dict(orient="records")
else:
    language = data.to_dict(orient="records")
cards = {}


def generate_number():
    global cards, timer
    window.after_cancel(timer)
    cards = choice(language)
    canvas.itemconfig(card, image=CARD_FRONT)
    canvas.itemconfig(lang, text="French", fill="black")
    canvas.itemconfig(word, text=f"{cards['French']}", fill="black")
    window.after(3000, func=flip)


def flip():
    canvas.itemconfig(card, image=CARD_BACK)
    canvas.itemconfig(lang, text="English", fill="white")
    canvas.itemconfig(word, text=f"{cards['English']}", fill="white")


def correct():
    language.remove(cards)
    print(len(language))
    learn = DataFrame(language)
    learn.to_csv("data/learn.csv", index=False)
    generate_number()


# ---------------------------------- UI ----------------------------------#

window = Tk()
window.config(pady=50, padx=50, background=BACKGROUND_COLOR)
window.title("Flash Card")
timer = window.after(3000, func=flip)

canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
CARD_FRONT = PhotoImage(file='images/card_front.png')
CARD_BACK = PhotoImage(file='images/card_back.png')
card = canvas.create_image(400, 263, image=CARD_FRONT)
canvas.grid(row=0, column=0, columnspan=2)
lang = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))

RIGHT = PhotoImage(file='images/right.png')
RIGHT_BUTTON = Button(image=RIGHT, highlightthickness=0, borderwidth=0, command=correct)
RIGHT_BUTTON.grid(row=1, column=1)

LEFT = PhotoImage(file='images/wrong.png')
LEFT_BUTTON = Button(image=LEFT, highlightthickness=0, borderwidth=0, command=generate_number)
LEFT_BUTTON.grid(row=1, column=0)

generate_number()

mainloop()
