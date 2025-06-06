from turtle import Turtle
FONT = ("Trebuchet MS", 20, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(-280,250)
        self.hideturtle()
        self.level = 1
        self.update_level()

    # level manipulations
    def update_level(self):
        self.clear()
        self.write(f"Level : {self.level}",align="left",font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_level()

    # game over message
    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("Game Over.",align="center",font=FONT)

