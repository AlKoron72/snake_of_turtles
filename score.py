from turtle import Turtle

FONT = ("Arial", 24, "bold")
ALIGN = "center"
PATH_HIGH_SCORE = "snake/data.txt"

class Score(Turtle):
    """ Score class to display and manage the score. """

    def __init__(self, field_size: int = 600):
        super().__init__()
        self.SCREEN_SIZE = field_size
        # keeping score and highscore
        self.score = 0
        self.hight_score = self.read_high_score()
        # move turtle to position
        self.hideturtle()
        self.penup()
        self.goto(0, field_size / 2 - 40)  # Position oben in der Mitte
        self.color("red")
        # update display of scores
        self.update_score_display()

    def update_score_display(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.hight_score}", align=ALIGN, font=FONT)
    
    def read_high_score(self) -> int:
        try:
            with open(PATH_HIGH_SCORE, "r") as file:
                content = file.read().strip()  # Dateiinhalt lesen und Leerzeichen entfernen
                print("High Score loaded:", content)
                return int(content) if content else 0  # Sicherstellen, dass der Inhalt nicht leer ist
        except FileNotFoundError:
            return 0
    
    def write_high_score(self):
        with open(PATH_HIGH_SCORE, "w") as file:
            file.write(str(self.hight_score))
            
    def increase_score(self):
        self.score += 1
        self.update_score_display()
        if self.score > self.hight_score:
            self.hight_score = self.score
            self.update_score_display()
            self.write_high_score()
        print(self)
   
    def __str__(self):
        return f"Score: {self.score} | High Score: {self.hight_score}"
    
if __name__ == "__main__":
    my_score = Score()
    my_score.increase_score()
