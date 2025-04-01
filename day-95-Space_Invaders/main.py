from turtle import Turtle, Screen
import time
from ship import Ship
from projectile import Projectile
from enemy import Enemy
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.title("Space Invaders")
screen.setup(height=500, width=450)

ship = Ship()
scoreboard = Scoreboard()

game_over = False
sleep_time = 0.05

enemies = []
rows = 3
cols = 6
start_x = -150
start_y = 220
spacing_x = 50
spacing_y = 40

for row in range(rows):
    for col in range(cols):
        enemy_x = start_x + (col * spacing_x)
        enemy_y = start_y - (row * spacing_y)
        enemies.append(Enemy(enemy_x, enemy_y))


count = 0
while not game_over:
    time.sleep(sleep_time)
    screen.update()

    for projectile in ship.projectiles:
        projectile.move_projectile()
        if not projectile.active:
            ship.projectiles.remove(projectile)


    for enemy in enemies:
        enemy.move()
        if enemy.ycor() < -210:
            game_over = True

        for projectile in ship.projectiles:


            if enemy.distance(projectile) < 20:
                enemy.setposition(300,300)  #moving it out of the way before removing it from the list
                enemies.remove(enemy)
                projectile.setposition(300, 300)
                ship.projectiles.remove(projectile)
                scoreboard.update_score()
                scoreboard.update_scoreboard()

    if not enemies:
        scoreboard.win()



    screen.listen()
    screen.onkey(ship.move_left, "Left")
    screen.onkey(ship.move_right, "Right")
    screen.onkey(ship.shoot, "Up")
