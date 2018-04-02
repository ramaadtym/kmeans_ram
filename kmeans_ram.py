import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import contextlib
import random

arr = []
x0 = []
y0 = []
titik = []
x1 = []
y1 = []
attr = 0


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
        titik.append([float(brs[0]), float(brs[1])])
        x0.append([float(brs[0])])
        y0.append([float(brs[1])])
    attr += 1
    berkas.brks.close()

# with contextlib.closing(kmeans("TestsetTugas2.txt"))as berkas:
#     data = berkas.brks.readlines()
#     for x in data:
#         brs = x.split()
#         x1.append([float(brs[0])])
#         y1.append([float(brs[1])])
#     attr += 1

c1 = random.choice(titik)
c2 = random.choice(titik)
print("Centroid 1 = ", c1)
print("Centroid 2 = ", c2)

# for i in range(len(titik)):
# hitung pake euclid



# graf = plt.figure()
# graf.canvas.set_window_title('Visualisasi Data Training')
# data = graf.add_subplot(111)
# data.set_xlabel('Attr 1')
# data.set_ylabel('Attr 2')
# data.scatter(x0,y0, c='black', marker='+')
# plt.show()
