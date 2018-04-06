import matplotlib.pyplot as plt
import numpy as np
# import pandas as pd
import contextlib
import random

arr = []
x0 = []
y0 = []
titik = []
centroid = []

jSSE = []
attr = 0

class kmeans:
    def __init__(self, file):
        self.brks = open(file, 'r')

    def close(self):
        if self.brks:
            self.brks.close()
            self.brks = None


with contextlib.closing(kmeans("TrainsetTugas2.txt"))as berkas:
# with contextlib.closing(kmeans("datakecil.txt"))as berkas:
    data = berkas.brks.readlines()
    for x in data:
        brs = x.split()
        titik.append([float(brs[0]), float(brs[1])])
        x0.append([float(brs[0])])
        y0.append([float(brs[1])])
    attr += 1
    berkas.brks.close()

k = 7

#iterasi 1
for t in range(k):
    getCentroid = random.choice(titik)
    centroid.append(getCentroid)


print (centroid)

g = 0
i = 0
# print (centroid)
for iterasi in range(100):
    jarak = [[] for i in range (k)]

    sse = 0
    for i in range(len(titik)):
        a = titik[i][0]
        b = titik[i][1]
        for g in range(k):
            jarak[g].append(np.sqrt((a - centroid[g][0]) ** 2 + (b - centroid[g][1]) ** 2))
    for i in range(len(jarak)):
        sse += sum(jarak[i])

    jaraktranspos = np.transpose(jarak)
    klaster = []
    for i in range (len(jarak[0])):
        jarakmin = jaraktranspos[i].tolist().index(min(jaraktranspos[i]))
        klaster.append([titik[i][0],titik[i][1],jarakmin])

    upil = [[0,0] for i in range(len(centroid))]
    jumlah = [0] * len(centroid)
    #kan gua bantuin klo bingung, wkwk
    for i in range(len(klaster)):
        kelompoktitik = klaster[i]
        upil[kelompoktitik[2]][0] += kelompoktitik[0]
        upil[kelompoktitik[2]][1] += kelompoktitik[1]
        jumlah[kelompoktitik[2]] += 1

    titikbaru = []
    for i in range(len(upil)):
        if (jumlah[i] > 0):
            ratarata = np.divide(upil[i],jumlah[i]).tolist()
            titikbaru.append(ratarata)
        else:
            titikbaru.append(centroid[i])
    centroid = titikbaru
    print (centroid)



centroidtranspose = np.transpose(centroid)

graf = plt.figure()
graf.canvas.set_window_title('Visualisasi Data Training')
data = graf.add_subplot(111)
data.set_xlabel('Attr 1')
data.set_ylabel('Attr 2')
data.scatter(x0,y0, c='black', marker='+')
data.scatter(centroidtranspose[0],centroidtranspose[1], c='red', marker='^')
plt.show()

#ditampilin coba, grafik? iya sama titiknya
#bingung nampilinnya, wkwk. titik yang mana pat? data trainnya?