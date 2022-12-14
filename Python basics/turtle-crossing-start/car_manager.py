from turtle import Turtle, Screen
import random as r

screen = Screen()
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.gaadiya = []
        self.ordinate = 0
        self.abscissa = 300
        self.x = 0
        self.raftaar = STARTING_MOVE_DISTANCE


    def gaadi_aao(self):
        abhi_banao = r.randint(1,6)
        if abhi_banao == 1:
            gaadi = Turtle(shape="square")
            gaadi.color(r.choice(COLORS))
            gaadi.shapesize(stretch_wid=1, stretch_len=2)
            gaadi.penup()
            self.ordinate = r.randint(-250, 250)
            gaadi.goto(self.abscissa, self.ordinate)
            self.gaadiya.append(gaadi)

    def gaadi_aage_aao(self):
        for i in self.gaadiya:
            i.backward(self.raftaar)

    def speed_badhao(self):
        for i in self.gaadiya:
            i.goto(0,400)
        self.gaadiya = []
        self.raftaar += 5





