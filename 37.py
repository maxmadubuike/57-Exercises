'''
Exercise 37: Password Generator

Create a program that generates a secure password.  Prompt the user for the minimum
length, the number of special characters, and the number of numbers.  Then generate a
password for the user using these inputs.

Constraints:
  - Use lists to store the characters you'll use to generate the passwords.
  - Add some randomness to the password generation
'''

import random

def greeting():
  print("Exercise 37:  Password Generator")
  
def minPasswordLength():
  minLengthraw = input("What's the minimum length? ")
  if minLengthraw.isnumeric():
    minLength = int(minLengthraw)
    return minLength
  else:
    print("Please enter a number.")
    minPasswordLength()
  
def specialChars():
  specialCharsraw = input("How many special characters? ")
  if specialCharsraw.isnumeric():
    numofspecialChar = int(specialCharsraw)
    return numofspecialChar
  else:
    print("Please enter a number.")
    specialChars()
    
def numofNums():
  numofNumsraw = input("How many numbers? ")
  if numofNumsraw.isnumeric():
    numofNumbs = int(numofNumsraw)
    return numofNumbs
  else:
    print("Please enter a number.")
    numofNums()
  
def passwordCreator(l, c, n):
  
  # Create alphabet list of lowercase letters
  alphabet = []
  for letter in range(97,123):
    alphabet.append(chr(letter))
  # Create alphabet list of uppercase letters
  for letter in range(65, 91):
    alphabet.append(chr(letter))
    
  # Create list of numbers  
  numbers = []
  for num in range(0,10):
    numbers.append(num)
    
  # List of special characters
  specialcharacters = "!@#$%^&"
  
  # Password Generator
  newPassword = []
  lengthCounter = 0
  numberCounter = 0
  specialCharacterCounter = 0
  alphaCounter = 0
  while numberCounter < n:
    randomNumber = random.choice(numbers)
    newPassword.append(randomNumber)
    numberCounter += 1
    lengthCounter += 1
    alphaCounter += 1
  while specialCharacterCounter < c:
    randomCharacter = random.choice(specialcharacters)
    newPassword.append(randomCharacter)
    specialCharacterCounter += 1
    lengthCounter += 1
    alphaCounter += 1
  while alphaCounter < l:
    letter = random.choice(alphabet)
    newPassword.append(letter)
    alphaCounter += 1

  # Password Presentation Prep
  strNewPasswordListItem = []
  for item in newPassword:
    a = str(item)
    strNewPasswordListItem.append(a)
  finishedPassword = "".join(strNewPasswordListItem)
  print(finishedPassword)
  
  
def main():
  greeting()
  length = minPasswordLength()
  numofchars = specialChars()
  numofNumbers = numofNums()
  passwordCreator(l=length, c=numofchars, n=numofNumbers)
  
main()
  
  
  
  
  
  
  
  
  
  
  
  
  
  
