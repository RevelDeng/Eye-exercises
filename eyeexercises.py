import turtle #graphics module
import random
# import time
import threading

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

#random ball speed
def randomspeed():
	return random.uniform(0.1, 0.9)

ball_dx = randomspeed()
ball_dy = randomspeed()

#ball movement increments in pixels
def balldirection():
	ball_dx = randomspeed()
	ball_dy = randomspeed()

#Main loop
while True:
	window.update() #updates the screen
	
	#random speed changes
	threading.Timer(5, balldirection()).start()
	# if time.time() == time.time() + 0.5:
	# 	ball_dx = randomspeed()
	# 	print ("ball dx " + str(ball_dx))
	# 	if random.randint(0, 1) == 0:
	# 		ball_dx *= -1
	# 		print ("ball dx " + str(ball_dx))

	# if time.time() == time.time() + 0.3:
	# 	ball_dy = randomspeed()
	# 	print ("ball dy " + str(ball_dy))
	# 	if random.randint(0, 1) == 0:
	# 		ball_dy *= -1
	# 		print ("ball dy " + str(ball_dy))

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
		ball_dy = randomspeed()
		ball_dy *= -1

	if ball.ycor() < -350:
		ball.sety(-350)
		ball_dy = randomspeed()

	if ball.xcor() > 550:
		ball.setx(550)
		ball_dx = randomspeed()

	if ball.xcor() < -550:
		ball.setx(-550)
		ball_dx = randomspeed()
		ball_dx *= -1