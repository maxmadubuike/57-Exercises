"""
Exercise 15: Password Validation

Create a simple program that validates user login credentials.
The program must prompt the user for a username and
password.  The program should compare the password given
by the user to a known  password.  If the password matches,
the program should display "Welcome!"  If it doesn't match,
the program should display "I don't know you."
"""

def password_validation():
	user_input = input("What is the password? ")
	password = '1234'
	
	if user_input == password:
		print("Welcome!")
	else:
		print("I don't know you.")
		
password_validation()
