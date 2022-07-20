from turtle import Turtle

DELTA_RANGE = 0
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
	def __init__(self):
		self.all_segment = []
		self.create_snake()
		self.head = self.all_segment[0]

	def create_snake(self):
		for segment_index in range(0,3):
			self.add_segment()

	def move(self):
		for seg_num in range(len(self.all_segment)-1,0,-1):
			new_x = self.all_segment[seg_num-1].xcor()
			new_y = self.all_segment[seg_num-1].ycor()
			self.all_segment[seg_num].goto(new_x,new_y)
		self.all_segment[0].forward(MOVE_DISTANCE)

	def up(self):
		if self.head.heading() != DOWN:
			self.head.setheading(UP)

	def down(self):
		if self.head.heading() != UP:
			self.head.setheading(DOWN)

	def left(self):
		if self.head.heading() != RIGHT:
			self.head.setheading(LEFT)

	def right(self):
		if self.head.heading() != LEFT:
			self.head.setheading(RIGHT)

	def increase_size(self):
		self.add_segment()

	def add_segment(self):
		global DELTA_RANGE
		segment = Turtle()
		segment = Turtle(shape="square")
		segment.color("white")
		segment.penup()
		segment.goto(0 - DELTA_RANGE, 0)
		DELTA_RANGE += 20
		self.all_segment.append(segment)

