def my_sum(x, y):
	'''
	Takes in two number (x and y) and returns
	the sum of the two numbers 
	'''
	if type(x) == str or type(y) == str:
		raise TypeError
	else:
		return x + y