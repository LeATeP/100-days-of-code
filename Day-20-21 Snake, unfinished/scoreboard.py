from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        score = super().__init__()
        self.penup()
        self.color("White")
        self.hideturtle()
        self.goto(0, 260)

    def show_score(self, food):
        self.clear()
        self.write(f"score: {food}", move=False, align="center", font=("Arial", 20, "normal"))

    def game_over(self):
        self.color("Blue")
        self.goto(0, 0)
        self.write(f"Game Over", move=False, align="center", font=("Arial", 30, "normal"))