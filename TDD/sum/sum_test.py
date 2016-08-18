import unittest
from sum import my_sum

class MySumTests(unittest.TestCase):

	def setUp(self):
		pass

	def test_sum_of_numbers(self):
		'''
		Test sum of digits/numbers
		'''
		self.assertEqual(30, my_sum(10,20), msg='10, 20 should be equal to 30')
		self.assertEqual(10, my_sum(6,4))
		self.assertEqual(20, my_sum(2,18))

	def test_none_numbers(self):
		'''
		Assert throwing of exception when it's a non-number
		'''
		self.assertRaises(TypeError, my_sum, 'arnold', 7, msg='Expected TypeError')
		self.assertRaises(TypeError, my_sum, 10, 'okoth', msg='Expected TypeError')


if __name__ == '__main__':
	unittest.main()

# TDD Assignment
# Write a _variadic_ function super sum that takes in any number of 
# numbers or list of numbers and sums them up

# Write at least 5 test cases for your function, before 