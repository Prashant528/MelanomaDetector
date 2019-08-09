# import os
# from flask import Flask, request, render_template, url_for, redirect
# import matplotlib.pyplot as plt
import mainProcess

# app = Flask(__name__)

import os
#import magic
import urllib.request
from app import app
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename
global filename

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
	
@app.route('/')
def upload_form():
    # prediction = mainProcess.processImage(filename)
	return '5'

@app.route('/', methods=['POST'])
def upload_file():
	if request.method == 'POST':
        # check if the post request has the file part
		if 'file' not in request.files:
			flash('No file part')
			return redirect(request.url)
		file = request.files['file']
		if file.filename == '':
			flash('No file selected for uploading')
			return redirect(request.url)
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			print('File successfully uploaded')
			predic = mainProcess.processImage(filename)
			return '5'
			return redirect('/')
		else:
			flash('Allowed file types are png, jpg, jpeg')
			return redirect(request.url)

if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug = True)


'''
@app.route("/")
def fileFrontPage():
    return render_template('form.html')

@app.route("/handleUpload", methods=['POST'])
def handleFileUpload():
    if 'photo' in request.files:
        photo = request.files['photo']
        if photo.filename != '':    
            photo.save(os.path.join('C:/Users/prashant/Desktop/third/minorProject/images/', photo.filename))
            
    predic = mainProcess.processImage(photo.filename)
    # return redirect(url_for('fileFrontPage'))
    return render_template("result.html", result = predic)

if __name__ == '__main__':
	app.run(host = '0.0.0.0', debug = True) 
'''