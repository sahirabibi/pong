# create two scoreboards to keep track of points
from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.setposition(position)
        self.score = 0
        self.write(f"{self.score}", align="center", font=("Courier", 80, "normal"))

    def point(self):
        self.clear()
        self.score += 1
        self.write(f"{self.score}", align="center", font=("Courier", 80, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", move=False, align="center", font=("Courier", 40, "normal"))