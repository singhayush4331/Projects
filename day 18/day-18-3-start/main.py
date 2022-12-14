import turtle as t
from random import randint
tim = t.Turtle()

########### Challenge 3 - Draw Shapes ########

colors = ["#0000FF", "#000000", "#00008B", "#FF4040", "#7FFF00", "#FF00FF"]
sides = 3
total_angle = 360
while True:
    angle = total_angle/sides
    tim.color(colors[randint(0, 5)])
    for i in range(sides):
        tim.forward(100)
        tim.right(angle)
    sides += 1

