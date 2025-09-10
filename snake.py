from turtle import Turtle
MOVE_DISTANCE = 20
START_LENGTH = 5

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in range(START_LENGTH):
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(x=-20 * i, y=0)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def grow(self):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(self.segments[-1].position())
        self.segments.append(new_segment)

    def turn(self, direction):
        if direction == "up" and self.head.heading() != 270:
            self.head.setheading(90)
        elif direction == "down" and self.head.heading() != 90:
            self.head.setheading(270)
        elif direction == "left" and self.head.heading() != 0:
            self.head.setheading(180)
        elif direction == "right" and self.head.heading() != 180:
            self.head.setheading(0)

    def __str__(self):
        return f"Snake with {len(self.segments)} segments\nHead at {self.head.position()}"

if __name__ == "__main__":
    my_snake = Snake()
    print(my_snake)
