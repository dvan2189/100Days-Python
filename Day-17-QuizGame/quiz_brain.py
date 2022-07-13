import random

class QuizBrain:
	def __init__(self, q_list):
		self.question_number = 0
		self.question_list = q_list
		#self.appearance = [False] * len(q_list)
		self.score = 0
		#self.question_standing = 0

	def randomly_question(self):
		self.question_number = random.randrange(0, len(self.question_list))
		self.appearance[self.question_number] = True
		print(f"Appreance list: {self.appearance}")

	def next_question(self):
		#self.randomly_question()
		#if self.appearance[self.question_number]== True: 
		#	self.randomly_question()
		current_question = self.question_list[self.question_number]
		self.question_number += 1
		#self.question_standing += 1
		user_answer = input(f"Q. {self.question_number} : {current_question.text} (True/False): ").lower()
		self.check_answer(user_answer,current_question.answer.lower())

	def still_have_question(self):
		if self.question_number > len(self.question_list):
			return False
		else: return True

	def check_answer(self, answer, correct_answer):
		if answer == correct_answer:
			self.score += 1
		print(f"Current score of the user is: {self.score}/{self.question_number}\n")