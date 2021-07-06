from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    q = Turtle(shape="turtle")
    q.penup()
    q.goto(x=-230, y=y_position[turtle_index])
    q.color(colors[turtle_index])
    all_turtles.append(q)


print(all_turtles)
if user_bet:
    is_race_on = True


while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winner = turtle.color()
            if winner[0] == user_bet:
                print(f"Your bet is won The color: {winner[0]} Winner")
            else:
                print(f"You've lost! The {winner[0]} is the winner")

            is_race_on = False
            break
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)



screen.exitonclick()

