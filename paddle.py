# create paddle class in order to generate paddles for Pong
from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.setheading(90)
        self.color("white")
        self.shapesize(stretch_len=5)
        self.setposition(position) 

    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.setheading(90)
        self.backward(20)
        


class Walls(Turtle):
    def __init__(self, position, length):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=length)
        self.setposition(position)
    