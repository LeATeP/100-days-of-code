from turtle import Turtle

UP = 90
DOWN = 270
SPEED = 20


class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.speed("slow")
        self.goto(x, y)

    def go_up(self):
        new_y = self.ycor() + SPEED
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - SPEED
        self.goto(self.xcor(), new_y)
