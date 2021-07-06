from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    
    def __init__(self):
        self.car_list = []
        self.level = 1

    def create_car(self):
        self.car = Turtle()
        self.car.penup()
        self.car.shape("square")
        self.car.shapesize(stretch_wid=1, stretch_len=2)
        self.car.color(random.choice(COLORS))
        self.car.goto(315, random.randint(-260, 300))
        self.car.setheading(180)
        self.car_list.append(self.car)

    def list_move(self):
        for item in range(len(self.car_list)):
            self.car_list[item].forward(STARTING_MOVE_DISTANCE * self.level)

    def reset(self):
        for car in range(len(self.car_list)):
            self.car_list[car].reset()
        self.car_list = []

        