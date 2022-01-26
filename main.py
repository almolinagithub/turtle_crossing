from turtle import Screen
import random
import time
from car import Car
from tartaruga import Tartaruga

PLAYING = True
cars = []

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
car = Car()
for i in range(10):
    car = Car()
    cars.append(car)

#main loop
while PLAYING:
    time.sleep(0.04)
    screen.update()
    screen.tracer(0)
    for car in cars:
        car.move()
    type(cars)




screen.exitonclick()

