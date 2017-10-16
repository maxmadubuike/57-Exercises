#5: Simple Math
#Write a program that prompts for two numbers.  Print the sum, difference, product, and quotient of those numbers.

import sys
from basic_ops import  *

def simple_math():
	a = input("What is the first number?\t")
	try:
		c = int(a)
	except ValueError:
		print("You must enter a number")
	
	if c < 0:
		print("Must enter a positive number.")
		sys.exit()
	
	b = input("What is the second number?\t")	
	try:
		d = int(b)
	except ValueError:
		print("You must enter a number")
	if d < 0:
		print("Must enter a positive number.")
		sys.exit()

	
	if c >= 0 and d >= 0:
		add_ops(c, d)
		sub_ops(c, d)
		mult_ops(c, d)
		div_ops(c, d)


	
simple_math()
