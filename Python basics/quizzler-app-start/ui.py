from tkinter import *
from quiz_brain import QuizBrain
import time as t

THEME_COLOR = "#375362"
FONT = ("Ariel", 20, "italic")


class UI:
    def __init__(self, q: QuizBrain):
        self.quest = q
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        right_b_i = PhotoImage(file="images/true.png")
        wrong_b_i = PhotoImage(file="images/false.png")

        self.canvas = Canvas(width=300, height=250)
        self.canvas_q = self.canvas.create_text(
            150,
            125,
            width=300,
            text="nacho",
            fill=THEME_COLOR,
            font=FONT)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.score = Label(text="Score = 0", fg="#FFFFFF", bg=THEME_COLOR)
        # self.score.config(padx=20, pady=20)
        self.score.grid(column=1, row=0)

        self.right_b = Button(image=right_b_i, bg=THEME_COLOR, highlightthickness=0, command=self.true)
        # self.right_b.config(padx=20, pady=20)
        self.right_b.grid(column=0, row=2)

        self.wrong_b = Button(image=wrong_b_i, bg=THEME_COLOR, highlightthickness=0, command=self.false)
        # self.wrong_b.config(padx=20, pady=20)
        self.wrong_b.grid(column=1, row=2)
        self.chapo()
        self.window.mainloop()

    def chapo(self):
        self.canvas.config(bg="#FFFFFF")
        if self.quest.still_has_questions():
            text = self.quest.next_question()
            self.canvas.itemconfig(self.canvas_q, text=text)
        else:
            self.canvas.itemconfig(self.canvas_q, text="You reached the limit")
            self.right_b.config(state="disable")
            self.wrong_b.config(state="disable")

    def true(self):
        self.s, is_right = self.quest.check_answer("True")
        self.change_bg(is_right)

    def false(self):
        self.s, is_right = self.quest.check_answer("False")
        self.change_bg(is_right)



    def change_bg(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.score.config(text=f"Score: {self.s}")
        self.window.after(1000, self.chapo)

# m = UI()
# m.gui()



