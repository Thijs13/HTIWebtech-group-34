class Cluster:

    def __init__(self, nodes, first, last):
        self.nodes = nodes
        self.first = first
        self.last = last

    # def __init__(self, nodes):
    #     self.nodes = nodes

    def setNodes(self, nodes):
        self.nodes = nodes

    def getNodes(self):
        return self.nodes

    def setFirst(self, first):
        self.first = first

    def getFirst(self):
        return self.first

    def setLast(self, last):
        self.last = last

    def getLast(self):
        return self.last

    def conjugate(self, cluster, addFront):
        newNodes = self.getNodes()
        newNodes.extend(cluster.getNodes())
        self.setNodes(newNodes)
        if addFront:
            self.setFirst(cluster.getFirst())
        else:
            self.setLast(cluster.getLast())

