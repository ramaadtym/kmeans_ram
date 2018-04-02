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


with contextlib.closing(kmeans("datakecil.txt"))as berkas:
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

#asumsi k = 2
# c1 = random.choice(titik)
# c2 = random.choice(titik)
# print("Centroid 1 = ", c1)
# print("Centroid 2 = ", c2)

# k = random.randint(2,5)
k = 2
print(k)

#iterasi 1
for t in range(k):
    getCentroid = random.choice(titik)
    centroid.append(getCentroid)
    print("Centroid ke-",t+1,getCentroid)
print(centroid)
# print(centroid[0][0])
# print(centroid[0][1])
# print(centroid[1][0])
for i in range(len(titik)):
    a = titik[i][0]
    b = titik[i][1]
    jarak = (a - centroid[0][0])**2 +  (b - centroid[0][1])**2
    jarak2 = (a - centroid[1][0])**2 +  (b - centroid[1][1])**2
    if jarak <  jarak2:
        kelas = "Kelas 1"
    else:
        kelas = "kelas 2"
    print("Data ke-",i,"|",jarak,"|",jarak2," | Titik Terdekat ", min(jarak, jarak2),"|",kelas)
# print("nilai min",min(jrk))


    # for i in range(len(titik)):
    #     a = titik[i][0]
    #     b = titik[i][1]
    #     jrkC1 = (a - centroid[0])**2 +  (b - centroid[1])**2
    #     print("Jarak titik ke centroid ke kelas",t+1,"= ", jrkC1)


# graf = plt.figure()
# graf.canvas.set_window_title('Visualisasi Data Training')
# data = graf.add_subplot(111)
# data.set_xlabel('Attr 1')
# data.set_ylabel('Attr 2')
# data.scatter(x0,y0, c='black', marker='+')
# plt.show()
