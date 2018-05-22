#!/usr/bin/python

import csv
import sys
import math as m
import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt


def readFile(in_file):
    reader = csv.reader(in_file)
    outX = []
    outY = []
    for row in reader:
        i = list(map(float, row[0].split(";")))
        outX.append(i[0:-1])
        outY.append(i[-1])
    return outX, outY


def k(d, sigm):
    exp = m.exp(-1 * m.pow(d, 2) / (2 * m.pow(sigm, 2)))
    return float(1 / (m.sqrt(2 * m.pi) * sigm) * exp)


file = open(sys.argv[1], "r")

arrX, arrY = readFile(file)

a = min(arrX)   # min X
b = max(arrX)   # max X
c = int(sys.argv[2])

arrC = np.empty(c)
arrS = np.empty(c)
arrW = np.empty(c)
w0 = rand.uniform(-4, 4)

for i in range(0, c):
    arrC[i] = rand.uniform(a, b)
    arrS[i] = rand.uniform(0.1, 0.5)
    arrW[i] = rand.uniform(-4, 4)

arrX = np.linspace(0, 10, 1001)
arrY = np.zeros(1001)


for i in range(len(arrC)):
    y = np.empty(1001)
    for x in range(len(arrX)):
        d = m.fabs(arrX[x] - arrC[i])
        y[x] = w0 + arrW[i] * k(d, arrS[i])
    y = np.array(y)
    plt.plot(arrX, y, color='r')

for x in range(len(arrX)):
    sum = 0
    for i in range(len(arrC)):
        d = m.fabs(arrX[x] - arrC[i])
        sum += arrW[i] * k(d, arrS[i])
    arrY[x] = w0 + sum

plt.plot(arrX, arrY, color='k')

plt.tight_layout()
plt.grid()

fileName = 'out' + str(c) + '.png'
plt.savefig(fileName, format='png')
