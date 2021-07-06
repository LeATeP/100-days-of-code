from turtle import Turtle

ANGEL = 45
BASE = 360
SPEED = 20
w = 360


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=1.5, stretch_len=1.5)
        self.x_move = 10
        self.y_move = 10

    def move(self, ):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def ped_bounce(self):
        pass


