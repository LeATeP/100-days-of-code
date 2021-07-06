import turtle
import random


q1 = turtle.Turtle()
turtle.colormode(255)
q1.pensize(10)
q1.speed("fastest")
q1.shape("turtle")
turtle.colormode(255)

steps = 30


def change_color():
    r = random.randrange(0, 255)
    b = random.randrange(0, 255)
    g = random.randrange(0, 255)

    q1.pencolor(r, g, b)


def pool_of_movement(step):
    direction = [0, 90, 180, 270]
    choice = random.choice(direction)
    q1.forward(step)
    q1.left(choice)


for step in range(10000):
    change_color()
    pool_of_movement(steps)


screen = turtle.Screen()
