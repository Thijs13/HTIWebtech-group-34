import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from scripts.DataSetSort import *
import pandas as pd
from bokeh.io import output_file, show
from bokeh.models import BasicTicker, ColorBar, LinearColorMapper, ColumnDataSource, PrintfTickFormatter, HoverTool, TapTool, BoxSelectTool, BoxZoomTool, ResetTool, UndoTool, RedoTool, SaveTool
from bokeh.plotting import figure
from bokeh.transform import transform
import webcolors as wc


class AdjacencyMatrix:
    def makeMatrix(self, ds, filterMin):
        # getting data from FileLoader and creating the right format

        dataSetSort = DataSetSort()
        # dataSetSort.robinsonSort(ds)

        names = ds.getNames()
        nodes = ds.getDoubleList(filterMin, 10, True)
        # nodes = ds.distanceMatrix(True)
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
            i = i + 10

        #colorList = [(23, 165, 137), (19, 141, 117), (40, 180, 99), (36, 113, 163)
        #             , (31, 97, 141), (17, 122, 101), (46, 134, 193), (34, 153, 84)]#,(202, 111, 30), (186, 74, 0)]
        #colors = []
        #for i in colorList:
        #    color = wc.rgb_to_hex(i)
        #    colors.append(color)

        colors = colorList

        # This part maps the colors at intervals
        mapper = LinearColorMapper(
            palette=colors, low=df.value.min(), high=df.value.max())

        # Creating the figure
        p = figure(
            plot_width=500,
            plot_height=500,
            x_range=list(df.X.drop_duplicates()),
            y_range=list(df.Y.drop_duplicates()),

            # Adding a toolbar
            #toolbar_location="right",
            #tools="hover,pan,box_zoom,undo,redo,reset,save",
            x_axis_location="above")

        node_hover_tool = HoverTool(tooltips=[("Name X Axis", "@X"), ("Name Y Axis", "@Y"), ("Relation Strength", "@value")])

        # plot.add_tools(node_hover_tool, BoxZoomTool(), ResetTool())
        p.add_tools(node_hover_tool, TapTool(), BoxSelectTool(), BoxZoomTool(), UndoTool(), RedoTool())
        p.toolbar_location = 'right'

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

        if len(list(df.X.drop_duplicates())) > p.plot_width / 10:
            p.xaxis.visible = False
        else:
            pass
        if len(list(df.Y.drop_duplicates())) > p.plot_height / 10:
            p.yaxis.visible = False
        else:
            pass

        p.xaxis.major_label_orientation = 'vertical'
        p.add_layout(color_bar, 'right')
        return p
