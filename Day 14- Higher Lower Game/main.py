from art import logo
from art import vs
from game_data import data
import random
import os 


def get_random():
  #get a random choice from the list data 
  random_choice = random.choice(data)
  return random_choice

def presentation_format(account):
  # representation the data format 
  name = account["name"]
  description = account["description"]
  country = account["country"]
  return f"{name} a {description} from {country}"

def check_answer(guess, a_follower, b_follower):
  #check the guess from input with two account followers
  if(a_follower > b_follower):
    return guess == "a" # it return true if guess is a which is a follower greater than b follower
  else: 
    return guess == "b"

def clear_screen():

    # It is for MacOS and Linux(here, os.name is 'posix')
  if os.name == 'posix':
    _ = os.system('clear')
  else:
    # It is for Windows platfrom
    _ = os.system('cls')   
  
def game():
  print(logo)
  score = 0
  game_continue = True
  account_one = get_random()
  account_two = get_random()

  while(game_continue):
    account_one = account_two # if the game_continue is true mean we keep compare the one before with the new one after
    account_two = get_random()

    while(account_one == account_two):
      account_two = get_random()
      
    print(f"Compare A: {presentation_format(account_one)}.")
    print(vs)  
    print(f"Against B: {presentation_format(account_two)}.")
  
    guess = input("Who has more follower A or B: ").lower()
    a_follower = account_one["follower_count"]
    print(a_follower)
    b_follower = account_two["follower_count"]
    print(b_follower)
    is_correct = check_answer(guess, a_follower,b_follower)

    clear_screen()
    print(logo)
    if(is_correct):
      score +=1
      print(f"You are right! Your current score is: {score}")
    else:
      game_continue = False
      print(f"Oop, your guess is wrong. Your final score: {score}")
  
game()

