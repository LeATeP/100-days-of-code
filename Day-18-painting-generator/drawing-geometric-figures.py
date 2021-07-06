from turtle import Turtle, Screen, colormode
import random


timmy_the_turtle = Turtle()
q1 = timmy_the_turtle
q1.shape("turtle")
colormode(255)

angels = 3
loops = 20


def change_color():
    r = random.randrange(0, 255)
    b = random.randrange(0, 255)
    g = random.randrange(0, 255)

    q1.pencolor(r, g, b)


def move_turn_left(angle):
    q1.forward(100)
    q1.right(angle)


while loops > 0:
    change_color()

    for move in range(angels):
        left_move = 360 / angels

        move_turn_left(left_move)

    angels += 1
    loops -= 1


screen = Screen()
screen.exitonclick()
