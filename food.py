from turtle import Turtle

class Food:
    def __init__(self):
        food = Turtle("circle")

    def __str__(self):
        print("Food")

if __name__ == "__main__":
    my_food = Food()
    print(my_food)