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

def sse(x0,y0):
    k = 2
    for i in k:
