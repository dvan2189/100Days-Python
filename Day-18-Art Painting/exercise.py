import turtle as t
import random

timmy_turtle  = t.Turtle()
timmy_turtle.color("red")

tom_turtle = t.Turtle()
tom_turtle.color("blue")

jack_turtle = t.Turtle()
jack_turtle.color("green")

randy_turtle = t.Turtle()

dany_turtle = t.Turtle()

colours = ["DimGray", "RoyalBlue", "LightSkyBlue", "MediumSeaGreen", 
			"DarkOliveGreen", "DarkOrange", "Gold", "DarkGreen"]

#Timmy will draw a rectangle 
for index in range(0,4):
	timmy_turtle.forward(40)
	timmy_turtle.right(90)

# Tom will draw a dash line
for index in range(0,15):
	tom_turtle.forward(10)
	tom_turtle.penup()
	tom_turtle.forward(10)
	tom_turtle.pendown()

#Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon
def draw_shape(number_edge):
	for _ in range(number_edge):
		jack_turtle.forward(100)
		jack_turtle.right(360/number_edge)

for shape_n_size in range(3,4):
	jack_turtle.color(random.choice(colours))
	draw_shape(shape_n_size)

#This time, Randy will do random walk
direction = [0,90,180,270]
t.colormode(255)

def random_color():
	r = random.randrange(255)
	g = random.randrange(255)
	b = random.randrange(255)
	rgb_tuple = (r,g,b)
	return rgb_tuple

for _ in range(10):
	randy_turtle.color(random_color())
	randy_turtle.width(10)
	randy_turtle.speed(4) #1-10: slowest -> fastest
	randy_turtle.forward(30)
	randy_turtle.setheading(random.choice(direction))

#This time, who volunteer to make spirograph
off_set = 5
for _ in range(int(360/off_set)):
	dany_turtle.color(random_color())
	dany_turtle.circle(100)
	dany_turtle.setheading(dany_turtle.heading() + off_set)
	dany_turtle.speed("fastest")



screen = t.Screen()
screen.exitonclick()