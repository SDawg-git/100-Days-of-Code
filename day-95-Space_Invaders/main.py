from turtle import Turtle, Screen
import time
from ship import Ship
from projectile import Projectile
from enemy import Enemy

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.title("Space Invaders")
screen.setup(height=500, width=450)

ship = Ship()
enemy = Enemy()

game_over = False
sleep_time = 0.05

while not game_over:
    time.sleep(sleep_time)
    screen.update()

    for projectile in ship.projectiles:
        projectile.move_projectile()
        if not projectile.active:
            ship.projectiles.remove(projectile)


    screen.listen()
    screen.onkey(ship.move_left, "Left")
    screen.onkey(ship.move_right, "Right")
    screen.onkey(ship.shoot, "Up")
