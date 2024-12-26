import random
from turtle import Turtle

LEVEL_1_SPEED = 10
LEVEL_2_SPEED = 50
LEVEL_3_SPEED = 20

class Car():
    def __init__(self):
        self.level = 1
        self.all_cars = []
        self.car_speed = 10


    def create_car(self):
        colors = ["Blue", "Green", "Red", "Orange", "Brown", "Magenta"]

        new_car = Turtle()
        new_car.shape("square")
        new_car.X_POS = 330                             # makes sure cars spawn invisible to user
        new_car.Y_POS = self.random_y_position()
        new_car.penup()
        new_car.setx(new_car.X_POS)
        new_car.sety(new_car.Y_POS)
        new_car.shapesize(1, 2)
        new_car.color(random.choice(colors))
        self.all_cars.append(new_car)


    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += 10

    def current_level(self):
        if self.level == 1:
            return LEVEL_1_SPEED
        elif self.level == 2:
            return LEVEL_2_SPEED
        elif self.level == 3:
            return LEVEL_3_SPEED


    def random_y_position(self):
        return random.randint(-280, 280)



