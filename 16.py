"""
Exercise 16: Legal Driving Age

Write a program that asks the user for their age and
compare it to the legal driving age of sixteen.  If the
user is sixteen or older, then the program should
display "You are old enough to legally drive."  If the
user is under sixteen, the program should display
"You are not old enough to legally drive."
"""

import datetime

def legal_driving_age():
	on  = True
	while on == True:
		now = datetime.datetime.now()
		year = now.year
		minimum_driving_age = 16
		birthyear_to_drive = year - minimum_driving_age
		
		print("Welcome to the driving age calculator.\nPress 'q' to quit anytime.")
		input_age = input("What is your age?\n")
		if input_age == 'q':
			on = False	
			break
					
		try:
			age = int(input_age)
		except ValueError:
			print("\nSorry, must enter a number.")
		else:
			year_of_birth = year - age
			if age <= 0:
				print("\nMust enter a non-zero number.\n")	
			elif year_of_birth <= birthyear_to_drive:
				print("\nYou are old enough to legally drive\n")
			else:
				print("\nYou are not old enough to legally drive.\n")


legal_driving_age()
