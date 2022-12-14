from turtle import Turtle, Screen
import random

colours = ["red", "orange", "yellow", "green", "blue", "purple"]
ordinates = [-100, -60, -20, 20, 60, 100]
screen = Screen()
screen.setup(width=500, height=400)
prediction = screen.textinput(title="Make your bet", prompt="Which turtle will win the game? Type the colour")
sara_kachua = []


for i in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(colours[i])
    tim.penup()
    tim.goto(x=-230, y=ordinates[i])
    sara_kachua.append(tim)

if prediction in colours:
    not_game_over = True
else:
    print("You had entered wrong command. Please try again")
while not_game_over:
    for i in range(0, 6):
        kachua = sara_kachua[i]
        distance = random.randint(0, 10)
        kachua.forward(distance)
        if kachua.xcor() > 200:

            if kachua.pencolor() == prediction:
                print(f"Party doh, Aap jit chuke hai")
            else:
                print("Maaf karia aap har gae hai")
            print(f"Jitne wala kachua {kachua.pencolor()} hai")
            not_game_over = False


screen.exitonclick()



























# tim = Turtle(shape="turtle")
# tom = Turtle(shape="turtle")
# tommy = Turtle(shape="turtle")
# timmy = Turtle(shape="turtle")
# m = Turtle(shape="turtle")
# t = Turtle(shape="turtle")
#
# tim.color(colours[0])
# tom.color(colours[1])
# tommy.color(colours[2])
# timmy.color(colours[3])
# m.color(colours[4])
# t.color(colours[5])
#
#
# def move_tim():
#     tim.forward(random.randint(1, 4))
#     return tim.position
#
#
# def move_tom():
#     tom.forward(random.randint(1, 4))
#     # print((tom.position)
#     return tom.position
#
#
# def move_tommy():
#     tommy.forward(random.randint(1, 4))
#     return tommy.position
#
#
# def move_timmy():
#     timmy.forward(random.randint(1, 4))
#     return timmy.position
#
#
# def move_m():
#     m.forward(random.randint(1, 4))
#     return m.position
#
#
# def move_t():
#     t.forward(random.randint(1, 4))
#     return t.position
#
#
# tim.penup()
# tom.penup()
# tommy.penup()
# timmy.penup()
# m.penup()
# t.penup()
# tim.goto(-230, -100)
# tom.goto(-230, -60)
# tommy.goto(-230, -20)
# timmy.goto(-230, 20)
# m.goto(-230, 60)
# t.goto(-230, 100)
#
# game_over = True
# winner = ""
#
# while game_over:
#     print(game_over)
#     tim_pos = move_tim()
#     print(tim_pos)
#     tom_pos = move_tom()
#     tommy_pos = move_tommy()
#     timmy_pos = move_timmy()
#     m_pos = move_m()
#     t_pos = move_t()
#
#     if tim_pos == (230, -100):
#         game_over = False
#         winner = f"{colours[0]} turtle"
#
#     elif tom_pos == (230, -60):
#         game_over = False
#         winner = f"{colours[1]} turtle"
#
#     elif tommy_pos == (230, -20):
#         game_over = False
#         winner = f"{colours[2]} turtle"
#
#     elif timmy_pos == (230, 40):
#         game_over = False
#         winner = f"{colours[3]} turtle"
#
#     elif m_pos == (230, 60):
#         game_over = False
#         winner = f"{colours[4]} turtle"
#
#     elif t_pos == (230, 100):
#         game_over = False
#         winner = f"{colours[5]} turtle"
#
