# ################################
#   Copyright (c) 2021 Jim Bray
#       All Rights Reserved
# ################################
from turtle import Turtle

FONT = ("courier", 80, "normal")
ALIGN = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.penup()
        self.color("white")
        self.setposition(0, 200)
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        text = f"{self.l_score}  {self.r_score}"
        self.write(text, move=False, align=ALIGN, font=FONT)

    def check_score(self):
        if self.l_score >= 8 or self.r_score >= 8:
            self.game_over()
            game_go = False
        else:
            game_go = True
        return game_go


    def game_over(self):
        text = f"GAME OVER"
        self.setposition(0, 0)
        self.write(text, move=False, align=ALIGN, font=FONT)

    def add_to_r_score(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()

    def add_to_l_score(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()


if __name__ == "__main__":
    from turtle import Screen
    from time import sleep
    screen = Screen()
    screen.setup(height=600, width=800)
    screen.bgcolor("black")
    screen.title("PONG")
    screen.tracer(0)
    score = Scoreboard()
    sleep(2)
    score.add_to_r_score()
    sleep(2)
    score.add_to_l_score()
    sleep(2)
    score.add_to_r_score()
    sleep(2)
    score.add_to_l_score()
    screen.exitonclick()
