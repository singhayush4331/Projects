from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.chapoo()


    def chapoo(self):
        self.clear()
        self.write(arg=f"Level: {self.score}", font= FONT)

    def score_ginoh(self):
        self.score += 1
        self.chapoo()

    def score_reset(self):
        self.goto(-40, 0)
        self.chapoo()
