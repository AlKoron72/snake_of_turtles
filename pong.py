import time
from turtle import Screen, Turtle
from paddle import Paddle
from score_pong import Score
from ball import Ball

FIELD_SIZE = [800, 600]
game_is_on = True

screen = Screen()
screen.setup(width=FIELD_SIZE[0], height=FIELD_SIZE[1])
screen.bgcolor("black")
screen.title("Pong Game")
#screen.tracer(0)

left_paddle = Paddle([-350, 0])
right_paddle = Paddle([350, 0])
scoreboard = Score()
ball = Ball()

screen.listen()
screen.onkey(right_paddle.move_up, key="Up")
screen.onkey(right_paddle.move_down, key="Down")
screen.onkey(left_paddle.move_up, key="w")
screen.onkey(left_paddle.move_down, key="s")

while game_is_on:
    screen.update()
    time.sleep(0.01)
    ball.move()
    
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.reset_position()
        if ball.xcor() > 0:
            scoreboard.l_point()
        else:
            scoreboard.r_point()

screen.exitonclick()
