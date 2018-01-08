'''
Execise 29: Handling Bad Input

Write a quick calculator that prompts for the rate of return on an 
investment and calculates how many years it will take to double your
 investment.
 
Constraints
	- Don't allow the user to enter 0.
	- Don't allow non-numeric values.
	- Use a loop to trap bad input, so you can ensure that the user enters
		valid values.
		
'''

def main():
	print("Welcome to Exercise 29: Handling Bad Input")
	while True:
		rate = input("What is the rate of return? ")
		if rate.isnumeric():
			rate_clean = int(rate)
			if rate_clean == 0:
				print("Sorry, that is not a valid input.\n")
				return main()
			else:
				years = 72 / rate_clean
				print("It will take {} years to double your initial investment.".format(years))
				break
		else:
			print("Sorry, that is not a valid input.\n")
			return main()
	
main()
