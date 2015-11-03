import numpy as np 
import matplotlib.pyplot as plt

# function used to compute the Mandelbrot fractal and save the result to an image
def compute_mandelbrot():
	N_max = 50
	some_threshold = 50

	grid_interval = 1000

	# construct the grid 
	x = np.linspace(-2, 1, grid_interval)
	y = np.linspace(-1.5, 1.5, grid_interval)

	c = x[:, np.newaxis] + 1j*y[np.newaxis, :]

	# do the iteration 
	z = c 
	for v in range(N_max):
		with np.errstate(all = "ignore"): # catches overflow and invalid value errors 
			z = z**2 + c 
		
	with np.errstate(all = "ignore"): # catches overflow and invalid value errors 

		# form a 2-D boolean mask 
		mask = (abs(z) < some_threshold)

	# save the result to an image
	plt.imshow(mask.T, extent = [-2, 1, -1.5, 1.5])
	plt.gray()
	plt.savefig('mandelbrot.png')


