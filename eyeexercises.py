import turtle #graphics module
import random
import time

window = turtle.Screen()
window.title("Pong by RevelKnievel")
window.bgcolor("green")
window.setup(width = 1.0, height = 1.0)
window.tracer(0) #stops window from updating; must be manually updated; speeds up game

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball_dx = random.uniform(0.1, 0.5) #ball movement increments in pixels
ball_dy = random.uniform(0.1, 0.5)

#Main game loop
while True:
	window.update() #updates the screen
	
	#random speed changes
	if time.time() == time.time() + 0.5:
		ball_dx = random.uniform(0.1, 0.5)

	if time.time() == time.time() + 0.3:
		ball_dy = random.uniform(0.1, 0.5)

	#move the ball
	ball.setx(ball.xcor() - ball_dx)
	# print("ball_dx " + str(ball_dx))
	# print("xcor " + str(ball.xcor()))
	ball.sety(ball.ycor() + ball_dy)
	# print("ball_dy " + str(ball_dy))
	# print("ycor " + str(ball.ycor()))

	#ball border check
	if ball.ycor() > 350:
		ball.sety(350)
		ball_dy = random.uniform(0.1, 0.5)
		ball_dy *= -1
		print (time.time())

	if ball.ycor() < -350:
		ball.sety(-350)
		ball_dy = random.uniform(0.1, 0.5)

	if ball.xcor() > 550:
		ball.setx(550)
		ball_dx = random.uniform(0.1, 0.5)

	if ball.xcor() < -550:
		ball.setx(-550)
		ball_dx = random.uniform(0.1, 0.5)
		ball_dx *= -1