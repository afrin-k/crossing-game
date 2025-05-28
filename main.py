import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.title("Turtle Crossing Game")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

player = Player()
car_manager = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.move_forward,"Up")

# loop for the game
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    
    # collision with a car
    if car_manager.check_collision(player):
        game_is_on = False
        score.game_over()

    # updating levels
    if player.ycor()>280:
        score.increase_level()
        player.goto(0,-280)
        car_manager.increase_speed()

screen.exitonclick()