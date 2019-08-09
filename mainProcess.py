#This module sends the image for pre-processing, recieves it back and fits it on the CNN model and returns back the risk factor.
import tensorflow
import tensorflow.keras
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.backend import set_session
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import preprocess
import os

img_width, img_height = 500, 500
global sess
global graph
sess = tensorflow.Session()
graph = tensorflow.get_default_graph()
set_session(sess)
model = load_model('newModelgray.h5')
# model.summary()


#is a function that takes the filename as argument and displays it.
def processImage(imgFileName):

	path = os.path.join('C:/Users/prashant/Desktop/third/minorProject/images/', imgFileName)
	processed = preprocess.processing(path) #this sends image to next module for preprocessing.
	print(path)
	print('\n--------------PREDICTIONS------------------\n')
	x = image.img_to_array(processed)
	x = np.expand_dims(x, axis=0)
	with graph.as_default():
		set_session(sess)
		prediction = model.predict(x, batch_size=None)

	print("Risk factor from image = ",prediction, type(prediction))
	print('\n')
	value = prediction[0][0]
	print(type(value))
	return value

if(__name__ == '__main__'):
	processImage()