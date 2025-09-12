from turtle import Screen, Turtle
from paddle import Paddle
from score_pong import Score

FIELD_SIZE = [800, 600]


screen = Screen()
screen.setup(width=FIELD_SIZE[0], height=FIELD_SIZE[1])
screen.bgcolor("black")
screen.title("Pong Game")
#screen.tracer(0)

left_paddle = Paddle([-350, 0])
right_paddle = Paddle([350, 0])
scoreboard = Score()

screen.listen()
screen.onkey(right_paddle.move_up, key="Up")
screen.onkey(right_paddle.move_down, key="Down")
screen.onkey(left_paddle.move_up, key="w")
screen.onkey(left_paddle.move_down, key="s")

screen.exitonclick()
