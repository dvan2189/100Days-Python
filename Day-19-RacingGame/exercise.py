

timmy_turtle = Turtle()
screen = Screen()


def move_forward():
	timmy_turtle.forward(10)

def move_backward():
	timmy_turtle.backward(10)

def turn_left():
	timmy_turtle.setheading(timmy_turtle.heading() + 5)

def turn_right():
	timmy_turtle.setheading(timmy_turtle.heading() - 5)

def clear_screen():
	timmy_turtle.clear()
	timmy_turtle.penup()
	timmy_turtle.home()
	timmy_turtle.pendown()


screen.listen()
screen.onkey(key="w",fun = move_forward)
screen.onkey(key="s",fun = move_backward)
screen.onkey(key="a",fun = turn_left)
screen.onkey(key="d",fun = turn_right)
screen.onkey(key="c",fun = clear_screen)


