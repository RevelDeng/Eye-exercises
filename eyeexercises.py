import turtle #graphics module
import random

window = turtle.Screen()
window.title("Pong by RevelKnievel")
window.bgcolor("green")
window.setup(width = 800, height = 600)
window.tracer(0) #stops window from updating; must be manually updated; speeds up game

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()

#Main game loop
while True:
	window.update() #updates the screen
	
	ball_dx = random.uniform(0.1, 1) #ball movement increments in pixels
	ball_dy = random.uniform(0.1, 1)
	
	#move the ball
	ball.setx(ball.xcor() - ball_dx)
	print(ball_dx)
	print("xcor " + str(ball.xcor()))
	ball.sety(ball.ycor() + ball_dy)
	print(ball_dy)
	print("ycor " + str(ball.ycor()))

	#ball border check
	if ball.ycor() > 288:
		ball.sety(288)
		ball_dy *= -1

	if ball.ycor() < -282:
		ball.sety(-282)
		ball_dy *= -1

	if ball.xcor() > 382:
		ball.setx(382)
		ball_dx *= -1

	if ball.xcor() < -388:
		ball.setx(-388)
		ball_dx *= -1