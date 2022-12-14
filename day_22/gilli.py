from turtle import Turtle
import random as r

class Gilli(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        # self.shapesize(stretch_wid=20, stretch_len=20)
        self.penup()
        self.xcor_kadam = 10
        self.ycor_kadam = 20
        self.raftaar = 0.1

    def gilli_hiil(self):
        xcor = self.xcor() + self.xcor_kadam
        ycor = self.ycor() + self.ycor_kadam
        self.goto(xcor, ycor)

    def kud_y(self):
        self.ycor_kadam *= -1

    def kud_x(self):
        self.xcor_kadam *= -1
        self.raftaar *= 0.9

    def chuot_gaya(self):
        self.raftaar = 0.1
        self.goto(0,0)
        self.xcor_kadam *= -1
        self.ycor_kadam *= -1
