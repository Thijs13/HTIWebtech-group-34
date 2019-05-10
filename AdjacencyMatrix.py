import numpy as np
import matplotlib
import matplotlib.pyplot as plt
# sphinx_gallery_thumbnail_number = 2


class AdjacencyMatrix:
    def makeMatrix(self, ds):
        names = []
        nodes = []
        for i in ds.getNodes():
            names.append(i.getName())
        for i in range(len(ds.getNodes())):
            nodes.append([])
            for j in range(len(ds.getNodes())):
                nodes[i].append(ds.getNodes()[i].getLinks()[j][1])

        y = names
        x = names
        nodes = np.array(nodes)

        fig, ax = plt.subplots()
        im = ax.imshow(nodes)

        # Shows all entries in the data set
        #ax.set_xticks(np.arange(len(x)))
        #ax.set_yticks(np.arange(len(y)))
        # Adds the labels to the axis
        #ax.set_xticklabels(x)
        #ax.set_yticklabels(y)

        # Rotate the tick labels and set their alignment.
        plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
                 rotation_mode="anchor")

        # Loop over data dimensions and create text annotations.
        #for i in range(len(y)):
        #    for j in range(len(x)):
        #        text = ax.text(j, i, nodes[i, j],
        #                       ha="center", va="center", color="w")


        ax.set_title("MyMatrix")
        fig.tight_layout()
        plt.show()