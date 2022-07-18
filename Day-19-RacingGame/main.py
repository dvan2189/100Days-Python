from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(width = 500, height = 400)

is_race_on = False
user_bet = screen.textinput(title="Make your best", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red","orange","yellow","green","blue","purple"]

all_turtle = []
clone_turtle = Turtle()
begin_at = 30
delta = 40
for turtle_index in range(0,6):
	clone_turtle = Turtle(shape="turtle")
	clone_turtle.color(colors[turtle_index])
	clone_turtle.penup()
	clone_turtle.goto(-screen.window_width()/2 + begin_at,-screen.window_height()/2 + begin_at + delta)
	delta += 40
	all_turtle.append(clone_turtle)

if user_bet:
	is_race_on = True

while is_race_on:
	# turtle run with random speed from 0 to 10 
	rand_distance = random.randint(0,10)
	for turtle in all_turtle:
		rand_distance = random.randint(0,10)
		turtle.forward(rand_distance)
		if turtle.xcor() > 220:
			is_race_on = False
			winning_turtle = turtle.pencolor()
			if winning_turtle == user_bet:
				print(f"You won! The {user_bet} turtle is the winner")
			else:
				print(f"You lost! The {winning_turtle} turtle is the winner")
screen.exitonclick()