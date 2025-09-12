from turtle import Turtle
FONT = ("Arial", 48, "bold")
ALIGN = "center"
COLOR = "white"

class Score(Turtle):
    def __init__(self, field_size: int = 600):
        super().__init__()
        self.SCREEN_SIZE = field_size
        self.score_left = 0
        self.score_right = 0
        self.hideturtle()
        self.penup()
        self.goto(0, field_size / 2 - FONT[1]*2)  # Position oben in der Mitte
        self.color(COLOR)
        self.write(f"{self}", align=ALIGN, font=FONT)
    
    def increase_score(self, player: str = "left"):
        self.clear()
        if player == "left":
            self.score_left += 1
        else:
            self.score_right += 1

        #score = f"{self.score_left} : {self.score_right}"
        self.write(f"{self}", align=ALIGN, font=FONT)
        print(self)
   
    def __str__(self):
        return f"{self.score_left} : {self.score_right}"

if __name__ == "__main__":
    my_score = Score()
    my_score.increase_score()
