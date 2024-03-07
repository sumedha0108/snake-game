from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('highscore.txt') as file:
            self.high_sc = int(file.read())
        self.goto(0, 270)
        self.color("white")
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score = {self.score}  High Score = {self.high_sc}", align="center", font=("Arial", 24, "normal"))

    def reset_score(self):
        if self.score > self.high_sc:
            self.high_sc = self.score
            with open('highscore.txt', mode='w') as file:
                file.write(str(self.high_sc))
        self.score = 0
        self.update()

    def inc_score(self):
        self.score += 1
        self.update()

