from turtle import Turtle 

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.goto(0,-280)
        self.setheading(90)
        
    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    
