import unittest
from unittest import TestCase
from arrayGenerator import *
from divideArray import *
from randomArray import *
from Mandelbrot import *

''' this class will test answers in different modules'''

class AssignmentTest(TestCase):

	def setUp(self):
		pass

	# this function will test question 1 
	def test_arrayGenerator(self):
		actual = ArrayGenerator()
		# part a
		test_a = np.array([[2, 7, 12], [4, 9, 14]])

		actual_a = actual.rowArray()
		self.assertTrue(np.array_equal(test_a, actual_a))

		# part b
		test_b = np.array([[6], [7], [8], [9], [10]])
		actual_b = actual.colArray()
		self.assertTrue(np.array_equal(test_b, actual_b))

		# part c
		test_c = np.array([[2, 7, 12], [3, 8, 13], [4, 9, 14]])
		actual_c = actual.recArray()
		self.assertTrue(np.array_equal(test_c, actual_c))

		# part d 
		test_d = np.array([[6, 11, 7, 3, 8, 4, 9, 5, 10]])
		actual_d = actual.restrictedArray()
		self.assertTrue(np.array_equal(test_d, actual_d))

	# test question 2
	def test_divideArray(self):
		actual = divideArray()

		self.assertEqual(1.6, actual[1, 3])
		self.assertEqual(1.1, actual[2, 1])
		self.assertEqual(1.3, actual[2, 3])
		self.assertEqual(2., actual[0, 2])

	# test question 3
	def test_randomArray(self):
		actual = randomArray()

		test_originalArray = np.random.rand(10,3)
		test_changedArray = np.argsort(abs(test_originalArray - 0.5))
		test_fancyIndex = test_changedArray[:, 1]
		test_final_array = test_originalArray[np.arange(0,10), test_fancyIndex]
		for i in range(10):
			if abs(test_final_array[i] - 0.5) >= abs(actual[i] - 0.5):
				self.assertTrue

if __name__ == "__main__":
	unittest.main()
	

