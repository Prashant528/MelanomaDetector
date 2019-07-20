import os
from flask import Flask, request, render_template, url_for, redirect
import matplotlib.pyplot as plt
import mainProcess

app = Flask(__name__)

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