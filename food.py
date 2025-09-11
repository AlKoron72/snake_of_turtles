from turtle import Turtle
import random

class Food:
    def pos_random20(self) -> tuple[int, int]:
        """Generiert eine zufällige Position, die durch segment_size teilbar ist."""
        max_position = (self.FIELD_SIZE // 2) - self.SEGMENT_SIZE  # Maximaler Abstand vom Mittelpunkt
        min_position = -max_position  # Minimaler Abstand vom Mittelpunkt

        # Zufällige x- und y-Koordinaten generieren, die durch segment_size teilbar sind
        x = random.randint(min_position // self.SEGMENT_SIZE, max_position // self.SEGMENT_SIZE) * self.SEGMENT_SIZE
        y = random.randint(min_position // self.SEGMENT_SIZE, max_position // self.SEGMENT_SIZE) * self.SEGMENT_SIZE
        return (x, y)
        
    def eat(self):
        """Aktualisiert die Position des Essens, wenn es "gegessen" wird."""
        print(f"Food eaten ({self.pos})!")
        self.pos = self.pos_random20()
        self.food.goto(self.pos)

    def __init__(self, SEGMENT_SIZE: int = 20, FIELD_SIZE: int = 600):
        self.SEGMENT_SIZE = SEGMENT_SIZE
        self.FIELD_SIZE = FIELD_SIZE
        self.food = Turtle("circle")
        self.food.penup()
        self.food.color("blue")
        self.pos = self.pos_random20()  # Initiale Position setzen
        self.food.goto(self.pos)

    def __str__(self):
        return f"Food ({self.pos})"

if __name__ == "__main__":
    my_food = Food()
    print(my_food)