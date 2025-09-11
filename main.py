import time
from turtle import Screen
from snake import Snake
from food import Food
from score import Score

SEGMENT_SIZE = 20
FIELD_SIZE = SEGMENT_SIZE * 30

screen = Screen()
screen.setup(width=FIELD_SIZE, height=FIELD_SIZE)
screen.title("Snake Game ")
screen.bgcolor("black")
screen.tracer(0)

game_is_on = True

my_snake = Snake(SEGMENT_SIZE)
my_food = Food(SEGMENT_SIZE=SEGMENT_SIZE, FIELD_SIZE=FIELD_SIZE)
my_score = Score(SCREEN_SIZE=FIELD_SIZE)

screen.listen()
screen.onkey(key="Up", fun=lambda: my_snake.turn("up"))
screen.onkey(key="Down", fun=lambda: my_snake.turn("down"))
screen.onkey(key="Left", fun=lambda: my_snake.turn("left"))
screen.onkey(key="Right", fun=lambda: my_snake.turn("right"))

segments = my_snake.segments

while game_is_on:
    screen.update()
    snake_head_pos = my_snake.move()
    
    if my_snake.head.distance(my_food) < 15: # distance is a method of Turtle class
        # snake_head_pos hits food_pos in distance < 15
        my_food.eat()
        my_snake.grow()
        my_score.increase_score()
    
    time.sleep(0.08)

screen.exitonclick()

