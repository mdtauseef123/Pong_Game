from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        self.move()

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)

    def bounce_y(self):
        """
        To move in the upward/downward direction as we only negate the y_move value and value of x remain changing as it
        is as we only have to move in left/right direction and that is done with the help of line 17 easily.
        """
        self.y_move *= -1

    def bounce_x(self):
        """
        To move in the left/right direction as we only negate the x_move value and value of y remain changing as it
        is as we only have to move in up/down direction and that is done with the help of line 18 easily.
        """
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        """
        The rule of the game is that whenever a paddle misses the ball then we have to start from origin point and the
        ball will move in the opposite player.
        So firstly we will go to the origin point, and then we reverse our x-direction by executing bounce_x().
        The functionality of bounce_x() remains same as it did when we hit the paddle.
        """
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
