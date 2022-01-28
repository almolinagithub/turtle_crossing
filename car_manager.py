import random
from turtle import Turtle

COLORS = ["yellow", "green", "red"]
STEP = 10

class Car_Manager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []

    def create_car(self):
        random_chance = random.randint(1, 5)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.setheading(180)
            new_car.goto(280, random.randrange(-230, 280, 30))
            new_car.shapesize(1, 2)
            self.cars.append(new_car)

    def move_car(self):
        for car in self.cars:
            car.forward(STEP)
