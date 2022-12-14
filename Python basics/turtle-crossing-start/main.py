import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

kachua = Player()
gaadiya = CarManager()
scoreboard = Scoreboard()


def agla_level():
    kachua.waapsi()
    gaadiya.speed_badhao()
    scoreboard.score_ginoh()

screen.listen()
screen.onkey(fun=kachua.upper_jao, key="w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    gaadiya.gaadi_aao()
    gaadiya.gaadi_aage_aao()
    for i in gaadiya.gaadiya:
        g_xcor = i.xcor()
        g_ycor = i.ycor()

        if kachua.kachua.distance(i) < 20:
            game_is_on = False
            scoreboard.score_reset()

    if kachua.kachua.ycor() > 280:
        agla_level()


screen.exitonclick()
