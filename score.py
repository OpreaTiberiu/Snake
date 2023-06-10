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
        self.update()
        self.hideturtle()

    def update(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}",
                   font=("Arial", 30, "normal"),
                   align="center")

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER",
                   font=("Arial", 30, "normal"),
                   align="center")
