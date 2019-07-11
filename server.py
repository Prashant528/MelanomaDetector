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
            photo.save(os.path.join('C:/Users/Prashant/desktop/try/images/', photo.filename))
    mainProcess.processImage(photo.filename)
    print('server.py redirecting ...')
    return redirect(url_for('fileFrontPage'))

if __name__ == '__main__':
	app.run(host = '0.0.0.0') 