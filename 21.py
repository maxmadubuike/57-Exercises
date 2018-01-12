"""
Exercise 21: Numbers to Names

Write a program that converts a number from 1 to 12 to the corresponding month.
Prompt for a number and display the corresponding calendar month, with 1 being
January and 12 being December.  For any value outside the range, display an
appropriate error message.

"""

from ex_21_func import *

def numbers_to_names():
    greeting()
    number = entered_number()
    month = match(number)
    output(month)

numbers_to_names()
