# ################################
#   Copyright (c) 2021 Jim Bray
#       All Rights Reserved
# ################################
from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.penup()
        self.color("white")
        self.width(20)
        self.shape("square")
        self.shapesize(5, 1, 1)
        self.setposition(position)
        self.speed(0)

    def up_move(self):
        new_y = self.ycor() + 20
        if new_y < 260:
            self.goto(self.xcor(), new_y)

    def down_move(self):
        new_y = self.ycor() - 20
        if new_y > - 260:
            self.goto(self.xcor(), new_y)


if __name__ == "__main__":
    from turtle import Screen
    screen = Screen()
    screen.setup(height=600, width=800)
    screen.bgcolor("black")
    screen.title("PONG")
    screen.tracer(0)

    pad = Paddle((350, 0))
    pad1 = Paddle((-350, 0))

    screen.listen()
    screen.onkey(pad.up_move, "Up")
    screen.onkey(pad.down_move, "Down")
    screen.onkey(pad1.up_move, "w")
    screen.onkey(pad1.down_move, "s")
    game_on = True

    while game_on:
        screen.update()

    screen.exitonclick()
