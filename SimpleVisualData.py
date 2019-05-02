from math import *
import tkinter as tk

# variables
master = tk.Tk()
# data = [[1], [3], [3], [2], [0, 2, 3], []]
locations = []

midX = 1000
midY = 500
radius = 250
size = 20

w = tk.Canvas(master, width=midX * 2, height=midY * 2)
w.pack()


def circleVisual(data):
    numData = len(data)
    for i in range(numData):
        circleX = midX + radius * sin(i * 2 * pi / numData)
        circleY = midY - radius * cos(i * 2 * pi / numData)
        locations.append([circleX, circleY])
        w.create_oval(circleX - size, circleY - size, circleX + size, circleY + size, fill="blue")

    for i in range(numData):
        for j in data[i]:
            drawArrow(locations[i][0], locations[i][1], locations[j][0], locations[j][1])
            # w.create_line(locations[i][0], locations[i][1], locations[j][0], locations[j][1], arrow=tk.LAST,
                          # arrowshape="16 20 6")


def hierarchicalVisual(data):
    root = findRoot(data)
    height = 100
    locations = []
    stop = False
    nodes = []
    nextNodes = []

    w.create_oval(midX - size, 100 - size, midX + size, 100 + size, fill="blue")
    traverseTree(data, root, midX, 100, 750)

    # while not stop:
    #     for i in nodes[0]:
    #         nextNodes.append[i]
    #     locations.append([midX, height])
    #     height += 100


def traverseTree(data, i, xParent, yParent, space):
    if len(data[i]) == 1:
        w.create_oval(xParent - size, yParent + 100 - size, xParent + size, yParent + 100 + size, fill="blue")
        #w.create_line(xParent, yParent, xParent, yParent + 100, arrow=tk.LAST, arrowshape="16 20 6")
        drawArrow(xParent, yParent, xParent, yParent + 100)
        traverseTree(data, data[i][0], xParent, yParent + 100, space / len(data[i]))
    else:
        count = 0
        for j in data[i]:
            xLoc = xParent - space/2 + count*space/(len(data[i]) - 1)
            yLoc = yParent + 100
            w.create_oval(xLoc - size, yLoc - size, xLoc + size, yLoc + size, fill="blue")
            #w.create_line(xParent, yParent, xLoc, yLoc, arrow=tk.LAST, arrowshape="16 20 6")
            drawArrow(xParent, yParent, xLoc, yLoc)
            traverseTree(data, j, xLoc, yLoc, space/len(data[i]))
            count += 1


def findRoot(data):
    numData = len(data)
    root = -1
    isRoot = False
    for i in range(numData):
        isRoot = True
        for j in range(numData):
            for k in data[j]:
                if k == i:
                    isRoot = False
        if j == numData - 1 and isRoot:
            root = i
    return root


def drawArrow(x1, y1, x2, y2):
    angle = atan((x1-x2)/(y1-y2))
    min = 1
    if y1 <= y2:
        min = -1
    xEdge = x2 + sin(angle) * size * min
    yEdge = y2 + cos(angle) * size * min
    w.create_line(x1, y1, xEdge, yEdge, arrow=tk.LAST, arrowshape="16 20 6")


# circleVisual([[1], [3], [3, 5], [2], [0, 2, 3], []])
# hierarchicalVisual([[1, 2], [3, 4], [5, 6], [], [], [], []])
# hierarchicalVisual([[1], [2, 3, 4], [5, 6], [], [], [], []])
hierarchicalVisual([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [], [], [], [], [], [], [], [], []])
master.mainloop()
