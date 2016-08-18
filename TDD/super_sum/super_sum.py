def super_sum(*args):
	total = 0
	total_arg_list = 0
	total_arg_number = 0
	for argument in args:
		if type(argument) == list:
			for element in argument:
				total_arg_list = total_arg_list + element
		else:
			total_arg_number = total_arg_number + argument

	total = total_arg_number + total_arg_list
	return total

print(super_sum(1,2,4,[1,2]))