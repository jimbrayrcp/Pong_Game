# ################################
#   Copyright (c) 2021 Jim Bray
#       All Rights Reserved
# ################################
from turtle import Turtle

BOUND = 260
CANVAS_HEIGHT = 600


class Net(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(0.5, 0.5, 0)

        for i in range(-320, 320, 40):
            self.stamp()
            self.setposition(0, i)


if __name__ == "__main__":
    from turtle import Screen
    screen = Screen()
    screen.setup(height=600, width=800)
    screen.bgcolor("black")
    screen.title("PONG")
    # screen.tracer(0)

    net = Net()


    screen.listen()
    screen.exitonclick()
