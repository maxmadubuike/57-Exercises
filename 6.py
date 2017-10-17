"""
Excercise 6: Retirement Calculator

Create a program that determines how many years you have left until
retirement and the year you can retire.  It should prompt for your
current age and the age you want to retire and display the output.
"""
import datetime

def retirement_calculator():
	curr_age = input("What is your current age? ")
	ret_age = input("At what age would you like to retire? ")
	
	a = int(curr_age)
	b = int(ret_age)
	c = b - a
	print("You have " + str(c) + " years until you can retire.")

	t = datetime.date.today()  
	u = t.year  
	
	v = u + c
	
	print("The current year is " + str(u) + ", so you can retire in " + str(v)  + ".")
	
retirement_calculator()

