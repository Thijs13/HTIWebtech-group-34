class DataSet:

    def __init__(self, nodes):
        self.nodes = nodes

    # returns a list with the nodes in ds
    def getNodes(self):
        return self.nodes

    # replaces the list of nodes
    def setNodes(self, nodes):
        self.nodes = nodes

    # adds an additional node to the nodes in ds
    def addNote(self, node):
        self.nodes.append(node)

    # returns a reference to a node with the inputted name
    def getNode(self, name):
        for node in self.nodes:
            if node.name == name:
                return node

    # deletes the inputted node
    def deleteNode(self, target):
        self.nodes.remove(target)

    # prints the names and links of all nodes in the ds
    def print(self):
        for node in self.getNodes():
            node.print()

    # for all nodes, if they have a link to a node that does not have a link back, set that link to 0
    def makeUndirectional(self):
        for node in self.getNodes():
            for link in node.getLinks():
                if not link[0].checkLink(node):
                    link[1] = 0

