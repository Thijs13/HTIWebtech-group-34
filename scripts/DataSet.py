import networkx as nx
import numpy as np
from scripts.Node import *
from scipy.spatial.distance import pdist
from scipy.cluster.hierarchy import complete

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

    # returns a list of names of all nodes
    def getNames(self):
        names = []
        for i in self.getNodes():
            names.append(i.getName())
        return names

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

    # sets all link strengths of the ds to 0
    def setToZero(self):
        for i in self.getNodes():
            for j in i.getLinks():
                j[1] = 0

    # for all nodes, if they have a link to a node that does not have a link back, set that link to 0
    def makeUndirectional(self):
        for node in self.getNodes():
            # print(node.getName())
            for link in node.getLinks():
                if not link[0].checkLink(node):
                    link[1] = 0

    # for all nodes, if they get a link from a node that do not have a link to, set that link to 1
    def makeUndirectionalAdd(self):
        for node in self.getNodes():
            for link in node.getLinks():
                if link[0].checkLink(node):
                    link[1] = link[0].getLink(node)

    # returns the ds as two dimensional array with level 1 the nodes and level 2 that nodes links
    # set filters to 0 to have no filter
    # set reverse to true to reverse the order of the links within the nodes. mainly for matrix visualisation
    def getDoubleList(self, filterMin, filterMax, reverse):
        result = []
        for i in range(len(self.getNodes())):
            result.append([])
            curNode = self.getNodes()[i]
            for j in range(len(self.getNodes())):
                curIndex = self.returnIndex(curNode.getLinks(), self.getNodes()[j])
                link = curNode.getLinks()[curIndex][1]
                if not (filterMin <= link <= filterMax) and filterMin != 0 and filterMax != 0:
                    link = 0
                result[i].append(link)
            if reverse:
                result[i].reverse()
        return result

    # returns the index of a node in an list of links. Made primarily for getDoubleList()
    def returnIndex(self, links, node):
        count = 0
        for link in links:
            if link[0] == node:
                return count
            count += 1
        return -1

    # adds nodes based on the inputted two dimensional edge array and name array
    # note that this function deletes existing data in the ds
    def buildFromList(self, list, nameList):
        nodes = []
        for i in nameList:
            node = Node(i, [])
            nodes.append(node)
        for i in range(len(list)):
            for j in range(len(list[i])):
                nodes[i].addLink([nameList[j], list[i][j]])
        self.setNodes(nodes)

    # returns true if the ds contains nodes with identical names
    def checkDoubleNames(self):
        for i in self.getNodes():
            name = i.getName()
            nameCount = 0
            for j in self.getNodes():
                if j.getName() == name:
                    nameCount += 1
                if nameCount > 1:
                    return True
        return False

    def editDoubleNames(self):
        for i in self.getNodes():
            numName = 0
            for j in self.getNodes():
                if j.getName() == i.getName():
                    if numName > 0:
                        newName = j.getName() + str(numName)
                        j.setName(newName)
                        # print(newName)
                    numName += 1

    # turns the data in the ds into a minimum spanning tree.
    # note that this function deletes other data in the ds
    def toMinSpanTree(self):
        nodeList = self.getDoubleList(0, False)
        numpyArray = np.array(nodeList)
        netX = nx.from_numpy_matrix(numpyArray)
        netX = nx.minimum_spanning_tree(netX)
        nxList = nx.to_edgelist(netX)
        self.setToZero()
        nodes = self.getNodes()
        for i in nxList:
            nodes[i[0]].getLinks()[i[1]][1] = i[2]['weight']

    # returns the distance matrix of the current ds
    # note that this function takes (at least) O(n^3) worst case time
    def distanceMatrix(self, reverse):
        oldDs = self.getNodes()
        self.toMinSpanTree()
        self.makeUndirectionalAdd()
        nodes = self.getNodes()
        self.setNodes(oldDs)

        disMatrix = []
        names = self.getNames()

        count = 0
        for i in nodes:
            print(count)
            count += 1
            disMatrix.append([])
            checknodes = [[i, 0]]
            for j in range(len(i.getLinks())):
                curNode = checknodes[j][0]
                curDis = checknodes[j][1]
                for k in curNode.getLinks():
                    if k[1] != 0 and not self.checkPresent(checknodes, k[0]):
                        checknodes.append([k[0], curDis + k[1]])
                if j == len(checknodes) - 1:
                    for k in self.getNodes():
                       if not self.checkPresent(checknodes, k):
                           checknodes.append([k, -1])
                    break
            for j in names:
                for k in checknodes:
                    if k[0].getName() == j:
                        disMatrix[-1].append(k[1])
        if reverse:
            for i in disMatrix:
                i.reverse()
        return disMatrix

    # support function for the distanceMatrix function
    # check if a target is present in a list of lists as first item of the second level list
    def checkPresent(self, list, target):
        for i in list:
            if i[0] == target:
                return True
        return False

    # def robinsonReordering(self):
    #     nodes = self.getDoubleList(0, False)
    #     distMat = pdist(nodes)
    #     orderedMatrix = complete(distMat)
    #     orderedMatrix = orderedMatrix.tolist()
    #     for i in orderedMatrix:
    #         print(i)
    #     return orderedMatrix
