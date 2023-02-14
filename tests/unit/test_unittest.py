# unittest way of testing the add_one function
import unittest

# function to test
def add_one(num:int):
		return num + 1

# class that has tests
class testFunction(unittest.TestCase):
	def test_add_one(self):
		test_num = 1
		expected = 2
		self.assertEqual(add_one(test_num), expected, "Raise Error")
	
	@unittest.expectedFailure
	def test_add_one_fail(self):
		test_num = 2
		expected = 2
		self.assertEqual(add_one(test_num), expected, "3 != 2")

if __name__ == '__main__':
    unittest.main()