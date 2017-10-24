"""
Exercise 9: Paint Calculator

Calculate the gallons of paint needed to paint the ceiling of a room.  Prompt for the length and width, and assume one gallon covers 350 square feet.  Display the number of gallons needed to paint the ceiling as a whole number.

Constraints:
Use a constant to hold the conversion rate.
Ensure that you round up to the next whole gallon.
"""

import math

def paint_calculator():
  length = input("What is the length? ")
  try:
    int_length = int(length)
  except ValueError:
    print("You must enter a number")
  
  
  width = input("What is the width? ")
  try:
    int_width = int(width)
  except ValueError:
    print("You must enter a number")
    
  gallons_per_square_foot = 350
  area_of_ceiling = int_width * int_length
  gallons_needed = area_of_ceiling / gallons_per_square_foot
  
  print("You will need {} gallons of paint to cover {} square feet.".format(math.ceil(gallons_needed), area_of_ceiling))
  
  
