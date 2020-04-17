# Create a calculator function
# The function should accept three parameters:
# first_number: a numeric value for the math operation
# second_number: a numeric value for the math operation
# operation: the word 'add' or 'subtract'
# the function should return the result of the two numbers added or subtracted
# based on the value passed in for the operator
#
# Test your function with the values 6,4, add 
# Should return 10
#
# Test your function with the values 6,4, subtract 
# Should return 2
# 
# BONUS: Test your function with the values 6, 4 and divide 
# Have your function return an error message when invalid values are received

def calc(number1, number2, op):
	if op == 'add':
		return number1 + number2
	elif op == 'subtract':
		return number1 - number2
	elif op == 'divide':
		if number2 == 0:
			print('\nCannot divide by 0!!')
			return 0
		else:
			return number1 / number2
	else:
		print('Invalid operation!!\n')
		return 0
		

sum = calc(6, 4, 'add')		#Give input here
print('sum = ' + str(sum))
print('-------------------------')

diff = calc(6, 4, 'subtract')	#Give input here
print('\ndiff = ' + str(diff))
print('-------------------------')

quo = calc(6, 4, 'divide')		#Give input here
print('\nQuo = ' + str(quo))
print('-------------------------')

quo = calc(6, 0, 'divide')		#Give input here
print('\nQuo = ' + str(quo))
print('-------------------------')



