"""
Exercise 07: Area of a Rectangular Room

Create a program that calculates the area of a room.  Prompt
the user for the length and width of the room in feet.  Then
display the rea in both square feet and square meters
"""

def area_of_room():
	flength = input("What is the length of the room in feet? ")
	fwidth = input("What is the width of the room in feet? ")
	
	farea = int(flength)  * int(fwidth)  #Convert to integers.  Area = length * width
	feet_to_met = 0.09290304  #Conversion factor for feet to meters
	marea = farea * feet_to_met  #Area in meters
	
	print("You entered dimension of {} feet by {} feet.".format(flength, fwidth))
	print("The area is: ")
	print("{} square feet.".format(str(farea)))
	print("{} square meters.".format(str(marea)))
	
area_of_room()
