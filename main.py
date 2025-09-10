import time
from turtle import Screen
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game ")
screen.bgcolor("black")
screen.tracer(0)

game_is_on = True

my_snake = Snake()

screen.listen()
screen.onkey(key="Up", fun=lambda: my_snake.turn("up"))
screen.onkey(key="Down", fun=lambda: my_snake.turn("down"))
screen.onkey(key="Left", fun=lambda: my_snake.turn("left"))
screen.onkey(key="Right", fun=lambda: my_snake.turn("right"))

segments = my_snake.segments

while game_is_on:
    screen.update()
    my_snake.move()
    time.sleep(0.1)

screen.exitonclick()

