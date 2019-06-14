class DataSetSort:

    def DesConnectionSort(self, ds):
        nodes = ds.getNodes()
        nodes.sort(key = self.sortConnectionKey, reverse = True)
        ds.setNodes(nodes)
        return ds

    def sortConnectionKey(self, node):
        return node.numLinks()

    def DesStrengthSort(self, ds):
        nodes = ds.getNodes()
        nodes.sort(key = self.sortStrengthKey, reverse = True)
        ds.setNodes(nodes)
        return ds

    def sortStrengthKey(self, node):
        return node.totLinkStrength()

