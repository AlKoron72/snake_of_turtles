import time
from screen_config import setup_screen
from snake import Snake
from snake.food import Food
from score import Score

SEGMENT_SIZE = 20
FIELD_SIZE = SEGMENT_SIZE * 30 + SEGMENT_SIZE
WALL_COLLISION = True

# Snake-Objekt initialisieren
my_snake = Snake(SEGMENT_SIZE, FIELD_SIZE, WALL_COLLISION)

# Bildschirm und Steuerung einrichten
screen = setup_screen(FIELD_SIZE, turn_callback=my_snake.turn)

# Andere Objekte initialisieren
my_food = Food(segment_size=SEGMENT_SIZE, field_size=FIELD_SIZE)
my_score = Score(field_size=FIELD_SIZE)


# Spielschleife
game_is_on = True
while game_is_on:
    screen.update()
    try:
        snake_head_pos = my_snake.move()
    except Exception as e:
        print(e)
        game_is_on = False
        my_score.goto(0, 0)
        my_score.clear()
        my_score.write(f"GAME OVER\n  ({my_score})", align="center", font=("Arial", 24, "bold"))
        break
    
    if my_snake.head.distance(my_food) < 15:  # distance is a method of Turtle class
        my_food.eat()
        my_snake.grow()
        my_score.increase_score()
    
    time.sleep(0.1)

screen.exitonclick()