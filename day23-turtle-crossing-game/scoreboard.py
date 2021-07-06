from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("Black")
        self.hideturtle()
        self.goto(-200, 260)

    def show_score(self, level):
        self.clear()
        self.write(f"Level: {level}", move=False, align="center", font=FONT)

    def game_over(self):
        self.color("Blue")
        self.goto(0, 0)
        self.write(f"Game Over", move=False, align="center", font=("Arial", 30, "normal"))
