
from turtle import Turtle


class Tartaruga(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()

    def move_up(self):
        self.forward(10)

    def move_down(self):
        self.back(10)



