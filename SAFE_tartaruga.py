
from turtle import Turtle

STARTING_POSITION = (0,-280)
MOVE_DISTANCE = 10

class Tartaruga(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setpos(STARTING_POSITION)
        self.setheading(90)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        self.back(10)

    def move_right(self):
        self.right(10)

    def move_left(self):
        self.left(10)



