'''class User:
	def __init__(self, id,username):
		self.id = id
		self.username = username
		self.followers = 0
		self.following = 0

	def follow(self,user):
		user.followers +=1
		self.following +=1


user_1 = User("001","Daniel")
user_2 = User("002","Amenda")
user_1.follow(user_2)
print(f"User ID {user_1.id} name is: {user_1.username} has the follower: {user_1.followers} and following: {user_1.following}")
print(f"User ID {user_2.id} name is: {user_2.username} has the follower: {user_2.followers} and following: {user_2.following}")
'''
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
	question_bank.append(Question(question["text"], question["answer"]))

question_list = QuizBrain(question_bank)
question_list.next_question()

while question_list.still_have_question():
	question_list.next_question()

print(f"You completed the quiz and your final score is: {question_list.score}/{question_list.question_number}")


