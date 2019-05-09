import networkx as nx
import matplotlib.pyplot as plt# nx can be seemed as an alias of networkx module
import numpy as np
G = nx.Graph()            # create an empty graph with no nodes and no edges
print(G.nodes(), G.edges())




nx.draw_networkx(G, with_labels=True)
plt.show()