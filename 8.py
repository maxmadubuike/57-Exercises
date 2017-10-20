"""
Exercise 8:  Pizza Party
Write a program to evenly divide pizzas.  Prompt for the numberf of people, the number of pizzas, and the number of slices per pizza.  Ensure that the number of pieces comes out even.  Display the number of pieces of pizza each person should get.  If there are leftovers, show the number of leftover pieces.
"""

def pizza_party():
  num_of_people = input("How many people? ")
  num_of_pizzas = input("How many pizzas? ")
  
  slices_per_pizza = 8
  print("\nEach pizza has {} slices.\n".format(slices_per_pizza))
  
  
  #Print the number of people and pizzas.
  print("{} people with {} pizzas".format(num_of_people, num_of_pizzas))
  
  #Print how many slices each person gets using only whole numbers.
  total_num_of_slices = int(num_of_pizzas) * slices_per_pizza
  print("Each person gets {} slices of pizza.".format(total_num_of_slices//int(num_of_people)))
  
  #Use modulus to return leftover pieces.
  print("There are {} leftover pieces".format(total_num_of_slices%int(num_of_people)))
  
  
"""
Challenge.  
Revise the program to ensure inputs are entered as numeric values.  Don't allow the user to proceed if the value entered is not numeric.

Alter the output so it handles pluralization properly.
"""

def pizza_party_challenge():
  num_of_people = input("How many people? ")
  num_of_pizzas = input("How many pizzas? ")
  
  try:
    int(num_of_people), int(num_of_pizzas)
  except ValueError:
    print("You must enter a number.")
    pizza_party_challenge()
  
  slices_per_pizza = 8
  print("\nEach pizza has {} slices.\n".format(slices_per_pizza))
  
  #Print how many slices each person gets using only whole numbers.
  total_num_of_slices = int(num_of_pizzas) * slices_per_pizza
  slice_per_person = total_num_of_slices // int(num_of_people)
  if slice_per_person <= 1:
    print("Each person gets {} slice of pizza".format(slice_per_person))
  else:
    print("Each person gets {} slices of pizza.".format(slice_per_person))
    
  #Print leftover slices
  leftover_slices = total_num_of_slices%int(num_of_people)
  if leftover_slices == 0:
    print("There are {} slices of pizza left.".format(leftover_slices))
  elif leftover_slices == 1:
    print("There is {} slice of pizza left.".format(leftover_slices))
  else:
    print("There are {} slices of pizza left.".format(leftover_slices))
    
  
    
  
    
