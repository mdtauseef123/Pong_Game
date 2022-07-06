from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        # As we want the size of the paddle to be 20x100, so we stretch the width by 5 times and leave the length as
        # it is i.e.20 Default size of square is 20x20
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(coordinates)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
