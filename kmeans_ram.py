import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import contextlib
import random

arr = []
x0 = []
y0 = []
titik = []
centroid = []
minx = []
miny = []
jarak = []
sse = []
jSSE = []
attr = 0


class kmeans:
    def __init__(self, file):
        self.brks = open(file, 'r')

    def close(self):
        if self.brks:
            self.brks.close()
            self.brks = None


# with contextlib.closing(kmeans("TrainsetTugas2.txt"))as berkas:
with contextlib.closing(kmeans("datakecil.txt"))as berkas:
    data = berkas.brks.readlines()
    for x in data:
        brs = x.split()
        titik.append([float(brs[0]), float(brs[1])])
        x0.append([float(brs[0])])
        y0.append([float(brs[1])])
    attr += 1
    berkas.brks.close()
k = 2
print(k)

#iterasi 1
for t in range(k):
    getCentroid = random.choice(titik)
    centroid.append(getCentroid)
    # print("Centroid ke-",t+1,getCentroid)
g = 0
i = 0

for i in range(len(titik)):
    a = titik[i][0]
    b = titik[i][1]
    for g in range(k):
        jarak.append((a - centroid[g][0]) ** 2 + (b - centroid[g][1]) ** 2)
        g += 1
    sse.append(min(jarak[i],jarak[i+1]))
#     print(sse)
#     print(sum(sse))
#     jSSE.append(sum(sse))
# print(jSSE)
# print(min(jSSE))
    # print(min(sum(sse)))
# print("Nilai Min SSE dari ",j+1," Percobaan",min(jSSE))

# graf = plt.figure()
# graf.canvas.set_window_title('Visualisasi Data Training')
# data = graf.add_subplot(111)
# data.set_xlabel('Attr 1')
# data.set_ylabel('Attr 2')
# data.scatter(x0,y0, c='black', marker='+')
# plt.show()
