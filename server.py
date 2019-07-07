import os
from flask import Flask, request, render_template, url_for, redirect
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route("/")
def fileFrontPage():
    return render_template('form.html')

@app.route("/handleUpload", methods=['POST'])
def handleFileUpload():
    if 'photo' in request.files:
        photo = request.files['photo']
        if photo.filename != '':
        	pass            
            #photo.save(os.path.join('C:/Users/Prashant/desktop', photo.filename))
    print(type(photo))
    return redirect(url_for('fileFrontPage'))

if __name__ == '__main__':
	app.run() 