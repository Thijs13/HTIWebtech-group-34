import networkx as nx
import matplotlib.pyplot as plt# nx can be seemed as an alias of networkx module
import numpy as np


class nodevis:
    def drawgraph(self,ds):
        G = nx.Graph()  # create an empty graph with no nodes and no edges
        nodes = []


        for i in range(len(ds.getNodes())):
            nodes.append([])
            for j in range(len(ds.getNodes())):
                nodes[i].append(ds.getNodes()[i].getLinks()[j][1])

        adj = np.array(nodes)
        G = nx.from_numpy_matrix(adj)

        nx.draw_networkx(G, with_labels=True)
        plt.show()
