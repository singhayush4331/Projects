from turtle import Turtle

FONT = ("courier", 80, "normal")


class Points(Turtle):
    def __init__(self):
        super().__init__()
        self.l_points = 0
        self.r_points = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.print()
        # self.r_print()

    def print(self):
        self.goto(-150, 150)
        self.write(arg=self.l_points,font=FONT)
        self.goto(80, 150)
        self.write(arg=self.r_points, font=FONT)


    def l_ginoh(self):
        self.clear()
        self.l_points += 1
        self.print()

    def r_ginoh(self):
        self.clear()
        self.r_points += 1
        self.print()