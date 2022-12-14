from turtle import Turtle

s = 5

s_ycor = 300

st = (s/2) + s


class Daayara(Turtle):
    def __init__(self):
        super().__init__()
        self.daayara_banao()
        self.daayara = []

    def daayara_banao(self):
        self.ordinate = 300
        self.s_ycor = 300
        for i in range(int(150/st)):
            daayara = Turtle("square")
            daayara.color("white")
            daayara.shapesize(1, 1/10)
            daayara.penup()
            self.ordinate = self.ordinate - (st*4)
            daayara.goto(0, self.ordinate)
            # self.daayara.append()

