# Print sum of numbers up to number.

def magic_sum(number):
	
	if number < 0:
		return 'Error! Input again: '
	sum = 0
	
	for i in range(number + 1):
		sum += number
		return sum
		
print magic_sum(5)