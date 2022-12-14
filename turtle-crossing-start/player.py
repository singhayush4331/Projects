from turtle import Turtle, Screen

screen = Screen()

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.kachua = Turtle(shape="turtle")
        self.hideturtle()
        self.kachua_banao()
        self.kachua_ycor = self.kachua.ycor()


    def kachua_banao(self):
        self.kachua.penup()
        self.kachua.color("black")
        self.kachua.goto(0, -275)
        self.kachua.setheading(90)

    def upper_jao(self):
        self.kachua_ycor = self.kachua.ycor()
        self.kachua_ycor += 5
        self.kachua.goto(0, self.kachua_ycor)

    def waapsi(self):
        self.kachua.goto(0, 0)





