import random
from turtle import Turtle


r = random.randrange(0, 257, 10)
g = random.randrange(0, 257, 10)
b = random.randrange(0, 257, 10)
y_pos = random.randrange(-300,300,30)

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize()
        self.change_color()
        self.position(600, y_pos)

    def change_color(self):
        R = random.random()
        B = random.random()
        G = random.random()
        self.color(R, G, B)