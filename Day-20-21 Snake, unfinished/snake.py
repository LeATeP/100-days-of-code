from turtle import Turtle

positions = [(0, 0), (-20, 0), (-40, 0)]
X = positions
SPEED = 10


class Snake:

    def __init__(self):
        self.position = []
        self.cubes = []
        self.create_snake()

    def create_snake(self):
        for pos in X:
            cube = Turtle("square")
            cube.penup()
            cube.color("white")
            cube.speed("slow")
            cube.goto(pos)
            self.cubes.append(cube)

    def move(self):
        for cub in range(len(self.cubes) - 1, 0, -1):
            new_x = self.cubes[cub - 1].xcor()
            new_y = self.cubes[cub - 1].ycor()
            self.cubes[cub].goto(new_x, new_y)
        self.cubes[0].forward(SPEED)

    def moving_right(self):
        if self.cubes[0].heading() != 180:
            self.cubes[0].setheading(0)

    def moving_left(self):
        if self.cubes[0].heading() != 0:
            self.cubes[0].setheading(180)

    def moving_up(self):
        if self.cubes[0].heading() != 270:
            self.cubes[0].setheading(90)

    def moving_down(self):
        if self.cubes[0].heading() != 90:
            self.cubes[0].setheading(270)
