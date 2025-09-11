from turtle import Turtle
FONT = ("Arial", 24, "bold")
ALIGN = "center"

class Score(Turtle):
    def __init__(self, field_size: int = 600):
        super().__init__()
        self.SCREEN_SIZE = field_size
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, field_size / 2 - 40)  # Position oben in der Mitte
        self.color("red")
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)
    
    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "bold"))
        print(self)
   
    def __str__(self):
        return f"Score: {self.score}"

if __name__ == "__main__":
    my_score = Score()
    my_score.increase_score()
