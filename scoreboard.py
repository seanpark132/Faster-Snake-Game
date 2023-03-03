from turtle import Turtle
FONT = ("Arial", 12, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.write("SCORE: 0", align="center", font=FONT)
        self.score = 0

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"SCORE: {self.score}", align="center", font=FONT)

    def end_game(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 36, "normal"))

    def update_timer(self, time_left):
        self.clear()
        self.goto(-200, 280)
        self.write(f"TIME LEFT: {time_left}",  align="left", font=FONT)

    def edit_stage(self, stage):
        self.clear()
        self.goto(140, 280)
        self.write(f"STAGE {stage}", align="center", font=FONT)