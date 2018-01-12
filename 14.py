"""
Exercise 14: Tax Calculator

Write a simple program to compute the tax on an order amount.
The program should prompt for the order amount and the state.
If the state is "WI," then the order must be charged 5.5% tax. 
The program should display the subtotal, tax, and total for
Wisconsin residents but diplay just the total for non-residents.
"""

def tax_calculator():
	order_amount = input("What is the order amount? ")
	order_state = input("What is the state? ")
	tax_state = ['wi', 'wisconsin']
	flt_tax_rate = float(1.055)
	
	flt_order_amount = float(order_amount)
	total = flt_order_amount * flt_tax_rate 
	
	if  order_state.lower() in tax_state:
		print("The subtotal is ${}.".format(order_amount))
		print("The tax is ${}.".format(flt_order_amount * 0.055))
		print("The total is ${}.".format(round(total, 2)))
	else:
		print("The subtotal is ${}.".format(flt_order_amount))
		print("The tax is $0.")
		print("The total is ${}.".format(round(total, 2)))
			
tax_calculator()
