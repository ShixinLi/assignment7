import numpy as np

'''The class for the Question 1: generate different arrays'''

class ArrayGenerator():

	# Constructor 
	def __init__(self):

		initial_array = np.arange(1, 6, 1)
		initial_array = initial_array[:, np.newaxis]

		add_array = np.array([0,5,10])

		self.added_array = initial_array + add_array

	# function used to generate a new array containing the 2nd and 4th rows
	def rowArray(self):
		row_2 = self.added_array[1, :]
		row_4 = self.added_array[3, :]

		row_array = np.array([row_2, row_4])

		return row_array

	# function used to generate a new array that contains the 2nd column
	def colArray(self):
		col_2 = self.added_array[:, 1:2]
		col_array = np.array(col_2)

		return col_array

	# function used to generate a new array that contains all the elements
	# from 2nd row to 4th row 
	def recArray(self):
		rec_array = self.added_array[[1, 2, 3], :]

		return rec_array

	# function used to generate a new array that contains only elements with
	# values that are between 3 and 11
	def restrictedArray(self):
		restricted_array = self.added_array[abs(self.added_array - 7) <= 4]
		restricted_array_2D = np.array([restricted_array])

		return restricted_array_2D

