"""
Exercise 18: Temperature Converter

Create a program that converts temperatures from Fahrenheit to Celcius or from Celsius to Fahrenheit.
Prompt for the starting temperature.  The program should prompt for the type of conversion and then
perform the conversion.

"""

from ex_18_func import *

def temperature_converter():
	greeting()
	selection = selection_input()
	if selection == 'c':
		temp = fah_to_cel()
	else:
		temp = cel_to_fah()
	

temperature_converter()
	
