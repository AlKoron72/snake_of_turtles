class Score:
    def __init__(self):
        self.score = 0
    def increase_score(self):
        self.score += 1
    def get_score(self):
        return self.score
    def __str__(self):
        return f"Score: {self.score}"

if __name__ == "__main__":
    my_score = Score()
    print(my_score)