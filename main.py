# This is a sample Python script.
import speech_recognition as sr
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from os import path
from pydub import AudioSegment
from functions import *
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


app = Flask(__name__, static_url_path='/static')

@app.route('/')
def home():
    text1 = 'sample test to audio:'
    return render_template('index.html') #(text1)#, script, 'Done')

@app.route('/sample')
def sample():
    filename = 'test.wav'
    script = get_script(filename)
    return script, '---Done----'

@app.route('/about/')
def about():
    return render_template('./about/index.html') #(text1)#, script, 'Done')

@app.route('/projects/')
def projects():
    return render_template('./projects/index.html') #(text1)#, script, 'Done')

@app.route('/projects/end_2_end_forecating/')
def end_2_end_forecating():
    return render_template('./projects/end_2_end_forecating/index.html') #(text1)#, script, 'Done')

@app.route('/projects/speech_to_text/')
def speech_to_text():
    return render_template('./projects/speech_to_text/index.html') #(text1)#, script, 'Done')

@app.route('/blogs/')
def blogs():
    return render_template('./blogs/index.html') #(text1)#, script, 'Done')

@app.route('/cv/')
def cv():
    return render_template('./cv/index.html') #(text1)#, script, 'Done')
# Press the green button in the gutter to run the script.

@app.route('/blogs/pc_building/')
def pc_building():
    return render_template('./blogs/pc_building/index.html') #(text1)#, script, 'Done')

@app.route('/transcribe', methods = ['POST'])
def transcribe():
    if request.method == 'POST':
        f = request.files['file']
        # f.save(f.filename)
        text = get_script(f)
        return render_template('./projects/speech_to_text/speech_to_text.html', name = text)

if __name__ == '__main__':
    app.run(debug=True)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
