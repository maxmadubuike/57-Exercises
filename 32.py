'''
Exercise 32: Guess the Number Game

Prompt for the difficulty level, and then start the game.  The computer picks a
random number in that range and prompts the player to guess that number.  Each
time the playher guesses, the computer should give the player a hint as to
whether the number is too high or too low.  The computer should also keep track
of the number of guesses.  Once the player guesses the correct number, the
computer should present the number of guesses and ask if the player would like
to play again.

Constraints:
Don't allow any non-numeric data entry.
During the game, count non-numeric entries as wrong guesses.

'''
from ex_32_func import *

def main():
  greeting()
  difficulty = difficulty_setting()
  computer_selection = computer_guess(difficulty)
  print("I have my guess.  What is your guess? ", end='')
  numberOfGuesses = 1
  while True:
    guess_input = input('')
    if guess_input.isnumeric():
      guess = int(guess_input)
      if guess > computer_selection:
        numberOfGuesses += 1
        print("Too high.  Guess again. ", end='')
      elif guess < computer_selection:
        numberOfGuesses += 1
        print("Too low.  Guess again. ", end='')
      elif guess == computer_selection:
        print("You got it in {} guesses!".format(numberOfGuesses))
        again = input("Would you like to play again? ")
        if again == 'y':
          main()
        elif again != 'y':
          return False
    else:
      numberOfGuesses += 1
      print("Please enter a number and try again. ")


main()
