'''
Exercise 33: Magic 8 Ball

Create a Magic 8 Ball game that prompts for a question and then displays either "Yes," "No," "Maybe," or 
"Ask again later."

Constraint:
  The value should be chosen randomly using a pseudo random number generator.  Store the possible choices
  in a list and select one at random.
'''

import random

def greeting():
  print("Welcome to Exercise 33: Magic 8 Ball")

def game():
  greeting()
  answers = ["Yes", "No", "Maybe", "Ask again later"]

  question = input("What's your question?")
  
  print(random.choice(answers))
  
game()
