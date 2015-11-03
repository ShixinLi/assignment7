import numpy as np

# function used to print out a 1-D array containing 10 values,
# each value is the number closest to 0.5 from the corresponding 
# row of the original array
def randomArray():

	originalArray = np.random.rand(10,3)

	changedArray = np.argsort(abs(originalArray - 0.5))

	fancyIndex = changedArray[:, 0]

	final_array = originalArray[np.arange(0,10), fancyIndex]

	return final_array
