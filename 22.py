"""
Exercise 22: Comparing Numbers

Write a program that asks for three numbers.  Check first to see that all
numbers are different.  If they're not different, then exit the program.
Otherwise, display the largest number of the three.

Constraint:
Write the algorithm manually.  Don't use a built-in function for finding the
largest number in a list.

"""

import sys

def comparing_numbers():
    largestnumber = 0

    raw_number1 = input("Please enter the first number:\t")
    number1 = int(raw_number1)
    if number1 > largestnumber:
        largestnumber = number1

    raw_number2 = input("Please enter the second number:\t")
    number2 = int(raw_number2)
    if number2 == number1:
        sys.exit()
    elif number2 > largestnumber:
        largestnumber = number2

    raw_number3 = input("Please enter the third number:\t")
    number3 = int(raw_number3)
    if number3 == number1 or number3==number2:
        sys.exit()
    elif number3 > largestnumber:
        largestnumber = number3

    print("The largest number is {}.".format(largestnumber))
    return largestnumber


comparing_numbers()
