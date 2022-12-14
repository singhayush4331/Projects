import turtle as t

tim = t.Turtle()

########### Challenge 2 - Draw a Dashed Line ########

for i in range(20):
    tim.penup()
    tim.forward(5)
    tim.pendown()
    tim.forward(5)

