from DataSet import DataSet
from Node import Node

class FileLoader:

    def readFile(self, file):
        ds = DataSet([])
        names = file.readline()
        names = names[1:]
        curName = ""

        # for all char's if it is a ";" create a node with the name up until the, else add the char to the name
        for char in names:
            if char == ";" or char == "\n":
                node = Node(curName, [])
                ds.addNote(node)
                curName = ""
            else:
                curName = curName + char

        numNode = 0
        nodes = ds.getNodes()

        # skips the first line because of 8
        for line in file:
            # remove everything up to and including the first ";"
            line = line[len(nodes[numNode].getName()) + 1:]
            count = 0
            i = 0
            while i < len(line) - 1:
                # if int(line[i]) != 0:
                nodes[numNode].addLink([nodes[count], int(line[i])])
                count += 1
                i += 2
            numNode += 1
        return ds


# file = open("ReadFileTest", "r")
# fileLoader = FileLoader()
# result = fileLoader.readFile(file)
# for i in result.getNodes():
#     print("name: " + i.getName())
#     for j in i.getLinks():
#         print("   " + j[0].getName())
#         print("   " + str(j[1]))
