from turtle import Turtle



position = [(-280, 0), (280, 0)]
# position1 = [(-350, 0), (-350, 20), (-350, 40), (-350, -20), (-350, -40)]
# position2 = [(350, 0), (350, -20), (350, -40), (350, 20),  (350, 40)]

class Dandah(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        # screen.tracer(0)
        self.dandah = []
        # self.dandah2 = []
        self.dandah_banao()
        # screen.update()
        # self.dandah_banao2()



    def dandah_banao(self):
        for i in position:
            dandah_ka_tukdah = Turtle(shape="square")
            dandah_ka_tukdah.penup()
            dandah_ka_tukdah.color("white")
            dandah_ka_tukdah.shapesize(stretch_len=1, stretch_wid=5)
            # dandah_ka_tukdah.speed("fastest")
            dandah_ka_tukdah.goto(i)
            self.dandah.append(dandah_ka_tukdah)

    def dandah1_uppar(self):
        xcor = self.dandah[0].xcor()
        ycor = self.dandah[0].ycor()
        # xcor = position[0][0]
        # ycor = position[0][1]
        ycor += 20
        self.dandah[0].goto(xcor, ycor)

    def dandah1_niche(self):
        xcor = self.dandah[0].xcor()
        ycor = self.dandah[0].ycor()
        # xcor = position[0][0]
        # ycor = position[0][1]
        # # if xcor > -230:
        ycor -= 20
        self.dandah[0].goto(xcor, ycor)

    def dandah2_uppar(self):
        xcor = self.dandah[1].xcor()
        ycor = self.dandah[1].ycor()
        # xcor = position[1][0]
        # ycor = position[1][1]
        # if xcor < 230:
        ycor += 20
        self.dandah[1].goto(xcor, ycor)

    def dandah2_niche(self):
        ycor = self.dandah[1].ycor()
        xcor = self.dandah[1].xcor()
        # ycor = position[1][1]
        # if xcor > -230:
        ycor -= 20
        self.dandah[1].goto(xcor, ycor)

    # def dandah_banao2(self):
    #     for i in position2:
    #         dandah_ka_tukdah2 = Turtle(shape="square")
    #         dandah_ka_tukdah2.penup()
    #         dandah_ka_tukdah2.speed("fastest")
    #         dandah_ka_tukdah2.goto(i)
    #         dandah_ka_tukdah2.shapesize(1)
    #         self.dandah2.append(dandah_ka_tukdah2)
#




# a = Dandah()
