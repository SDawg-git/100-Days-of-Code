from turtle import Turtle, Screen
from ball import Ball
from paddle import Paddle
from block import Block
import time

screen = Screen()
screen.tracer(0)
screen.bgcolor("gray")
screen.title("Breakout")
screen.setup(height=500, width=350)


ball = Ball()
paddle = Paddle()
blocks = []

block_x = 120
block_y = 200
count = 6

for i in range(28):
    if count > 0:
        block = Block()
        block.setposition(block_x, block_y)
        block_x -= 50                           #moves the next block over to the left by 50
        count -= 1                              #count makes sure there's 6 blocks per row
        blocks.append(block)
    else:
        block_y -= 30                           #moves on to next row after 6 blocks have been reached
        block_x = 120
        count = 6

screen.listen()
screen.onkey(paddle.move_left, "Left")
screen.onkey(paddle.move_right, "Right")



game_over = False

sleep_time = 0.05
while not game_over:

    time.sleep(sleep_time)
    screen.update()
    ball.move()

    # left-right wall bounce
    if ball.xcor() >= 150 or ball.xcor() <= -150:
        ball.bounce_wall()

    #top wall bounce
    if ball.ycor() >= 230:
        ball.bounce_top()

    #paddle bounce
    if ball.distance(paddle) < 40 and ball.ycor() < -180:
        ball.bounce_paddle()

    #game loss
    if ball.ycor() < -230:
        game_over = True

    #block hit
    for block in blocks:
        if ball.distance(block) < 25:
            ball.bounce_top()
            block.hideturtle()
            blocks.remove(block)
