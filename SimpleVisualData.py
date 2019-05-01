from math import *
import tkinter as tk

# variables
master = tk.Tk()
data = [[1], [3], [3], [2], [0, 2, 3]]
locations = []
numData = len(data)
midX = 1000
midY = 500
radius = 250
size = 25

w = tk.Canvas(master, width=midX*2, height=midY*2)
w.pack()

for i in range(numData):
    circleX = midX + radius*sin(i*2*pi/numData)
    circleY = midY - radius*cos(i*2*pi/numData)
    locations.append([circleX, circleY])
    w.create_oval(circleX - size, circleY - size, circleX + size, circleY + size, fill="blue")

for i in range(numData):
    for j in data[i]:
        w.create_line(locations[i][0], locations[i][1], locations[j][0], locations[j][1], arrow=tk.LAST,
                      arrowshape="16 20 6")

master.mainloop()
