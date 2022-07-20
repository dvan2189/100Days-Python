from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 18, 'normal')

class ScoreBoard(Turtle):

	def __init__(self):
		super().__init__()
		self.score = 0
		self.color("white")
		self.penup()
		self.goto(0,280)
		self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)
		self.hideturtle()
		
	def update_score(self):
		self.score += 1
		self.clear()
		self.write(f"Score: {self.score}", move=False, align="center", font=('Arial', 12, 'normal'))

	def game_over(self):
		self.goto(0,0)
		self.write(f"Game over!", move=False, align=ALIGNMENT, font=FONT)
