# ################################
#   Copyright (c) 2021 Jim Bray
#       All Rights Reserved
# ################################
from turtle import Turtle

BOUND = 260
CANVAS_HEIGHT = 600
xlist = [0.1, 0.09, 0.08, 0.07, 0.06, 0.05, 0.04, 0.03, 0.02, 0.001, 0]
# i += 1
# print(var)
# # ball.speed(speed=var)
# if var == 0:
#     i = 0


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.run_speed = 0.1

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.run_speed *= 0.9

    def new_ball(self):
        self.run_speed = 0.1
        self.home()
        self.bounce_x()



if __name__ == "__main__":
    from turtle import Screen
    from time import sleep
    from paddles import Paddle

    screen = Screen()
    screen.setup(height=600, width=800)
    screen.bgcolor("black")
    screen.title("PONG")
    screen.tracer(0)

    ball = Ball()
    r_pad = Paddle((350, 0))
    l_pad = Paddle((-350, 0))

    screen.listen()
    screen.onkey(r_pad.up_move, "Up")
    screen.onkey(r_pad.down_move, "Down")
    screen.onkey(l_pad.up_move, "w")
    screen.onkey(l_pad.down_move, "s")
    game_on = True

    while game_on:
        sleep(0.1)
        screen.update()
        ball.move_ball()
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        if ball.distance(r_pad) < 50 and ball.xcor() > 320 or ball.distance(l_pad) < 50 and ball.xcor() > - 320:
            ball.bounce_x()

        if ball.xcor() > 420:
            game_on = False

        if ball.xcor() < -420:
            game_on = False

    screen.exitonclick()
