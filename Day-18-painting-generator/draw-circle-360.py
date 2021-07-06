import random
import turtle

q = turtle.Turtle()
q.speed(0)
turtle.colormode(255)


def change_color():
    r = random.randrange(0, 255)
    b = random.randrange(0, 255)
    g = random.randrange(0, 255)

    q.pencolor(r, g, b)


direction = 1
total_circle = 0


while total_circle <= 360:
    change_color()
    q.circle(100)
    q.left(direction)
    total_circle += direction





screen = turtle.Screen()
screen.exitonclick()
