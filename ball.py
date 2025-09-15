from turtle import Turtle
BALL_SPEED = 2

class Ball(Turtle):
    """
    Ball class for Pong game.

    Args:
        Turtle (_type_): _description_
    """
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.dx = 2
        self.dy = 2
        
    def move(self) -> None:
        new_x = self.xcor() + BALL_SPEED * self.dx
        new_y = self.ycor() + BALL_SPEED * self.dy
        self.goto(new_x, new_y)
        
    def reset_position(self) -> None:
        self.goto(0, 0)
        self.dx *= -1  # Change direction after scoring
    
    def collide_with_paddle(self, left_paddle, right_paddle) -> None:
        if (self.distance(left_paddle) < 50 and self.xcor() < -320) or (self.distance(right_paddle) < 50 and self.xcor() > 320):
            self.dx *= -1  # Reverse direction on paddle collision
        
    def collide_with_wall(self) -> None:
        if self.ycor() > 290 or self.ycor() < -290:
            self.dy *= -1  # Reverse vertical direction on wall collision
        
    def collission_handling(self, left_paddle, right_paddle) -> None:
        self.collide_with_wall()
        self.collide_with_paddle(left_paddle, right_paddle)
            
    def __str__(self) -> str:
        return f"Ball at ({self.xcor()}, {self.ycor()})"  
    
if __name__ == "__main__":
    ball = Ball()
    print(ball)