import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import os

#is a function that takes the filename as argument and displays it.
def processImage(imgFileName):
	path = os.path.join('C:/Users/Prashant/desktop/try/images/', imgFileName)
	image = mpimg.imread(path)
	plt.imshow(image)
	plt.axis('off')
	plt.show()

if(__name__ == '__main__'):
	processImage()