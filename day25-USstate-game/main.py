import csv
import turtle
import pandas
import csv


screen = turtle.Screen()
screen.title("US state game")
screen.setup(width=700, height=491)
image = "states.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
print(all_states)

already_guessed = []

with open("./guesses.txt") as guess:
    data1 = csv.reader(guess)
    for row in data1:
        if row[0] in all_states:
            already_guessed.append(row[0])


if len(already_guessed) > 0:
    for item in range(len(already_guessed)):
        state_name = already_guessed[item]
        w = data[data.state == state_name]
        xcor, ycor = int(w.x), int(w.y)
        coordinate = turtle.Turtle()
        coordinate.color("Black")
        coordinate.penup()
        coordinate.goto(xcor, ycor)
        coordinate.hideturtle()
        coordinate.write(f"{state_name}", align="center", font=("Courier", 10, "normal"))

score = 0
score += len(already_guessed)

game_on = True
while game_on:

    player_answer = screen.textinput(title=f"{score}/50 States Correct", prompt="Guess").title()
    if player_answer == "Exit":
        with open("./guesses.txt", mode="w") as guess:
            for row in already_guessed:
                guess.writelines(f"{row}\n")
        break
    if player_answer not in already_guessed:
        correct_answer = data[data.state == player_answer]
        xcor = int(correct_answer.x)
        ycor = int(correct_answer.y)

        coordinate = turtle.Turtle()
        coordinate.color("Black")
        coordinate.penup()
        coordinate.goto(xcor, ycor)
        coordinate.hideturtle()
        coordinate.write(f"{player_answer}", align="center", font=("Courier", 10, "normal"))
        already_guessed.append(player_answer)
        score += 1






