from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.tracer(0)

screen.bgcolor("black")
screen.title("The Snack game")

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

is_game_on = True

screen.listen()
screen.onkey(snake.up,key="Up")
screen.onkey(snake.down,key="Down")
screen.onkey(snake.left,key="Left")
screen.onkey(snake.right,key="Right")



while is_game_on:
	#delay screen 0.1 second then refresh the screen
	screen.update()
	time.sleep(0.1)
	# let the snake move 20 pixels
	snake.move()
	#Detect collision with food
	distance_food= snake.head.distance(food)
	if distance_food < 15:
		food.refresh_food()
		snake.increase_size()
		scoreboard.update_score()


	#Detect collision with wall
	if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
		is_game_on = False
		scoreboard.game_over()

	#Detect collision with the tail
	for segment in snake.all_segment[1::1]:
		#if segment == snake.head:
		#	pass
		if snake.head.distance(segment) < 10:
			is_game_on = False
			scoreboard.game_over()

screen.exitonclick()