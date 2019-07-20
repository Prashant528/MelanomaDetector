import os
import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
import cv2 
imagePath = "C:/Users/prashant/Desktop/dataset/training/naevus"
savePath = "C:/Users/prashant/Desktop/third/minorProject/images"

'''------------ LOADING IMAGES FROM FILES -------------'''
def loadImage(path):
	image_files = sorted([os.path.join(path, file) for file in os.listdir(path) if file.endswith('.jpg')])
	return image_files

'''-----------FUNCTION FOR DISPLAYING IMAGE---------------'''
def display_one(imgA, title1="Original"):
	cv2.imshow('image', imgA)
	plt.imshow(imgA), plt.title(title1)
	plt.xticks([]), plt.yticks([])
	plt.show()

'''---------- FUNCTION FOR DISPLAYING TWO IMAGES (HERE,ORIGINAL AND CHANGED IMAGE) --------------'''
def display_two(imgA, imgB, title1="Original", title2="Edited"):
	plt.subplot(121), plt.imshow(imgA, cmap = plt.cm.gray), plt.title(title1)
	plt.xticks([]), plt.yticks([])
	plt.subplot(122), plt.imshow(imgB, cmap = plt.cm.gray),plt.title(title2)
	plt.xticks([]), plt.yticks([])
	plt.show()


""" ------------------ PROCESSING THE IMAGE ----------------"""
def processing(data):
	img_bgr = cv2.imread(data, cv2.IMREAD_UNCHANGED)#data is path hai
	img = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB) #changing bgr to rgb
	print('Original size:', img.shape)
	
	'''--------grayscale conversion---------------'''
	gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
	

	'''----------RESIZING THE IMAGE---------------'''
	height = 500
	width = 500
	dim = (height, width)
	resized = cv2.resize(gray, dim, interpolation=cv2.INTER_LINEAR)
	
	#printing the resized image
	display_two(img, gray, 'Original', 'Grayed')


	'''---------removing noise by gaussian blur---------'''
	blurred = cv2.medianBlur(resized, 5)
	#printing the blurred image
	display_two(resized, blurred, 'Resized', 'Median Filtered')


	'''-------------segmentation---------------------'''
	ret, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
	# printing the grayed and thresholded image
	display_two(blurred, thresh, 'Filtered', 'Thresholded')

	'''YESLE CHAI HAWA KAM GAREKO JASTO LAIRAXA MALAI
	# Further noise removal
	kernel = np.ones((3,3), np.uint8)
	opening = cv2.morphologyEx(tList[0], cv2.MORPH_OPEN, kernel, iterations=2)

	# sure background area
	sure_bg = cv2.dilate(opening, kernel, iterations=3)

	# sure foreground area
	dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
	ret, sure_fg = cv2.threshold(dist_transform, 0.7*dist_transform.max(), 255, 0)

	#finding unknown region
	# sure_fg = np.uint(sure_fg)
	# unknown = cv2.subtract(sure_bg, sure_fg)

	#displaying segmented background
	display_two(tList[0], sure_bg, 'first seg', 'later seg' )
	'''
	return blurred

def main():
	data = loadImage(imagePath)
	processing(data)

if(__name__ == '__main__'):
	main()