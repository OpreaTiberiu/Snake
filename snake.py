from turtle import Turtle


def int_sign(x):
    if x == 0:
        return 0
    else:
        return x / abs(x)


class Snake:
    __START_POS = [(40, 0), (20, 0), (0, 0)]
    __DISTANCE = 20

    def __init__(self, screen_x, screen_y, offset):
        self.max_screen_x = screen_x / 2 - offset / 2
        self.max_screen_y = screen_y / 2 - offset / 2
        self.segments = []
        for pos in self.__START_POS:
            self.add_seg(pos)
        self.head = self.segments[0]

    def add_seg(self, pos=None):
        seg = Turtle("square")
        seg.color("white")
        seg.penup()
        if pos is not None:
            seg.goto(pos)
        elif len(self.segments) > 1:
            seg.goto(self.segments[-1].xcor(), self.segments[-1].ycor())
        self.segments.append(seg)

    def move_snake(self):
        for index in range(len(self.segments) - 1, 0, -1):
            self.segments[index].goto(self.segments[index - 1].xcor(), self.segments[index - 1].ycor())
        self.head.forward(self.__DISTANCE)

        # If the snake reaches end of screen move it to the other side
        if self.head.xcor() > self.max_screen_x or self.head.xcor() < -self.max_screen_x:
            new_x = -1 * int_sign(self.head.xcor()) * (self.max_screen_x - (abs(self.head.xcor()) - self.max_screen_x))
            self.head.goto(new_x, self.head.ycor())

        if self.head.ycor() > self.max_screen_y or self.head.ycor() < -self.max_screen_y:
            new_y = -1 * int_sign(self.head.ycor()) * (self.max_screen_y - (abs(self.head.ycor()) - self.max_screen_y))
            self.head.goto(self.head.xcor(), new_y)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def distance(self, screen_object):
        return self.head.distance(screen_object)

    def check_collision(self):
        return len([seg for seg in self.segments[1:] if self.head.distance(seg) <= 10]) != 0
