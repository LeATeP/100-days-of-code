from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Shake Game")
screen.tracer(0)


snake = Snake()
food = Food()
display_score = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.moving_up)
screen.onkey(key="Down", fun=snake.moving_down)
screen.onkey(key="Right", fun=snake.moving_right)
screen.onkey(key="Left", fun=snake.moving_left)


score = 0
game_is_on = True
while game_is_on:
    food_active = True
    screen.update()
    time.sleep(0.05)

    snake.move()

    if snake.cubes[0].distance(food) < 15:
        score += 1
        food_active = False
        display_score.show_score(score)
        print(score)

    if not food_active:
        food.reposition()

    if snake.cubes[0].xcor() >= 285 or snake.cubes[0].xcor() <= -285 or \
            snake.cubes[0].ycor() >= 285 or snake.cubes[0].ycor() <= -285:
        display_score.game_over()
        game_is_on = False



screen.exitonclick()





