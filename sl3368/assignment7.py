'''
Author: Shixin Li 

This is the main program that generates answers for assignment7
'''

from arrayGenerator import *
from divideArray import *
from randomArray import *
from Mandelbrot import *

# main function 
def main():

	# create an ArrayGenerator object and call the functions 
	print "Question1 initial 2-D array:"
	question_1 = ArrayGenerator()
	print question_1.added_array

	print "Question1 part a:"
	print question_1.rowArray() # question1 part a

	print "Question1 part b:"
	print question_1.colArray() # question1 part b

	print "Question1 part c:"
	print question_1.recArray() # question1 part c

	print "Question1 part d:"
	print question_1.restrictedArray() # question1 part d

	# question 2
	print "Question2:"
	print divideArray()

	# question 3
	print "Question3:"
	print randomArray()

	# question 4 
	print "Question4: the plot will be saved"
	compute_mandelbrot()

if __name__ == "__main__":
	try:
		main()
	except EOFError:
		pass
	except TypeError:
		pass
	except ZeroDivisionError:
		pass
	except ArithmeticError, OverflowError:
		pass
	except KeyboardInterrupt, ValueError:
		pass 

