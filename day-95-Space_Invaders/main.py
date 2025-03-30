from turtle import Turtle, Screen
import time
from ship import Ship
from projectile import Projectile

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.title("Space Invaders")
screen.setup(height=500, width=450)


ship = Ship()


def shoot():
    projectile = Projectile()
    projectile.setposition(ship.xcor(), ship.ycor())
    for count in range(20):
        projectile.forward(10)


game_over = False
sleep_time = 0.05

while not game_over:
    time.sleep(sleep_time)
    screen.update()

    screen.listen()
    screen.onkey(ship.move_left, "Left")
    screen.onkey(ship.move_right, "Right")
    screen.onkey(shoot, "Up")
