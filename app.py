from flask import Flask, render_template, request, flash, redirect, url_for
from flask import send_file
from jinja2 import Template

import os

from processing import *
from MusicVae import *
from RANGAN import *

# To run just run: python -m flask run

app = Flask(__name__)

fileNames = [None, None]


@app.route("/")
def index():
    remove_Files(os.listdir('static/midiFiles'))
    return render_template("index.html")


@app.route("/process-file/", methods=['GET', 'POST'])
def process_file():
    myvar = request.form['processed-file']

    fileNames[0] = getFileFromURL(myvar)

    #noteSeq = getNoteSequence(fileNames[0])

    try:
        return ('', 204)
    except Exception as e:
        return str(e)


@app.route("/process-file-2/", methods=['GET', 'POST'])
def process_file_2():
    myvar = request.form['processed-file-2']

    fileNames[1] = getFileFromURL(myvar)

    #noteSeq = getNoteSequence(fileNames[1])

    try:
        return ('', 204)
    except Exception as e:
        return str(e)

# Running


@app.route("/run-fusion/", methods=['GET', 'POST'])
def run_fusion():
    """
    myvars = request.values['slider-values']
    myvars = myvars.split(',')
    var1 = myvars[0]
    var2 = myvars[1]
    var3 = myvars[2]
    print(var1, var2, var3)
    """

    print(fileNames)
    musicFusion(fileNames[0], fileNames[1])

    try:
        return ('', 204)
    except Exception as e:
        return str(e)


@app.route("/run-gan/", methods=['GET', 'POST'])
def run_gan():
    print(fileNames)
    myvars = request.values['slider-values']
    myvars = myvars.split(',')
    var1 = int(myvars[0])
    var2 = float(myvars[1])
    var3 = float(myvars[2])
    print(var1, var2, var3)

    # (length, offset_increment, alpha)
    runGan(var1, var2, var3)

    try:
        return ('', 204)
    except Exception as e:
        return str(e)

# run gan all variables set lowest: 2:15
# run gan all variables set highest(350, 1, 1): crash
# run gan all variables set highest(300, 1, 1): crash
# run gan all variables set highest(350, 0.6, 0.6): crash
# run gan all variables set highest(200, 1, 1): crash


if __name__ == "__main__":
    app.run(debug=True)


def remove_Files(fn):
    for f in fn:
        os.remove(os.path.join('static/midiFiles', f))
