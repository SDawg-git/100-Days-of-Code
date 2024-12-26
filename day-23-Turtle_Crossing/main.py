import time
from turtle import Turtle, Screen
from player import Player
from car import Car
from level import Level

screen = Screen()
screen.tracer(0)
player = Player()
level = Level()
car = Car()


#screen.screensize(600, 600)                 #this doesn't work smh
screen.setup(width=600, height=600)
screen.listen()






game_over = False
count = 0

while not game_over:
    time.sleep(0.1)
    screen.update()


    #car spawning system

    if count >= 5:
        car.create_car()
        count = 0


    for i in car.all_cars:
        i.back(car.car_speed)          #moves cars at current level speed

        # hit detection system:
        if player.distance(i) < 15:
            level.game_over()
            game_over = True

        if i.xcor() < -330:
            car.all_cars.remove(i)


    # next level

    if player.ycor() > 280:
        player.return_player()
        car.level_up()
        level.next_level()

    count += 1

    #movement:

    screen.onkey(player.up, "Up")








screen.exitonclick()
