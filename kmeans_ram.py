import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import contextlib


arr = []
x0 = []
y0 =[]
x1 = []
y1 = []
attr = 0
# with open ("TrainsetTugas2.txt","r") as brks:
#     data = brks.readlines()
#     for x in data:
#         brs = x.split()
#         x0.append([float(brs[0])])
#         y0.append([float(brs[1])])
#     attr += 1
#
# for i in range(len(x0)):
#     x0.append(np.array(x0[i]))
#     y0.append(np.array(y0[i]))
#
# print("Atribut X=",x0)
# print("Atribut Y=",y0)
#
# graf = plt.figure()
# graf.canvas.set_window_title('Visualisasi Data Training')
# data = graf.add_subplot(111)
# data.set_xlabel('Attr 1')
# data.set_ylabel('Attr 2')
# data.scatter(x0,y0, c='black', marker='+')
# plt.show()

class kmeans:
    def __init__(self, file):
        self.brks = open(file, 'r')
    def close(self):
        if self.brks:
            self.brks.close()
            self.brks = None

with contextlib.closing(kmeans("TrainsetTugas2.txt"))as berkas:
    data = berkas.brks.readlines()
    for x in data:
        brs = x.split()
        x0.append([float(brs[0])])
        y0.append([float(brs[1])])
    attr += 1

with contextlib.closing(kmeans("TestsetTugas2.txt"))as berkas:
    data = berkas.brks.readlines()
    for x in data:
        brs = x.split()
        x1.append([float(brs[0])])
        y1.append([float(brs[1])])
    attr += 1

for i in range(len(x0)):
    x0.append(np.array(x0[i]))
    y0.append(np.array(y0[i]))

print("Atribut X=",x0)
print("Atribut Y=",y0)

graf = plt.figure()
graf.canvas.set_window_title('Visualisasi Data Training')
data = graf.add_subplot(111)
data.set_xlabel('Attr 1')
data.set_ylabel('Attr 2')
data.scatter(x0,y0, c='black', marker='+')
plt.show()

berkas.brks.close()

