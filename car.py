import random
from turtle import Turtle
import time

cars = []
r = random.randrange(0, 257, 10)
g = random.randrange(0, 257, 10)
b = random.randrange(0, 257, 10)
car_step = random.randint(2, 20)
car_distance = random.randrange(25,35,1)

class Car(Turtle):
    def __init__(self):
        super().__init__()
        y_pos = random.randrange(-300, 300,car_distance)
        self.shape("square")
        self.speed(10)
        self.left(180)
        self.penup()
        self.shapesize(1,2)
        self.change_color()
        self.goto(300, y_pos)


    def change_color(self):
        R = random.random()
        B = random.random()
        G = random.random()
        self.color(R, G, B)

    def move(self):
        car_step = random.randint(2, 10)
        self.forward(car_step)
