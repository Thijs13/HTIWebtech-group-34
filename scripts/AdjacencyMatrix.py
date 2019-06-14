import numpy as np
import matplotlib
import matplotlib.pyplot as plt

import pandas as pd
from bokeh.io import output_file, show
from bokeh.models import BasicTicker, ColorBar, LinearColorMapper, ColumnDataSource, PrintfTickFormatter
from bokeh.plotting import figure
from bokeh.transform import transform
import webcolors as wc


class AdjacencyMatrix:
    def makeMatrix(self, ds):
        # getting data from FileLoader and creating the right format
        names = []
        # nodes = []

        for i in ds.getNodes():
            names.append(i.getName())
        # nodes = ds.getDoubleList(0, True)
        nodes = ds.robinsonReordering()

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


        # Making the plot html file
        output_file("matrixPlot.html")

        # Creating the array containing the colors
        colorList = []
        i = 0
        while i < 256:
            color = wc.rgb_to_hex((255-(i-10), 255-(i-20), 255-(i-30)))
            colorList.append(color)
            i = i + 51
        colors = colorList

        # This part maps the colors at intervals
        mapper = LinearColorMapper(
            palette=colors, low=df.value.min(), high=df.value.max())

        # Creating the figure
        p = figure(
            plot_width=800,
            plot_height=800,
            x_range=list(df.X.drop_duplicates()),
            y_range=list(df.Y.drop_duplicates()),

            # Adding a toolbar
            toolbar_location="right",
            tools="hover,pan,box_zoom,reset",
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

        if len(list(df.X.drop_duplicates())) > p.plot_width / 4:
            p.xaxis.visible = False
        else:
            pass
        if len(list(df.Y.drop_duplicates())) > p.plot_height / 4:
            p.yaxis.visible = False
        else:
            pass

        p.xaxis.major_label_orientation = 'vertical'
        p.add_layout(color_bar, 'right')
        return p