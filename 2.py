def number_of_characters():
	a = input("What is the input string?\n")
	if a == "":
		print("You must enter a string")
	else:
		print(a + " has " + str(len(a)) + " characters.")
			
number_of_characters()


