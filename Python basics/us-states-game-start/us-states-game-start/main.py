from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title("Nacho USA")
screen.setup(width=725, height=491)
image = "blank_states_img.gif"
screen.addshape(image)

turtle = Turtle(image)
turtle2 = Turtle()
turtle2.hideturtle()
turtle2.penup()

csv_data = pandas.read_csv("50_states.csv")

states = csv_data["state"].to_list()

# print(len(states))
# print(states)

score = 0

done_states = []

not_done = {
    "state": []
}

khel_chalu = True
while khel_chalu:
    guess = screen.textinput(title=f"{score}/ guess the rajya", prompt="Rajya Batao").title()

    if guess == "Exit":
        break

    for rajya in states:
        if rajya == guess:
            if guess in done_states:
                pass
            else:
                abscissa = csv_data[csv_data.state == guess].x.to_list()
                ordinate = csv_data[csv_data.state == guess].y.to_list()
                # print(type(abscissa[0]))
                turtle2.goto(abscissa[0], ordinate[0])
                turtle2.write(arg=guess, font=("Arial", 8, "normal"))
                score += 1
                done_states.append(guess)
        if score == 50:
            khel_chalu = False

# for i in states:
#     if i in done_states:
#         pass
#     else:
not_done["state"] = [i for i in states if i not in done_states]

print(not_done)

data = pandas.DataFrame(not_done)
data.to_csv("bhul_gaya_jo.csv")


