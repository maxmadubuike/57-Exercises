def add_ops(c, d):
	num1 = str(c)
	num2 = str(d)
	num3 = str(c + d)
	print(num1 + " + " + num2 + " = " + num3)

def sub_ops(c, d):
	num1 = str(c)
	num2 = str(d)
	num3 = str(c - d)
	print(num1 + " - " + num2 + " = " + num3)
	
def mult_ops(c, d):
	num1 = str(c)
	num2 = str(d)
	num3 = str(c * d)
	print(num1 + " * " + num2 + " = " + num3)

def div_ops(c, d):
	num1 = str(c)
	num2 = str(d)
	try:
		c / d
	except ZeroDivisionError:
		print("Division Error:  Cannot divide by zero!")
	else:
		num3 = str(c / d)
		print(num1 + " / " + num2 + " = " + num3)
