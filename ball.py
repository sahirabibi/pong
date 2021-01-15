# create a ball that moves around the screen 
from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color(random.choice(['pink', 'violet', 'blue', 'white', 'orange']))
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def motion(self, heading=0):
        self.setheading(heading)
        old_x = self.xcor()
        old_y = self.ycor()
        new_x = old_x + self.x_move
        new_y = old_y + self.y_move
        self.goto(new_x, new_y)
        
    def bounce_y(self):
        self.y_move *= -1
        

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_pos(self):
        self.move_speed = 0.1


    


