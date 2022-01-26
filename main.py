from turtle import Screen
import random
import time
from car import Car
from tartaruga import Tartaruga

PLAYING = True

#create the screen
screen = Screen()
screen.title("Turtle crossing")
screen.screensize(600, 600)
screen.tracer(0)
screen.listen()

#create the turtle
tarta = Tartaruga()
tarta.setpos(0, -300)
tarta.setheading(90)

#event handler to move the turtle
screen.onkey(tarta.move_up, "Up")
screen.onkey(tarta.move_down, "Down")

#create the car(s)

for i in range(20):
    car = Car()
    car
    print(car)

#main loop
while PLAYING:
    time.sleep(0.1)
    screen.update()
    screen.tracer(0)
    car.move()

screen.exitonclick()

