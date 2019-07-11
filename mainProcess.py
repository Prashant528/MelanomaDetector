import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import os
import preprocess

#is a function that takes the filename as argument and displays it.
def processImage(imgFileName):
	path = os.path.join('C:/Users/Prashant/desktop/try/images/', imgFileName)
	image = path
	processed = preprocess.processing(image)

if(__name__ == '__main__'):
	processImage()