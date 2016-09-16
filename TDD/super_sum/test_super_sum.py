import unittest
from super_sum import super_sum

class SuperSumTest(unittest.TestCase):

	def test_normal_list(self):
		'''Test a normal list i.e. 1,2,3,4,5 should return 15'''
		self.assertEqual(10, super_sum(7,3), msg='should return 10')
		self.assertEqual(4, super_sum(2,2), msg='should return 4')
		self.assertEqual(6, super_sum(4,2), msg='should return 6')

	def test_normal_list2(self):
		''' Test normal list with large values 10,20,30 should return 60'''
		self.assertEqual(20, super_sum(15,5), msg='should return 20')
		self.assertEqual(30, super_sum(21,9), msg='should return 30')
		self.assertEqual(25, super_sum(19,6), msg='should return 25')
	
	def test_normal_list3(self):
		''' Test normal list with large values 10,20,30 should return 60'''
		self.assertEqual(20, super_sum(15,5), msg='should return 20')
		self.assertEqual(30, super_sum(21,9), msg='should return 30')
		self.assertEqual(25, super_sum(19,6), msg='should return 25')


	def test_nested_list(self):
		''' Test a nested list with small values: 1,2,3,[4,5] should return 15'''
		self.assertEqual(10, super_sum(1,2,3,[2,2]), msg='should return 10')
		self.assertEqual(15, super_sum(4,5,[4,2]), msg='should return 15')
		self.assertEqual(60, super_sum(10,20,[10,20]), msg='should return 60')

	def test_nested_list2(self):
		'''Test a nested list with large values: 50,30,[10,20,30] should return 130 '''
		self.assertEqual(100, super_sum(50,20,[10,10,10]), msg='should return 100')
		self.assertEqual(200, super_sum(150,10,[30,10]), msg='should return 200')
		self.assertEqual(150, super_sum(75,75), msg='should return 150')

	def test_nested_and_normal(self):
		''' Test a nested plus normal list with mixed size values: '''
		self.assertEqual(10, super_sum(1,2,3,[2],2), msg='should return 10')
		self.assertEqual(40, super_sum(1,2,3,4,[10],10,5,5), msg='should return 40')
		self.assertEqual(60, super_sum(10,20,[15],[10],5), msg='should return 60')

	def test_list_has_invalid_data(self):
		self.assertEqual('your list contains a string', super_sum(1,2,3,'4'), msg='invalid data in your list')
		self.assertEqual('your list contains a string', super_sum(1,2,3,[3,'4']), msg='invalid data in your list')


if __name__ == '__main__':
	unittest.main()
