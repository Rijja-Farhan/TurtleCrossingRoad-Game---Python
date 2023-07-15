from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.Level = 1
        self.goto(-280,280)
        self.color("white")
        self.hideturtle()
        self.write(f"Level : "+ str(self.Level))
    def update_score(self,sleep_time):
        self.Level += 1
        self.clear()
        self.write(f"Level : "+ str(self.Level))


