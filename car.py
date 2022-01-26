import random
from turtle import Turtle


r = random.randrange(0, 257, 10)
g = random.randrange(0, 257, 10)
b = random.randrange(0, 257, 10)
car_step = random.randint(2, 20)


class Car(Turtle):
    def __init__(self):
        super().__init__()
        y_pos = random.randrange(-300, 300,20)
        self.shape("square")
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
        self.forward(car_step)