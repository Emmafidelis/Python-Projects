import random

ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'
emojis = { ROCK: '🪨', PAPER: '📰', SCISSORS: '✂️' }
choices = (tuple(emojis.keys()))

def get_user_choice():
  while True:
    user_choice = input('Rock, paper, or scissors? (r/p/s): ').lower()
    if user_choice in choices:
      return user_choice
    else:
      print('Invalid choice!')

def display_choices(user_choice, computer_choice):
  print(f'you chose {emojis[user_choice]}')
  print(f'computer chose {emojis[computer_choice]}')

def determine_winner(user_choice, computer_choice):
  if user_choice == computer_choice:
    print('Tie!')
  elif (
    (user_choice == ROCK and computer_choice == SCISSORS) or
    (user_choice == SCISSORS and computer_choice == PAPER) or
    (user_choice == PAPER and computer_choice == ROCK)):
    print('Yow win')
  else:
    print('You lose')

def play_game():
  while True:
    user_choice = get_user_choice()

    computer_choice = random.choice(choices)

    display_choices(user_choice, computer_choice)

    determine_winner(user_choice, computer_choice)

    should_continue = input('Continue? (y/n): ')
    if should_continue == 'n':
      break

play_game()