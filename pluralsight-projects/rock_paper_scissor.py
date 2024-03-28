import random
computer_choice = random.choice(['rock', 'paper', 'scissors'])

user_choice = input('Do you want rock, paper or scissors? ')

user_choice = user_choice.lower()

if user_choice == "scissors" or user_choice == "paper" or user_choice == "rock":
 
 if computer_choice == user_choice:
  print("It's a TIE!")
 elif computer_choice == 'scissors' and user_choice == "rock":
  print("You win!The computer had "+ computer_choice + "!")
 elif computer_choice == 'rock' and user_choice == "paper":
  print("You win!The computer had "+ computer_choice + "!")
 elif computer_choice == 'paper' and user_choice == "scissors":
  print("You win!The computer had "+ computer_choice + "!")
 else:
  print("Oh, no! You lost! The computer had "+ computer_choice + "!")
else:
 print("Input error")