from scripts.Cluster import *
import math
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

    def robinsonSort(self, ds):
        disMatrix = ds.distanceMatrix(False)
        clusters = []
        nodes = ds.getNodes()
        count = 0
        for i in nodes:
            cluster = Cluster([i], i, i)
            clusters.append(cluster)
        while len(clusters) > 1 and count < len(nodes):
            print(count)
            newClusters = []
            while len(clusters) > 1:
                curClus = clusters[0]
                clusters.pop(0)
                mini = math.inf
                closeClus = None
                for i in clusters:
                    distance = self.getDistance(disMatrix, nodes, curClus.getFirst(), i.getFirst())
                    if distance < mini and distance > 1:
                        mini = distance
                        first = True
                        closeClus = i
                    distance = self.getDistance(disMatrix, nodes, curClus.getLast(), i.getFirst())
                    if distance < mini and distance > 1:
                        mini = distance
                        first = False
                        closeClus = i
                    distance = self.getDistance(disMatrix, nodes, curClus.getFirst(), i.getLast())
                    if distance < mini and distance > 1:
                        mini = distance
                        first = True
                        closeClus = i
                    distance = self.getDistance(disMatrix, nodes, curClus.getLast(), i.getLast())
                    if distance < mini and distance > 1:
                        mini = distance
                        first = False
                        closeClus = i
                if closeClus is not None:
                    curClus.conjugate(closeClus, first)
                    clusters.remove(closeClus)
                newClusters.append(curClus)
            if len(clusters) == 1:
                newClusters.append(clusters[0])
                clusters.pop(0)
            clusters.extend(newClusters.copy())
            count += 1
        newNodes = []
        for i in clusters:
            newNodes.extend(i.getNodes())
        ds.setNodes(newNodes)

    def searchClusters(self, clusters, node, first):
        for i in clusters:
            if first:
                if i.getFirst() == node:
                    return i
            else:
                if i.getLast() == node:
                    return i

    def getDistance(self, disMatrix, nodes, node1, node2):
        row = nodes.index(node1)
        column = nodes.index(node2)
        return disMatrix[row][column]


