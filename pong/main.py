# ################################
#   Copyright (c) 2021 Jim Bray
#       All Rights Reserved
# ################################
from turtle import Screen, Turtle
from time import sleep
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard
from game_net import Net


BOUND = 280


screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

net = Net()
ball = Ball()
score = Scoreboard()
r_pad = Paddle((350, 0))
l_pad = Paddle((-350, 0))

screen.listen()
screen.onkey(r_pad.up_move, "Up")
screen.onkey(r_pad.down_move, "Down")
screen.onkey(l_pad.up_move, "w")
screen.onkey(l_pad.down_move, "s")
game_on = True

while game_on:
    sleep(ball.run_speed)
    screen.update()
    ball.move_ball()
    # Detect Wall Collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect Paddle Collision
    if ball.distance(r_pad) < 50 and ball.xcor() > 320 or ball.distance(l_pad) < 50 and ball.xcor() < - 320:
        ball.bounce_x()

    # Detect R Side Miss
    if ball.xcor() > 420:
        score.add_to_l_score()
        ball.new_ball()

    # Detect Left Side Miss
    if ball.xcor() < -420:
        score.add_to_r_score()
        ball.new_ball()

    # Detect End Of Game
    if score.check_score():
        game_on = True
    else:
        game_on = False

screen.exitonclick()
