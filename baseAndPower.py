#Author: Luke Ittycheria
#Date March 7th 2016
#Program: Base and Power Program



def power (base, exponent):# Function of the Actual calculating of base to the power
	if exponent == 0: #If the exponent is 0 
		base = 1
	else:
		for number in range(exponent-1): #looping through multiplication
			base *= base
    	
	return base #return the new value

############################## MAIN PROGRAM  ################################

#Prompts user for a base int and a exponent int
base = raw_input('Please Enter a Base: ')
exponent = raw_input ('Please Enter an Exponent: ')

#Changes base and power to be ints
base = int(base)
exponent = int(exponent)

#Starting the function and printing to screen    
calculation = power(base, exponent)
print("Your result is: " + str(calculation))



	


