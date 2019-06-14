import networkx as nx
import matplotlib.pyplot as plt# nx can be seemed as an alias of networkx module
import numpy as np
import pyqtgraph as pt
from bokeh.io import show, output_file
from bokeh.models import Plot, Range1d, MultiLine, Circle, HoverTool, TapTool, BoxSelectTool, BoxZoomTool, ResetTool
from bokeh.models.graphs import from_networkx, NodesAndLinkedEdges, EdgesAndLinkedNodes
from bokeh.palettes import Spectral4

class nodevis:
    def drawgraph(self, ds):
        G = nx.Graph()  # create an empty graph with no nodes and no edges

        # nodes = []
        # for i in range(len(ds.getNodes())):
        #     nodes.append([])
        #     # print(ds.getNodes()[i].getName())
        #     for j in range(len(ds.getNodes())):
        #         nodes[i].append(ds.getNodes()[i].getLinks()[j][1])
        #         # print("   " + str(ds.getNodes()[i].getLinks()[j][1]))

        ds.toMinSpanTree()
        nodes = ds.getDoubleList(0, False)

        adj = np.array(nodes)
        G = nx.from_numpy_matrix(adj)

        for i in range(len(G.node)):
            G.node[i]['name'] = ds.getNames()[i]
        #pos = nx.drawing.layout.circular_layout(G, 1, None, 2)

        #nx.draw_networkx(G, pos, with_labels=True)
        # pt.show()
        #plt.show()
        plot = Plot(plot_width=500, plot_height=500,
                    x_range=Range1d(-1.1, 1.1), y_range=Range1d(-1.1, 1.1))
        plot.title.text = "Graph Interaction Demonstration"

        node_hover_tool = HoverTool(tooltips=[("name", "@name")])

        # plot.add_tools(node_hover_tool, BoxZoomTool(), ResetTool())
        plot.add_tools(node_hover_tool, TapTool(), BoxSelectTool())

        graph_renderer = from_networkx(G, nx.circular_layout, scale=1, center=(0, 0))

        graph_renderer.node_renderer.glyph = Circle(size=15, fill_color=Spectral4[0])
        graph_renderer.node_renderer.selection_glyph = Circle(size=15, fill_color=Spectral4[2])
        graph_renderer.node_renderer.hover_glyph = Circle(size=15, fill_color=Spectral4[1])

        graph_renderer.edge_renderer.glyph = MultiLine(line_color="#CCCCCC", line_alpha=0.8, line_width=5)
        graph_renderer.edge_renderer.selection_glyph = MultiLine(line_color=Spectral4[2], line_width=5)
        graph_renderer.edge_renderer.hover_glyph = MultiLine(line_color=Spectral4[1], line_width=5)

        graph_renderer.selection_policy = NodesAndLinkedEdges()
        #graph_renderer.inspection_policy = EdgesAndLinkedNodes()

        plot.renderers.append(graph_renderer)

        output_file("interactive_graphs.html")
        return plot
