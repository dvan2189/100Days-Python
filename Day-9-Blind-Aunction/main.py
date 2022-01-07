import os
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
print("Welcome to the secret auction program")
aunction_bid = {}

def find_highest_bid(bidder_record):
  highest_bid = 0
  for bidder in bidder_record:
    if bidder_record[bidder] >= highest_bid:
      highest_bid = bidder_record[bidder]
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

def clear_screen():

    # It is for MacOS and Linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # It is for Windows platfrom
        _ = os.system('cls')

end_of_bid = True
while end_of_bid:
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: $"))
  aunction_bid[name] = bid
  continue_bid = input("Are there any other bidders?Type yes or no. ").lower()
  if continue_bid =="yes" or continue_bid =="y":
    end_of_bid = True
  else: 
    end_of_bid = False
  clear_screen()
  
find_highest_bid(aunction_bid)


