def super_sum(*args):
	total = 0
	total_arg_list = 0
	total_arg_number = 0
	string_error_message = 'your list contains a string'
	for argument in args:
		if type(argument) == list:
			for element in argument:
				if type(element) is not int:
					return string_error_message
				total_arg_list = total_arg_list + element
		else:
			if type(argument) is not int:
				return string_error_message
			total_arg_number = total_arg_number + argument

	total = total_arg_number + total_arg_list
	return total

print(super_sum(50,20,[10,10,10]))