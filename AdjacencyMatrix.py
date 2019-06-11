import numpy as np
import matplotlib
import matplotlib.pyplot as plt

import pandas as pd
from bokeh.io import output_file, show
from bokeh.models import BasicTicker, ColorBar, LinearColorMapper, ColumnDataSource, PrintfTickFormatter
from bokeh.plotting import figure
from bokeh.transform import transform


class AdjacencyMatrix:
    def makeMatrix(self, ds):
        names = []
        # nodes = []
        for i in ds.getNodes():
            names.append(i.getName())
        nodes = ds.getDoubleList(0, True)

        yNames = names.copy()
        yNames.reverse()

        df = pd.DataFrame(
            nodes,
            columns=yNames,
            index=names)
        df.index.name = 'X'
        df.columns.name = 'Y'

        # Prepare data.frame in the right format
        df = df.stack().rename("value").reset_index()


        # here the plot :
        output_file("matrixPlot.html")

        # You can use your own palette here
        colorList = []
        for i in range(100):
            color = (255, 255, i)
            colorList.append(color)
        colors = colorList
        #[(255, 255, 255), '#fc942f', '#fda148', '#fdae61', '#fdbb7a', '#fec893', '#fed5ad']
        colors.reverse()
        # Had a specific mapper to map color with value
        mapper = LinearColorMapper(
            palette=colors, low=df.value.min(), high=df.value.max())
        # Define a figure
        p = figure(
            plot_width=800,
            plot_height=800,
            title="Matrix Visualization",
            x_range=list(df.X.drop_duplicates()),
            y_range=list(df.Y.drop_duplicates()),
            toolbar_location="below",
            tools="pan,wheel_zoom,box_zoom,reset",
            x_axis_location="above")
        # Create rectangle for heatmap
        p.rect(
            x="X",
            y="Y",
            width=1,
            height=1,
            source=ColumnDataSource(df),
            line_color=None,
            fill_color=transform('value', mapper))
        # Add legend
        color_bar = ColorBar(
            color_mapper=mapper,
            location=(0, 0),
            ticker=BasicTicker(desired_num_ticks=len(colors)))

        p.xaxis.major_label_orientation = 'vertical'
        p.add_layout(color_bar, 'right')
        show(p)
