import pandas
from tkinter import *
import random as r

BACKGROUND_COLOR = "#B1DDC6"
french_word = ""
word_no = 0
deleted_index = []
languages = ["English", "French"]
eng_word = ""
words_no = 0
new_dict = {
    "French": {},
    "English": {},
}

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


def unknown():
    next_card(inp="T")


def known():
    next_card(inp="F")


def french_csv():
    global csv_data, words_dict, no_of_words, deleted_index
    csv_data = pandas.read_csv("data/french_words.csv")
    words_dict = csv_data.to_dict()
    no_of_words = len(words_dict["French"])
    deleted_index = []


def next_card(inp="w"):
    global word_no, t, french_word, eng_word, new_dict, words_no, csv_data
    window.after_cancel(t)

    if inp == "T":
        new_dict["French"][words_no] = french_word
        new_dict["English"][words_no] = eng_word
        words_no += 1

        print(new_dict)

    elif inp == "F":
        print(words_dict)
        if len(words_dict["French"]) == 0:
            french_csv()
        else:
            words_dict["French"].pop(word_no)
            words_dict["English"].pop(word_no)
            deleted_index.append(word_no)
            if len(words_dict["French"]) == 0:
                french_csv()

    word_no = r.randint(0, no_of_words - 1)
    while word_no in deleted_index:
        word_no = r.randint(0, no_of_words - 1)
    print(word_no)
    french_word = words_dict[languages[1]][word_no]
    eng_word = words_dict[languages[0]][word_no]

    canva.itemconfig(card, image=gcard_image)
    canva.itemconfig(lang_canva, text=languages[1], fill="black")
    canva.itemconfig(word_canva, text=french_word, fill="black")
    print(words_dict)

    t = window.after(3000, flip_card)

    new_csv = pandas.DataFrame(new_dict)
    new_csv.to_csv("data/forgot_these_words.csv")


def flip_card():
    canva.itemconfig(card, image=wcard_image)
    canva.itemconfig(lang_canva, text=languages[0], fill="white")
    canva.itemconfig(word_canva, text=eng_word, fill="white")


try:
    csv_data = pandas.read_csv("data/forgot_these_words.csv")
except FileNotFoundError:
    csv_data = pandas.read_csv("data/french_words.csv")

words_dict = csv_data.to_dict()
no_of_words = len(words_dict["French"])

if no_of_words == 0:
    french_csv()

tick_image = PhotoImage(file="images/right.png")
cross_image = PhotoImage(file="images/wrong.png")
wcard_image = PhotoImage(file="images/card_back.png")
gcard_image = PhotoImage(file="images/card_front.png")

t = window.after(3000, flip_card)

card_face = gcard_image
canva = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card = canva.create_image(400, 263, image=gcard_image)
lang_canva = canva.create_text(400, 150, text=languages[1], font=("Ariel", 40, "italic"))
word_canva = canva.create_text(400, 263, text=french_word, font=("Ariel", 60, "bold"))
canva.grid(column=0, row=0, columnspan=2)

tick_b = Button(image=tick_image, bg=BACKGROUND_COLOR, command=known)
tick_b.grid(column=0, row=1)
cross_b = Button(image=cross_image, bg=BACKGROUND_COLOR, command=unknown)
cross_b.grid(column=1, row=1)

next_card()

window.mainloop()
