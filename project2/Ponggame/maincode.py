from turtle import Turtle,Screen
from paddle import paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)

screen.title("Pong")
screen.tracer(0)

l_paddle  = paddle((-370,0))
r_paddle = paddle((370,0))
ball = Ball()
scoreboard = ScoreBoard()


screen.listen()
screen.onkeypress(fun=r_paddle.moveup,key="Up")
screen.onkeypress(fun=r_paddle.movedown,key="Down")
screen.onkeypress(fun=l_paddle.moveup,key="w")
screen.onkeypress(fun=l_paddle.movedown,key="s")


game_is_on =True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() >280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 45 and ball.xcor() > 340 or ball.distance(l_paddle) < 45 and ball.xcor() < -340:
        ball.bounce_x()
        
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()























screen.exitonclick()


