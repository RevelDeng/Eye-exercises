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
ball_dx = 0.3 #ball movement increments in pixels
ball_dy = 0.3

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
# pen.write("Player A: {0} Player B: {1}".format(score_a, score_b), align = "center", font = ("Courier", 20, "normal"))

#Main game loop
while True:
	window.update() #updates the screen

	#move the ball
	ball.setx(ball.xcor() - random.randint(1, 3))
	ball.sety(ball.ycor() + random.randint(1, 3))

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
