import unittest
from super_sum import super_sum

class SuperSumTest(unittest.TestCase):

	def test_normal_list(self):
		self.assertEqual(10, super_sum(7,3))
		self.assertEqual(4, super_sum(2,2))
		self.assertEqual(6, super_sum(4,2))

	def test_normal_list2(self):
		self.assertEqual(20, super_sum(15,5))
		self.assertEqual(30, super_sum(21,9))
		self.assertEqual(25, super_sum(19,6))


	def test_nested_list(self):
		self.assertEqual(10, super_sum([1,2,3,[2,2]]))
		self.assertEqual(15, super_sum([4,5,[4,2]]))
		self.assertEqual(60, super_sum([10,20,[30]]))

	def test_nested_list2(self):
		self.assertEqual(100, super_sum([50,[20,10,10,10]]))
		self.assertEqual(200, super_sum([150, [10,30,10]]))
		self.assertEqual(150, super_sum([75,[75]]))

	def test_nested_and_normal(self):
		self.assertEqual(10, super_sum(1,2,3,[2],2))
		self.assertEqual(40, super_sum(1,2,3,4,[10],10,5,5))
		self.assertEqual(50, super_sum(10,20,[15],[10],5))