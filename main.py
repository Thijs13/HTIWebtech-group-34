from flask import Flask, flash, request, redirect, render_template, send_from_directory, url_for
import pandas as pd
from bokeh.embed import components
from bokeh.plotting import figure, curdoc
from bokeh.resources import CDN
# os methods for manipulating paths
from os.path import dirname, join, realpath

# Bokeh basics
from bokeh.io import curdoc, output_file, show
from bokeh.models.widgets import Tabs
from bokeh.layouts import column, row
from bokeh.models.widgets import *
from bokeh.models import CustomJS, Slider, ColumnDataSource, Select

from scripts.FileLoader import *
# from scripts.Node import nodeLink
from scripts.nodevis import *
# from scripts.DataSet import nodeLink
# from scripts.DataSetSort import nodeLink
from scripts.AdjacencyMatrix import *
from werkzeug.utils import secure_filename
import urllib.request
import os, sys
from random import random

FILEPATH = os.path.join(sys.path[0], "data/TestDataSmall")
UPLOAD_FOLDER = join(dirname(realpath(__file__)), 'data')
ALLOWED_EXTENSIONS = set(['txt', 'csv'])

LAYOUT = 0
FILTERMIN = 0
FILTERMAX = math.inf
REORDER = 0

app = Flask(__name__, static_url_path="", static_folder="static")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Index page
@app.route('/')
def index():
    fl = FileLoader()
    file = open(FILEPATH, "r")

    ds = fl.readFile(file)
    nv = nodevis()
    am = AdjacencyMatrix()

    filterMin = ds.maxLink() * FILTERMIN / 10
    filterMax = ds.maxLink() * FILTERMAX / 10

    plot = nv.drawgraph(ds, filterMin, filterMax, LAYOUT)
    plot2 = am.makeMatrix(ds, filterMin, filterMax, REORDER)

    slider1 = Slider(start=0, end=10, value=0, step=1, title="FILTERMIN", id="slider1")
    slider2 = RangeSlider(start=0, end=10, value=(1, 9), step=.1, title="Stuff", id="slider2")

    menu = [("Circular", "ordering"), ("Spring", "ordering"), ("Random", "ordering")]
    menu2 = [("Distance", "matrix"), ("Robinson", "re-ordering")]

    dropdown = Dropdown(label="Ordering", button_type="warning", menu=menu)
    dropdown2 = Dropdown(label="Ordering", button_type="warning", menu=menu2)

    infoNode = Div(text=ds.getStatsNode(FILTERMIN, 10), width=400, height=100)
    infoMatrix = Div(text=ds.getStatsMatrix(FILTERMIN, 10), width=400, height=100)

    #column1 = column(plot, dropdown, slider1, slider2)
    #column2 = column(plot2, dropdown, slider1, slider2)

    column1 = column(plot, infoNode)
    column2 = column(plot2, infoMatrix)

    row1 = row(column1, column2)

    script, div = components(row1)
    return render_template("index.html", script=script, div=div)


@app.route('/filter', methods = ['GET', 'POST'])
def result():
    slider1 = ""
    if request.method == 'POST':
        slider1 = request.form["slider3"]
        print(slider1)
        global FILTERMIN
        FILTERMIN = int(slider1)
        return redirect('/')


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            # print(file.filename)
            global FILEPATH
            FILEPATH = os.path.join(sys.path[0], "data/" + file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect('/')
        return


@app.route('/circular', methods = ['GET', 'POST'])
def circular():
    if request.method == 'POST':
        global LAYOUT
        LAYOUT = 0
        return redirect('/')


@app.route('/spring', methods = ['GET', 'POST'])
def spring():
    if request.method == 'POST':
        global LAYOUT
        LAYOUT = 1
        return redirect('/')


@app.route('/random', methods = ['GET', 'POST'])
def random():
    if request.method == 'POST':
        global LAYOUT
        LAYOUT = 2
        return redirect('/')


@app.route('/original', methods = ['GET', 'POST'])
def original():
    if request.method == 'POST':
        global REORDER
        REORDER = 0
        return redirect('/')


@app.route('/undirected', methods = ['GET', 'POST'])
def undirected():
    if request.method == 'POST':
        global REORDER
        REORDER = 1
        return redirect('/')


@app.route('/linkNumber', methods = ['GET', 'POST'])
def linkNumber():
    if request.method == 'POST':
        global REORDER
        REORDER = 2
        return redirect('/')


@app.route('/linkStrength', methods = ['GET', 'POST'])
def linkStrength():
    if request.method == 'POST':
        global REORDER
        REORDER = 3
        return redirect('/')


@app.route('/distanceMatrix', methods = ['GET', 'POST'])
def distanceMatrix():
    if request.method == 'POST':
        global REORDER
        REORDER = 4
        return redirect('/')


@app.route('/robinson', methods = ['GET', 'POST'])
def robinson():
    if request.method == 'POST':
        global REORDER
        REORDER = 5
        return redirect('/')


# @app.route('/static/<filename>')
# def uploaded_file(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'],
#                                filename)

# With debug=True, Flask server will auto-reload
# when there are code changes
if __name__ == '__main__':
    app.run(port=5000, debug=True)
