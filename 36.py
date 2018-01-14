'''
Exercise 36: Computing Statistics

Write a program that prompts for response times from a website in milliseconds.
It should keep asking for values until the user enters "done".

The program should print the average time (mean), the minimum time, the maximum
time, and the standard deviation.

Constraints:
  - Use loops and arrays to perform the input and mathematical operations.
  - Be sure to exclude the "done" entry from the array of inputs
  - Keep the input seperate form the processing and output.
  
'''

def greeting():
  print("Exercise 36: Computing Statistics")
  
def time_inputs():
  times = []
  while True:
    time_string = input("Enter a number: ")
    if time_string != 'done':
      time = int(time_string)
      times.append(time)
    else:
      return times
      
def minmax(*times):
  largestNumber = 0
  smallestNumber = 0
  
  # Max
  for a in times:
    if a > largestNumber:
      largestNumber = a
      smallestNumber = a
      
  # Min
  for b in times:
    if b < smallestNumber:
      smallestNumber = b

  print("The maximum is {}.".format(largestNumber))
  print("The minimum is {}.".format(smallestNumber))
  
  
def averageCalc(*times):
  total = 0
  for a in times:
    total += a
  average = total // len(times)
  print("The average is {}.".format(average))
  return average

def standardDevCalc(*times, average):
  squared_times = []
  squaredTotal = 0
  for a in times:
    right = a - average
    rightsquared = right * right
    squared_times.append(rightsquared)
    squaredTotal += rightsquared
  stdev_av = squaredTotal // len(squared_times)
  stddev = stdev_av ** (1 / 2)
  print("The standard deviation is {}.".format(stddev))
    
    
  
def main():
  greeting()
  times = time_inputs()
  minmax(*times)
  average = averageCalc(*times)
  standardDevCalc(*times, average=average)
  
main()
