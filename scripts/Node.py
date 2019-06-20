class Node:

    # links is a list of list, with the inner list being a node reference and a relation strength
    def __init__(self, name, links):
        self.name = name
        self.links = links

    # returns the name
    def getName(self):
        return self.name

    # returns a list with all links
    def getLinks(self):
        return self.links

    # replaces the name of the node
    def setName(self, name):
        self.name = name

    # replace the list of links
    def setLinks(self, links):
        self.links = links

    # adds a link to the list of links
    def addLink(self, link):
        self.links.append(link)

    # removes a link with the inputted name from the list of links
    def removeLinkByName(self, name):
        for link in self.links:
            if link[1].getName() == name:
                self.links.remove(link)

    # removes the inputted link from the list of links
    def removeLink(self, target):
        self.links.remove(target)

    # returns the number of non-zero links
    def numLinks(self):
        numLinks = 0
        for link in self.getLinks():
            if link[1] != 0:
                numLinks += 1
        return numLinks

    # returns the sum of link strengths
    def totLinkStrength(self):
        total = 0
        for link in self.getLinks():
            total += link[1]
        return total

    # prints the name and links of the node
    def print(self):
        print(self.getName())
        for link in self.getLinks():
            print("  " + link[0].getName() + ": " + str(link[1]))

    # checks if the node has a non-zero relation with the inputted node
    def checkLink(self, node):
        for link in self.getLinks():
            if link[0] == node and link[1] != 0:
                return True
        return False

    # gets the link value to the inputted Node
    def getLink(self, target):
        for i in self.getLinks():
            if i[0] == target:
                return i[1]

    # returns the highest link strength
    def maxLink(self):
        maxVal = self.getLinks()[0][1]
        for link in self.getLinks():
            maxVal = max(maxVal, link[1])
        return maxVal

    # returns the lowest link strength
    def minLink(self):
        minVal = self.getLinks()[0][1]
        for link in self.getLinks():
            minVal = min(minVal, link[1])
        return minVal

    def checkAlone(self):
        for i in self.getLinks():
            if i[1] != 0:
                return False
        return True
