from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self, screen_x, screen_y, offset):
        super().__init__()
        self.max_screen_x = int(screen_x / 2) - offset
        self.max_screen_y = int(screen_y / 2) - offset
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x_pos = random.choice(range(-self.max_screen_x, self.max_screen_x, 20))
        y_pos = random.choice(range(-self.max_screen_y, self.max_screen_y, 20))
        self.goto(x_pos, y_pos)
