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
screen.tracer(0)

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
    time.sleep(0.04)
    ball.move()
    ball.collission_handling(left_paddle, right_paddle)
    
    if ball.xcor() > 380 or ball.xcor() < -380:
        if ball.xcor() > 0:
            scoreboard.increase_score("left")
        else:
            scoreboard.increase_score("right")
        ball.reset_position()

screen.exitonclick()
