import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()

screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
# turn off animation
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


# need to create while loop to manual update screen everytime to turn on animation
game_is_on = True
while game_is_on:
    # this is ball's speed
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # detect ball bounce wall top and bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with r_paddle & l_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        # print("made contact")
        ball.bounce_x()
    #need to separate it due to score system.
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor() < - 380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()

