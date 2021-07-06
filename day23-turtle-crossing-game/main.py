import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
score = Scoreboard()

unit = CarManager()

screen.onkey(key="Up", fun=player.move_up)

STARTING_POSITION = (0, -280)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    number = random.randint(0, 2)
    if number == 0:
        unit.create_car()

    unit.list_move()
    score.show_score(unit.level)

    for uni in unit.car_list:
        if player.distance(uni) < 18:
            score.game_over()
            game_is_on = False
            print("Game over")

    if player.ycor() > 280:
        unit.level += 1
        unit.reset()
        player.goto(STARTING_POSITION)







