from time import sleep
from turtle import Turtle, Screen
from paddles import Paddle
from ball import Ball
import time
from score import Score


screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.title("PONG")
screen.setup(height=600, width=800)

right_paddle = Paddle()
left_paddle = Paddle()
ball = Ball()


left_paddle.goto(x=-350, y=0)
right_paddle.goto(x= 350, y=0)

screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

l_score = Score(-380, 280)
r_score = Score(330, 280)

game_over = False
#angle = ball.starter_angle()

sleep_time = 0.1
while not game_over:
    time.sleep(sleep_time)
    screen.update()

    ball.move()

#   ball.setheading(angle)
#    ball.forward(1)


# if ball.ycor() > 300 or ball.ycor() < -300:
# if angle < 180:                               #doesn't really work, gotta re-do this the way she did it
# angle = 180 - angle
# else:
# angle = 360 - angle

    #collision with ceiling and floor
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()


    #paddle bounce
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or (ball.distance(left_paddle) < 50 and ball.xcor() < -320):

        ball.bounce_x()
        if sleep_time >= 0.01:
            sleep_time -= 0.01

    if ball.xcor() > 380 :
        l_score.score +=1
        l_score.update_score()
        sleep_time = 0.1
        ball.reset_position()

    if ball.xcor() < -380:
        r_score.score +=1
        r_score.update_score()
        sleep_time = 0.1
        ball.reset_position()



screen.exitonclick()
