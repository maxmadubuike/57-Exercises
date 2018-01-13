'''
Exercise 35:  Picking a Winner

Create a program that picks a winner for a contest or prize drawing.
Prompt for names of contestants until the user leaves the entry blank.
Then randomly select a winner.

Constraints:
  - Use a loop to capture user input into an array.
  - Use a random number generator to pluck a value from the array.
  - Don't include a blank entry in the array.
  
'''

import random

def greeting():
  print("Welcome to Exercise 35: Picking a Winner")
  
def main():
  greeting()
  contestants = []
  while True:
    name = input("Enter a name: ")
    if name != '':
      contestants.append(name)
    else:
      winner = random.choice(contestants)
      print("The winner is... {}.".format(winner))
      return False

main()
