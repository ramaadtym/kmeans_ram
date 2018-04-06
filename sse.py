import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import norm

f = open("TrainsetTugas2.txt", "r")
s = f.readlines()
f.close()
np.random.seed(2)
# Preprocessing
X = []
for baris in s:
    splittedtext = baris.replace('\n', '').split('\t')
    X.append([float(splittedtext[0]), float(splittedtext[1])])

#


# x1 = [X[i][0] for i in range(len(X))]
# x2 = [X[i][1] for i in range(len(X))]
X = np.array(X)
x1 = X[:, 0]
x2 = X[:, 1]


# print (x1)

#
def euclid(x2, x1, y2, y1):
    deltax = (x2 - x1) ** 2
    deltay = (y2 - y1) ** 2
    return np.sqrt(deltax + deltay)


#
#
# # sentroids = [[0,0],[10,10],[15,15]]
daftarSSE = []
for bb in range(1, 2):
    K = bb
    sentroids = []
    SSElama = -1
    SSE = -2
    for i in range(K):
        sentroids.append([np.random.uniform(5, 35), np.random.uniform(0, 35)])

    while (SSElama != SSE):
        # for i in range(400):
        daftarjarak = []
        SSElama = SSE
        SSE = 0

        for j in range(len(sentroids)):
            sentroid = sentroids[j]
            daftarjarak.append([])
            for i in range(len(X)):
                daftarjarak[j].append(euclid(sentroid[0], X[i][0], sentroid[1], X[i][1]))
            print(daftarjarak)
        kelompok = [[] for i in range(len(sentroids))]
        # print (kelompok)
        for k in range(len(daftarjarak[0])):
            min = 999999999
            index = 0
            for j in range(len(sentroids)):
                if (daftarjarak[j][k] < min):
                    index = j
                    min = daftarjarak[j][k]
            kelompok[index].append([X[k][0], X[k][1]])
            #    # print (kelompok)

        for z in range(len(kelompok)):
            hh = [0, 0]
            for i in range(len(kelompok[z])):
                hh[0] += kelompok[z][i][0]
                hh[1] += kelompok[z][i][1]
            if (len(kelompok[z]) != 0):
                hh[0] /= len(kelompok[z])
                hh[1] /= len(kelompok[z])
                sentroids[z] = hh
        for i in range(len(sentroids)):
            if (len(kelompok[i]) > 0):
                SSE += norm(np.subtract(kelompok[i], sentroids[i]))
        print("SSE = ", SSE)
    # sen1 = [sentroids[i][0] for i in range(len(sentroids))]
    # sen2 = [sentroids[i][1] for i in range(len(sentroids))]
    # fig, ax = plt.subplots()
    # ax.scatter(x1,x2,c='k')
    # ax.scatter(sen1,sen2,c='r')
    daftarSSE.append(SSE)
    print(bb, SSE)
plt.plot(daftarSSE)
# plt.show()
# avg = []
# for i in range(len(kelompok)):
#     for k in range(len(kelompok[i])):
#         avg.append([0,0])
#         for titik in kelompok[i]:
#             avg[k][0] += titik[0]
#             avg[k][1] += titik[1]
#     pr4int (avg)/
