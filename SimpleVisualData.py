from math import *
import tkinter as tk

# variables
master = tk.Tk()
# data = [[1], [3], [3], [2], [0, 2, 3], []]
locations = []

midX = 1000
midY = 500
radius = 250
size = 25

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
            w.create_line(locations[i][0], locations[i][1], locations[j][0], locations[j][1], arrow=tk.LAST,
                          arrowshape="16 20 6")


def hierarchicalVisual(data):
    root = findRoot(data)
    height = 100
    locations = []
    stop = False
    nodes = []

    locations.append([midX, height])
    height += 100
    nodes.append(root)

    while not stop:
        nodes.append


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


# circleVisual([[1], [3], [3], [2], [0, 2, 3], []])
hierarchicalVisual([[], [0], [1, 3], [4], []])
master.mainloop()
