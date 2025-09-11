from turtle import Turtle
import random

class Food:
    def pos_random20(self, field_size: int, segment_size: int) -> tuple[int, int]:
        """Generiert eine zufällige Position, die durch segment_size teilbar ist."""
        max_position = (field_size // 2) - segment_size  # Maximaler Abstand vom Mittelpunkt
        min_position = -max_position  # Minimaler Abstand vom Mittelpunkt

        # Zufällige x- und y-Koordinaten generieren, die durch segment_size teilbar sind
        x = random.randint(min_position // segment_size, max_position // segment_size) * segment_size
        y = random.randint(min_position // segment_size, max_position // segment_size) * segment_size
        return (x, y)
        
    def eat(self):
        """Aktualisiert die Position des Essens, wenn es "gegessen" wird."""
        self.pos = self.pos_random20(self.FIELD_SIZE, self.SEGMENT_SIZE)
        self.food.goto(self.pos)

    def __init__(self, SEGMENT_SIZE: int = 20, FIELD_SIZE: int = 600):
        self.SEGMENT_SIZE = SEGMENT_SIZE
        self.FIELD_SIZE = FIELD_SIZE
        self.food = Turtle("circle")
        self.food.penup()
        self.food.color("blue")
        self.pos = self.pos_random20(self.FIELD_SIZE, self.SEGMENT_SIZE)  # Initiale Position setzen
        self.food.goto(self.pos)

    def __str__(self):
        return f"Food ({self.pos})"

if __name__ == "__main__":
    my_food = Food()
    print(my_food)