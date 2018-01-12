"""
Exercise 02: Counting the Number of Characters

Create a program that prompts for an input string and displays output that shows the input string and the number of
characters the string contains.

Constraints:
Besure the output contains the original string.
Use a simple output statement to construct the output.
Use a built-in function of the programming language to determine the length of the string.
"""

def number_of_characters():
	a = input("What is the input string?\n")
	if a == "":
		print("You must enter a string")
	else:
		print(a + " has " + str(len(a)) + " characters.")
			
number_of_characters()
