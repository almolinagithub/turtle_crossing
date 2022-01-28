
from turtle import Turtle

INITIAL_POSITION = (0, - 250)
STEP = 10

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.goto(INITIAL_POSITION)
        self.setheading(90)

    def move_ahead(self):
        self.forward(STEP)