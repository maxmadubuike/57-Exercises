'''
Exercise 37: Password Generator

Create a program that generates a secure password.  Prompt the user for the minimum
length, the number of special characters, and the number of numbers.  Then generate a
password for the user using these inputs.

Constraints:
  - Use lists to store the characters you'll use to generate the passwords.
  - Add some randomness to the password generation
'''

from ex_37_func import *

def main():
  greeting()
  length = minPasswordLength()
  numofchars = specialChars()
  numofNumbers = numofNums()
  passwordCreator(l=length, c=numofchars, n=numofNumbers)

main()
