#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from random import randint
from art import logo

print(logo)
print("Welcome to the Number Guessing Game")
print("I think about the number between 1 and 100")

guess_number = randint(0,100)
EASY_LEVEL = 10
HARD_LEVEL = 5
def choice_game():
  start_game = input("Choose a difficult. Type 'easy' or 'hard':").lower()
  if start_game == "easy":
    number_attemp = EASY_LEVEL
  else:
    number_attemp = HARD_LEVEL
  
  return number_attemp

def compare(user_choice, number_attemp):
  if(user_choice > guess_number):
    print("Too high")
    return number_attemp -1
  elif(user_choice < guess_number):
    print("Too low")
    return number_attemp -1
  else:
    print(f"Hooray. Your guess is correct and guessing number is {guess_number}")

def game():
  number_attemp = choice_game()
  user_choice = 0
  while(user_choice !=guess_number):
    print(f"You have {number_attemp} attemp remainding to guess the number")
    user_choice = int(input("Make a guess: "))
    number_attemp = compare(user_choice, number_attemp)
  
    if (number_attemp ==0):
      print("You ran out of attemp. You lose")
      break
  print(f"Guessing number is: {guess_number}")

game()