from turtle import Screen
from dandah import Dandah
from gilli import Gilli
import time as t
from points import Points
from daayara import Daayara

screen = Screen()
screen.setup(width=650, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

dandah = Dandah()
gilli = Gilli()
points = Points()
daayara = Daayara()

screen.update()

screen.listen()
screen.onkey(dandah.dandah1_uppar, "w")
screen.onkey(dandah.dandah1_niche, "s")
screen.onkey(dandah.dandah2_uppar, "Up")
screen.onkey(dandah.dandah2_niche, "Down")

khel_chalu = True
while khel_chalu:
    t.sleep(gilli.raftaar)
    screen.update()
    gilli.gilli_hiil()

    gilli_ycor = gilli.ycor()
    gilli_xcor = gilli.xcor()

    if gilli_ycor > 275 or gilli_ycor < -275:
        gilli.kud_y()
    if dandah.dandah[1].distance(gilli) < 45 and gilli_xcor > 255 or dandah.dandah[0].distance(gilli) < 45 and gilli_xcor < -255:
        gilli.kud_x()
    if gilli_xcor > 280:
        gilli.chuot_gaya()
        points.l_ginoh()
    if gilli_xcor < -280:
        gilli.chuot_gaya()
        points.r_ginoh()
    # x = 1
    # elif gilli_xcor > 250 or gilli_xcor < -250 and x == 1:
        # x = 0

screen.exitonclick()
