
#from replit import clear
from art import logo
import random

def deal_card():
  """Returns a random card from the deck"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def compare(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return "  you loose"
  elif user_score == computer_score:
    return "  Draw"
  elif user_score == 0:
    return "  User Wins"
  elif computer_score == 0:
    return "  Computer Wins"
  elif user_score > 21:
    return "  User went over.Computer wins"
  elif computer_score > 21:
    return "  Computer went over. Its a bust. User Wins"
  elif user_score > computer_score:
    return "  User Wins"
  elif user_score < computer_score:
    return "  Computer Wins"

def calculate_score(cards):
  """Take a list of cards and return the score calculated from the card """
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def sum(card):
  sum = 0
  for i in card:
    sum = sum + i
  return sum
def play_game():
  user_cards = []
  computer_cards = []
  is_game_over = False
  
  
  for i in range(2):  
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  
  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"  Your Cards: {user_cards}, current score: {user_score}")
    print(f"  Computer's first card is: {computer_cards[0]}")
    
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_should_deal = input("Type 'y' to draw another card, type 'n' to pass: ")
      if user_should_deal == 'y':
        user_cards.append(deal_card())
      else:
        is_game_over = True
  
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  print(f"  Your final hand: {user_cards}, final score: {user_score}")
  print(f"  Computer's final hand: {computer_cards}, final score: {computer_score}")
  print (compare(user_score, computer_score))
  

while input("Do you want to play a game of Blackjack ? Type 'y' or 'n': ") == 'y':
  #clear() 
  print(logo)
  play_game()
  
  
  




