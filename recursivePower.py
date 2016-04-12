def recursivePower(base, exponent):
	
	exponent = exponent - 1
	
	if exponent == 0:
		return base
	if exponent < 0:
		return 1
	
	return base * recursivePower(base , exponent)

def int_input(prompt):
	answer = raw_input(prompt)
	try: #terminating case
		return int(answer)
	except ValueError: #Recursive Call
		return int_input("That wasn't a number. Try again")

def float_input(prompt):
	answer = raw_input(prompt)
	
	try: #terminating case
		return float(answer)
	except ValueError: #Recursive Call
		return float_input("That wasn't a float. Try again")

######################## Test Cases ########################

print("The power of 10 to the 2nd power is: {}".format(recursivePower(10, 2)))
print("The power of 5 to the 3rd power is: {}".format(recursivePower(5, 3)))
print("The power of 2 to the 4th power is: {}".format(recursivePower(2, 4)))
print("The power of 3 to the 1st power is: {}".format(recursivePower(3, 1)))
print("The power of 26 to the 0th power is: {}".format(recursivePower(26, 0)))