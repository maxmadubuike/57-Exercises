'''
Exercise 27: Validating Inputs

Write a program that prompts for the first name, last name, employee ID, and
Zip code.  Ensure the input is valid according to these rules:
    - The first name must be filled in.
    - The last name must be filled in.
    - The first and last names must be at least two characters long
    - An employee  ID is in the format AA-1234.  So, two letters, a hyphen, and
      four numbers.
    - The ZIP code must be a number.

Display the appropriate error messages on incorrect data.

Constraints
    - Create a function for each type of validation you need to write.  Then
        create a validateInput function that takes in all of the input data
        and invokes the specific validation functions.
    - Use a single output statement to display the outputs.
'''

from ex_27_func import *

def main():
    greeting()
    first_name = first_name_input()
    last_name = last_name_input()
    zipcode = zip_code_input()
    employeeID = employeeID_input()
	
    validateInput(fn=first_name, ln=last_name, zc=zipcode, eid=employeeID)

main()
