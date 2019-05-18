class DataSet:

    def __init__(self, nodes):
        self.nodes = nodes

    def getNodes(self):
        return self.nodes

    def setNodes(self, nodes):
        self.nodes = nodes

    def addNote(self, node):
        self.nodes.append(node)

    def getNode(self, name):
        for node in self.nodes:
            if node.name == name:
                return node

# needs testing
    def deleteNode(self, target):
        self.nodes.remove(target)

    def print(self):
        for node in self.getNodes():
            node.print()


