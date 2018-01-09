'''
Exercise 30: Multiplication Table

Create a program that generates multiplication tables for the numbers 0 through
12.

Constraints:
Use a nested loop to complete this program.

'''
from ex_30_func import *

def main():
	for a in range(13):
		for b in range(1,13):
			print("{} * {} =  {}".format(a, b, a*b))
		
main()
