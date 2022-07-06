from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time
screen = Screen()
screen.setup(width=800, height=600)
screen.title("My Pong Game")
screen.bgcolor("black")
#Whenever we use tracer() we must use update() in while loop so that it updates the screen every single time
screen.tracer(0)
left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()
score = ScoreBoard()

screen.listen()
screen.onkey(key="Up", fun=right_paddle.move_up)
screen.onkey(key="Down", fun=right_paddle.move_down)
screen.onkey(key="w", fun=left_paddle.move_up)
screen.onkey(key="s", fun=left_paddle.move_down)
game_is_on = True
counter = 0
while game_is_on:
    """
    Now what we are expecting is to change the speed of the ball everytime when it hits the paddle so in order to
    achieve this we will take the help of sleep() so initially we pass 0.1 then if we pass 0.01 then it will again 
    become much fastest then 0.001 is again much fastest. So at each step when the ball hits the paddle we multiply
    the move_speed by 0.9 and whenever the game will restart we will again set the move_speed to 0.1 in reset_position()
    So that we again start with 0.1 speed 
    """
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    #Detect collision with wall in vertical mode
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with paddle in horizontal mode
    """
    The way to detect collision with simple as we used to do it i.e. with the help of distance().Now the problem is the
    size of the paddle is 100 in length and the distance() calculates distance from centre of the objects. So writing 
    only distance() condition will not work in cases like when it hit at the edge of the paddle. So we will set some
    boundary condition i.e. if the distance is less than 50 and the xcor() is within the ball set-up range then it will
    be considered as collision with paddle no matter where the ball hit the paddle.Same for the left paddle also.
    """
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        #We will negate x direction as negating x coordinate will land in somehow third quadrant and then again hitting
        #the wall will negate y direction will make the ball jump in the somewhere 1st quadrant
        ball.bounce_x()

    """
    Basically the rule of the game is that when the right paddle misses the ball the left side gamer will get score
    similarly when the left paddle misses the ball then the right side gamer will get a score
    """
    #Detect right paddle misses the ball
    if ball.xcor() > 370:
        counter += 1
        ball.reset_position()
        score.left_point()

    #Detect left paddle misses the ball
    if ball.xcor() < -370:
        counter += 1
        ball.reset_position()
        score.right_point()

    #If total 10 rounds take place the game should end here round means whenever the gamer from each side will score.
    if counter == 10:
        game_is_on = False


screen.exitonclick()
