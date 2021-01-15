# create screen 
import turtle
from turtle import Turtle, Screen 
import time
from paddle import Paddle, Walls
from ball import Ball
from scoreboard import ScoreBoard 

screen = Screen()
screen.setup(height=600, width = 800)
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
r_scoreboard = ScoreBoard((100, 200))
l_scoreboard = ScoreBoard((-100, 200))
ball = Ball()
top_wall = Walls((0, 350), 40)
bottom_wall = Walls((0, -300), 40)



turtle.listen()

turtle.onkey(fun=r_paddle.move_up, key = "Up")
turtle.onkey(fun=r_paddle.move_down, key="Down")
turtle.onkey(fun=l_paddle.move_up, key="w")
turtle.onkey(fun=l_paddle.move_down, key="s")


game_on = True
while game_on: 
    time.sleep(ball.move_speed)
    screen.update()
    ball.motion()
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()
   
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    if ball.xcor() > 380:
        r_scoreboard.point()
        ball.goto(0, 0)
        ball.bounce_x()
        
        
    if ball.xcor() < -380:
        l_scoreboard.point()
        ball.goto(0,0)
        ball.bounce_x()
        ball.reset_pos()
        
    
    if r_scoreboard.score == 10 or l_scoreboard.score == 10:
        r_scoreboard.game_over()
        game_on = False


# create another paddle 
# create the ball and make it move 
# detect collision with wall and bounce 
# detect collision with paddles 
# detect when paddle misses 
# keep score 
screen.exitonclick()