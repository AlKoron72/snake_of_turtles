from turtle import Turtle
SPEED = 20

class Paddle(Turtle):
    """
    Paddle class for Pong game.

    Args:
        turtle (_type_): _description_
    """
    def __init__(self, position: list[float]):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()  # Verhindert Linien
        self.speed("fastest")
        self.goto(position[0], position[1])  # Paddle an richtige Stelle setzen
        self.speed_value = SPEED  # nicht self.speed überschreiben!

    def move_up(self):
        if self.ycor() < 250:
            new_y = self.ycor() + self.speed_value
            self.goto(self.xcor(), new_y)

    def move_down(self):
        if self.ycor() > -240:
            new_y = self.ycor() - self.speed_value
            self.goto(self.xcor(), new_y)
        print(self)

    def __str__(self):
        return f"Paddle at {self.xcor()}, {self.ycor()}"

if __name__ == "__main__":
    my_paddle = Paddle([0, -0])
    print(my_paddle)
