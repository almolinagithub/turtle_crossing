
import turtle
import time
from player import  Player
from car_manager import Car_Manager

screen = turtle.Screen()
screen.screensize(600, 600)
screen.title("Turtle crossing game")
screen.listen()
screen.tracer(0)

PLAYING = True

#create the player
player = Player()

#move the player ahead
screen.onkey(player.move_ahead, "Up")

#create the car manager
car_manager = Car_Manager()

while PLAYING:
    time.sleep(0.1)
    car_manager.create_car()
    car_manager.move_car()
    screen.update()

screen.exitonclick()

