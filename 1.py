"""
Excercise 1: Saying Hello

Create a program that prompts for your name and prints a greeting using your name
"""

a = input("What is your name?")
print("Hello " + a + ", nice to meet you!")

# Challenges

"""Write a new version of the program without using any variables"""
print("Hello {}, nice to meet you!".format(input("What is your name?\n")))
