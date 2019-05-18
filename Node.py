class Node:

    # links is a list of list, with the inner list being a node reference and a relation strength
    def __init__(self, name, links):
        self.name = name
        self.links = links

    def getName(self):
        return self.name

    def getLinks(self):
        return self.links

    def setName(self, name):
        self.name = name

    def setLinks(self, links):
        self.links = links

    def addLink(self, link):
        self.links.append(link)

    def removeLink(self, name):
        for link in self.links:
            if link[1] == name:
                self.links.remove(link)

    def numLinks(self):
        numLinks = 0
        for link in self.getLinks():
            if link[1] != 0:
                numLinks += 1
        return numLinks

    def print(self):
        print(self.getName())
        for link in self.getLinks():
            print("  " + link[0].getName() + ": " + str(link[1]))