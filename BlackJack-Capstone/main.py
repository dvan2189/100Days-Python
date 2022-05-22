
from art import logo
import os
import random


def clear_screen():

    # It is for MacOS and Linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # It is for Windows platfrom
        _ = os.system('cls')


def calculate_score(cards):
  "Taking a list cards and return the sum of list cards"
  if(sum(cards)==21 and len(cards)==2):
    return 0
  if(11 in cards and sum(cards)>21):
    cards.remove(11)
    cards.append(1)
  return sum(cards)
    


def compare(user_score, computer_score):
  if(user_score >21 and computer_score >21):
    return "You and computer went over. Game draw"

  if user_score ==21 and len(user_score)==5:
    return "You win with 5 cards"
  if user_score == computer_score:
    return "Game draw"
  elif(user_score ==0):
    return "You win with BlackJack"
  elif computer_score ==0:
    return "Oop, the computer has BlackJack. We lose"
  elif user_score > 21:
    return "Went over. You lose"
  elif computer_score > 21:
    return "Computer went over. You win"
  elif user_score > computer_score:
    return "You win"

  else:
    return "You lose"

def deal_card():
  cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
  card = random.choice(cards)
  return card
  
def play_game():
  print(logo)

  user_cards = []
  computer_cards = []
  isGameOver = False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not isGameOver:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"You card: {user_cards} with the score is {user_score}")
    print(f"Computer first card: {computer_cards[0]}")

    if(user_score ==0 or computer_score==0 or user_score > 21):
      isGameOver = True
    else:
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass ").lower()
      if user_should_deal =='y':
        user_cards.append(deal_card())
      else:
        isGameOver = True
  while computer_score !=0 and computer_score <17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"You final hand: {user_cards} with the score is {user_score}")

  print(f"Computer final hand: {computer_cards} with the score is {computer_score}")

  print(compare(user_score, computer_score))
    

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear_screen()
  play_game()