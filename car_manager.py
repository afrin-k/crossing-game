from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 5

class CarManager():
    def __init__(self):
        self.all_cars = []
        self.move_distance = 5
        self.random_a = 1
        self.random_b = 6
    
    def create_car(self):
        random_chance = random.randint(self.random_a,self.random_b)
        if random_chance == self.random_a:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(300,random.randint(-250,250))
            new_car.setheading(180)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.move_distance)           
    
    # collision with player 
    def check_collision(self,player):
        for car in self.all_cars:
            if player.distance(car)<20:
                return True

    # increase speed of cars
    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT
    
