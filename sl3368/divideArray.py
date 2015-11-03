import numpy as np

# the function used to divides each column element-wise 
def divideArray():

	a = np.arange(25).reshape(5, 5)

	# create an empty array with the same shape as array a
	empty_a = np.empty(25).reshape(5, 5) 
	b = np.array([1., 5, 10, 15, 20]) 

	# for loop 
	for i in range(5):
		empty_a[:, i] = np.divide(a[:, i], b)

	# divided array 
	result = empty_a

	return result

