from DataSet import DataSet
from Node import Node

class DataSetSort:

    def DesConnectionSort(self, ds):
        nodes = ds.getNodes()
        nodes.sort(key = self.sortConnectionKey)
        ds.setNodes(nodes)
        return ds

    def sortConnectionKey(self, node):
        return node.numLinks()

    def DesStrengthSort(self, ds):
        nodes = ds.getNodes()
        nodes.sort(key = self.sortStrengthKey)
        ds.setNodes(nodes)
        return ds

    def sortStrengthKey(self, node):
        return node.totLinkStrength()

