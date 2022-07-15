import colorgram
import turtle as t
import random

t.colormode(255)


tom_turtle = t.Turtle()
tom_turtle.penup()
tom_turtle.hideturtle()
tom_turtle.speed("fastest")
screen = t.Screen()

number_of_dots = 210
dot_per_line = 15
space_between_dot = 40
space_between_line = 40
list_colors = []

colors = list(colorgram.extract("images_2.jpeg", 100))
for c in colors:
	red = c.rgb.r
	green = c.rgb.g
	blue = c.rgb.b
	rgb_color = (red,green,blue)
	list_colors.append(rgb_color)

width = t.window_width()
height = t.window_height()
tom_turtle.goto(-int(width/2)+80,-int(height/2)+90)

# Tom will draw a dash line
for count in range(1,number_of_dots+1):
	tom_turtle.dot(20,random.choice(list_colors))
	tom_turtle.forward(space_between_dot)
	if count % dot_per_line == 0:
		tom_turtle.setheading(90)
		tom_turtle.forward(space_between_line)
		tom_turtle.setheading(0)
		tom_turtle.setheading(180)
		tom_turtle.forward(space_between_dot * dot_per_line)
		tom_turtle.setheading(0)


screen.exitonclick()