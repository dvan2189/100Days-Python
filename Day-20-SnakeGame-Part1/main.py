from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.tracer(0)

screen.bgcolor("black")
screen.title("The Snack game")

snake = Snake()


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

screen.exitonclick()