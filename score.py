from turtle import Turtle
import random


class Score(Turtle):
    def __init__(self, screen_y):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, (screen_y / 2) - screen_y / 20)
        self.pencolor("white")
        self.show_score()
        self.hideturtle()

    def update(self):
        self.score += 1
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f"Score: {self.score}",
                   font=("Arial", 30, "normal"),
                   align="center")

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER",
                   font=("Arial", 30, "normal"),
                   align="center")
