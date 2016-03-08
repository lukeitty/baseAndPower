#Author: Luke Ittycheria
#Date March 7th 2016
#Program: Takes a base input and takes the power of another input



def power (base, exponent):# Function of the Actual calculating of base to the power
	if exponent == 0:
		base = 1
	else:
		for number in range(exponent-1):
			base *= base
    	
	return base


base = raw_input('Please Enter a Base: ')
exponent = raw_input ('Please Enter an Exponent: ')
base = int(base)
exponent = int(exponent)
    
calculation = power(base, exponent)
print("Your result is: " + str(calculation))


