from turtle import Turtle
START_LENGTH = 3

class Snake:
    def __init__(self, MOVE_DISTANCE: int = 2, FIELD_SIZE: int = 600, WALL_COLLISION: bool = True):
        self.MOVE_DISTANCE = MOVE_DISTANCE
        self.FIELD_SIZE = FIELD_SIZE
        self.WALL_COLLISION = WALL_COLLISION
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in range(START_LENGTH):
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(x=-self.MOVE_DISTANCE * i, y=0)
            self.segments.append(new_segment)

    def move(self) -> tuple[int, int]:
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(self.MOVE_DISTANCE)
        
        # Check for collision with walls or self
        if self.detect_collision(self.FIELD_SIZE, self.WALL_COLLISION):
            raise Exception("Game Over: Collision detected!")
        
        return self.head.position()

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
            
    def detect_collision(self, FIELD_SIZE: int, WALL_COllISSION: bool = True) -> bool:
        x, y = self.head.position()
        half_field = FIELD_SIZE / 2
        if WALL_COllISSION:
            if x < -half_field or x > half_field or y < -half_field or y > half_field:
                return True
            else:
                if x < -half_field:
                    self.head.setx(half_field)
                elif x > half_field:
                    self.head.setx(-half_field)
                if y < -half_field:
                    self.head.sety(half_field)
                elif y > half_field:
                    self.head.sety(-half_field)
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 10:
                return True
        return False

    def __str__(self):
        return f"Snake with {len(self.segments)} segments\nHead at {self.head.position()}"

if __name__ == "__main__":
    my_snake = Snake()
    print(my_snake)
