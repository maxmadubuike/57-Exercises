"""
Exercise 10: Self-Checkout

Create a simple self-checkout system.  Prompt for the prices and quantities of three items.  Calculate the subtotal 
of the items.  Then calculate the tax using a tax rate of 5.5%.  Print out the line items with the quantity and 
total, and then print out the subtotal, tax amount, and total.

Contraints:
Keep the input, processing, and output parts of your program seperate.  Collect the input, do the math operations, 
and string building, and then print out the output.
Be sure you explicitly convert input to numerical data before doing calculations.
"""

def get_items():
  a1p = input("Enter the price of item 1: ")
  a1q = input("Enter the quantity of item 1: ")
  item1p = float(a1p)
  item1q = float(a1q)
  
  a2p = input("Enter the price of item 2: ")
  a2q = input("Enter the quantity of item 2: ")
  item2p = float(a2p)
  item2q = float(a2q)
  
  a3p = input("Enter the price of item 3: ")
  a3q = input("Enter the quantity of item 3: ")
  item3p = float(a3p)
  item3q = float(a3q)
  
  subtotal = (item1p * item1q) + (item2p * item2q) + (item3p * item3q)
  tax = subtotal * 0.055
  total = subtotal + tax
  print("Subtotal: ${}".format(subtotal))
  print("Tax: ${}".format(tax))
  print("Total: ${}".format(total))

 get_items()
