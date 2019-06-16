from scripts.DataSet import DataSet
from scripts.Node import Node
from scripts.nodevis import nodevis
from scripts.AdjacencyMatrix import *


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

        # skips the first line because of names = file.readline()
        for line in file:
            # remove everything up to and including the first ";"
            line = line[len(nodes[numNode].getName()) + 1:]
            count = 0
            i = 0
            while i < len(line) - 1 and count != len(nodes):
                # if int(line[i]) != 0:
                number = ""
                while line[i] != ";" and line[i] != "\n":
                    number += line[i]
                    i += 1
                try:
                    number = float(number)
                except ValueError:
                    number = 0
                nodes[numNode].addLink([nodes[count], float(number)])
                count += 1
                i += 1
            while count < len(nodes) - 1:
                print(count)
                nodes[numNode].addLink([nodes[count], 0])
                count += 1
            numNode += 1
        ds.editDoubleNames()
        return ds


# file = open("TestDataSmall", "r")
# fileLoader = FileLoader()
# result = fileLoader.readFile(file)
# result.editDoubleNames()
# #result.makeUndirectional()
# #for i in result.getNodes():
# #    print("name: " + i.getName())
# #    for j in i.getLinks():
# #        print("   " + j[0].getName())
# #        print("   " + str(j[1]))
#
# while True:
#     choice = int(input("Type 1 for Adjacency Matrix, Type 2 for Node Link diagram, Type 3 to exit: "))
#     if choice == 1:
#         adjacencyMatrix = AdjacencyMatrix()
#         adjacencyMatrix.makeMatrix(result)
#     elif choice == 2:
#         nv = nodevis()
#         nv.drawgraph(result)
#     elif choice == 3:
#         break
#     else:
#         print("Wrong input")