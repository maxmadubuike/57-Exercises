'''
Exercise 38: Filtering Values

Create a program that prompts for a list of nubmers, sperated by spaces.
Have the program print out a new list containing only the even nubmers.

'''

def greeting():
  print("Exercise 38: Filtering Values")
  
def numInput():
  chosenNum = input("Enter a list of numbers, separated by spaces: ")
  chosenNumList = []
  nums = chosenNum.split()
  for a in nums:
    if int(a) % 2 == 0:
      chosenNumList.append(a)
  print("The even numbers are {}".format(" ".join(chosenNumList)))
    
numInput()
