from DataSet import DataSet
from Node import Node

class DataSetSort:

    def DesConnectionSort(self, ds):
        nodes = ds.getNodes()
        nodes.sort(key = self.sortKey)
        for node in nodes:
            node.print()
        ds.setNodes(nodes)
        # ds.print()
        return ds
        # self.mergeSort(nodes)

    def sortKey(self, node):
        return node.numLinks()

    def mergeSort(self, nodes):
        if nodes.length() != 1:
            length = nodes.length()
            n1 = nodes[0]
