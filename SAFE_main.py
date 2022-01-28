from turtle import Screen
import random
import time
from SAFE_car_manager import CarManager
from SAFE_tartaruga import Tartaruga

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


#event handler to move the turtle
screen.onkey(tarta.move_up, "Up")
screen.onkey(tarta.move_down, "Down")

#create the car(s)
car_manager = CarManager()


#main loop
while PLAYING:
    time.sleep(0.1)
    screen.update()
    screen.tracer(0)
    car_manager.create_car()
    car_manager.move_cars()





screen.exitonclick()

