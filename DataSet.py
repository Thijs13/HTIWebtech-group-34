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

    # returns the highest link strength of all the nodes
    def maxLink(self):
        maxVal = self.getNodes()[0].maxLink()
        for node in self.getNodes():
            maxVal = max(maxVal, node.maxLink())
        return maxVal

    # returns the lowest link strength of all the nodes
    def minLink(self):
        minVal = self.getNodes()[0].minLink()
        for node in self.getNodes():
            minVal = min(minVal, node.minLink())
        return minVal

    # for all nodes, if they have a link to a node that does not have a link back, set that link to 0
    def makeUndirectional(self):
        for node in self.getNodes():
            # print(node.getName())
            for link in node.getLinks():
                if not link[0].checkLink(node):
                    link[1] = 0

    # returns the ds as two dimensional array with level 1 the nodes and level 2 that nodes links
    def getDoubleList(self):
        result = []
        for i in range(len(self.getNodes())):
            result.append([])
            curNode = self.getNodes()[i]
            for j in range(len(self.getNodes())):
                #curIndex = curNode.getLinks().index(self.getNodes()[j])
                curIndex = self.returnIndex(curNode.getLinks(), self.getNodes()[j])
                link = curNode.getLinks()[curIndex][1]
                result[i].append(link)
        return result

    # returns the index of a node in an list of links. Made primarily for getDoubleList()
    def returnIndex(self, links, node):
        count = 0
        for link in links:
            if link[0] == node:
                return count
            count += 1
        return -1
