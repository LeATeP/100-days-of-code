from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.speed(0)
        self.shapesize(stretch_wid=0.5, stretch_len=0.5, outline=10)
        self.color("red")
        self.shape("circle")
        x, y = random.randint(-270, 270), random.randint(-270, 270)
        self.goto(x, y)

    def reposition(self):
        x, y = random.randint(-270, 270), random.randint(-270, 270)
        self.goto(x, y)