import random
from turtle import Turtle
import time


COLORS = ["blue", "yellow", "green", "red", "purple"]
car_step = random.randint(2, 20)
car_distance = random.randrange(25, 35, 1)


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []

    def create_car(self):
        random_chance = random.randint(1, 3)
        if random_chance == 1:
            y_pos = random.randrange(-250, 450, car_distance)
            new_car = Turtle("square")
            new_car.speed(10)
            new_car.left(180)
            new_car.penup()
            new_car.shapesize(1, 2)
            new_car.color(random.choice(COLORS))
            new_car.goto(300, y_pos)
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.forward(10)



