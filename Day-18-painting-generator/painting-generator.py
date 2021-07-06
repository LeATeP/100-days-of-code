import random
import turtle


q = turtle.Turtle()
q.speed(0)
turtle.colormode(255)
q.penup()
q.hideturtle()


dots_size = 20
space_between = 50
board_size = (10, 10)


colors1 = [[245, 243, 238], [246, 242, 244],
           [202, 164, 110], [240, 245, 241],
           [236, 239, 243], [149, 75, 50],
           [222, 201, 136], [53, 93, 123],
           [170, 154, 41], [138, 31, 20]]


def moving_dot(size=dots_size, color=colors1):
    x = random.choice(color)
    q.pencolor(x)

    q.dot(size)
    q.forward(50)


y = 0

for step in range(10):
    for move in range(10):
        moving_dot()

    y += 50
    q.sety(y)
    q.setx(0)


screen = turtle.Screen()
screen.exitonclick()
