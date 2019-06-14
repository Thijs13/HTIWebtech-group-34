from flask import Flask, flash, request, redirect, render_template, send_from_directory, url_for
import pandas as pd
from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.resources import CDN
# os methods for manipulating paths
from os.path import dirname, join, realpath

# Bokeh basics
from bokeh.io import curdoc, output_file, show
from bokeh.models.widgets import Tabs
from bokeh.layouts import column, row
from bokeh.models.widgets import *
from bokeh.models import CustomJS, Slider

from scripts.FileLoader import *
# from scripts.Node import nodeLink
from scripts.nodevis import *
# from scripts.DataSet import nodeLink
# from scripts.DataSetSort import nodeLink
from scripts.AdjacencyMatrix import *
from werkzeug.utils import secure_filename
import urllib.request
import os, sys

FILEPATH = os.path.join(sys.path[0], "data/TestDataSmall.txt")
UPLOAD_FOLDER = join(dirname(realpath(__file__)), 'data')
ALLOWED_EXTENSIONS = set(['txt', 'csv'])

app = Flask(__name__, static_url_path="", static_folder="static")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Index page
@app.route('/')
def index():
    print("t")
    fl = FileLoader()
    file = open(FILEPATH, "r")

    ds = fl.readFile(file)
    ds.editDoubleNames()

    nv = nodevis()
    am = AdjacencyMatrix()

    plot = nv.drawgraph(ds)
    plot2 = am.makeMatrix(ds)

    slider1 = Slider(start=0, end=10, value=1, step=.1, title="Stuff")
    slider2 = Slider(start=0, end=10, value=1, step=.1, title="Stuff")
    slider3 = RangeSlider(start=0, end=10, value=(1, 9), step=.1, title="Stuff")

    menu = [("Item 1", "item_1"), ("Item 2", "item_2"), None, ("Item 3", "item_3")]
    dropdown = Dropdown(label="Dropdown button", button_type="warning", menu=menu)

    column1 = column(plot, dropdown, slider2, slider3)
    column2 = column(plot2, dropdown, slider2, slider3)

    row1 = row(column1, column2)

    script, div = components(row1)

    return render_template("index.html", script=script, div=div)


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
            print(file.filename)
            global FILEPATH
            FILEPATH = os.path.join(sys.path[0], "data/" + file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect('/')
        return


# @app.route('/static/<filename>')
# def uploaded_file(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'],
#                                filename)

# With debug=True, Flask server will auto-reload
# when there are code changes
if __name__ == '__main__':
    app.run(port=5000, debug=True)
