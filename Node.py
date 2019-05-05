class Node:

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