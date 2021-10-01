from turtle import Turtle, Screen
import random

turtle = Turtle()

num_sides = 5

colours = ["CornFlowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]


def draw_shapes(num_sides):
    for _ in range(num_sides):
        angle = 360 / num_sides

        turtle.forward(100)
        turtle.right(angle)


for shape_side_n in range(3, 11):
    turtle.color(random.choice(colours))
    draw_shapes(shape_side_n)

screen = Screen()
screen.exitonclick()
