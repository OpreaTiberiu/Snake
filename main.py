from turtle import Screen
from snake import Snake
from food import Food
from score import Score

import time

SCREEN_X = 1600
SCREEN_Y = 1200
OFFSET = 100

s = Screen()
s.setup(SCREEN_X, SCREEN_Y)
s.bgcolor("black")
s.title("My Snake game")
s.tracer(0)

snake = Snake(SCREEN_X, SCREEN_Y, OFFSET)

food = Food(SCREEN_X, SCREEN_Y, OFFSET)

score = Score(SCREEN_Y)

s.listen()
s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")
s.onkey(snake.left, "Left")
s.onkey(snake.right, "Right")

print(snake.segments[1:])

game_on = True
while game_on:
    s.update()
    time.sleep(0.1)
    snake.move_snake()
    if snake.distance(food) < 18:
        food.refresh()
        snake.add_seg()
        score.update()
    if snake.check_collision():
        game_on = False

score.game_over()
s.exitonclick()
