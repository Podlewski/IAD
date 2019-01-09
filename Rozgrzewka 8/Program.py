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
        i = list(map(float, row[0].split(" ")))
        outX.append(i[0:-1])
        outY.append(i[-1])
    return outX, outY


def k(d, sigm):
    exp = m.exp(-1 * m.pow(d, 2) / (2 * m.pow(sigm, 2)))
    return float(1 / (m.sqrt(2 * m.pi) * sigm) * exp)


def f(x, arrC, arrS, arrW, w0):
    sum = 0
    for i in range(len(arrC)):
        d = m.fabs(x - arrC[i])
        sum += arrW[i] * k(d, arrS[i])
    return w0 + sum


def f_single(x, c, s, w, w0):
    d = m.fabs(x - c)
    return w0 + w * k(d, s)


def new_w(w, c, ):
    alfa = 0.1
    w = w - alfa * (1/c)
    pass


def q(arrX, arrY, arrC, arrS, arrW, w0):
    n = len(arrX)
    q = 1/2*n
    pass


file = open(sys.argv[1], "r")

trrX, trrY = readFile(file)

a = min(trrX)   # min X
b = max(trrX)   # max X
c = int(sys.argv[2])

arrC = np.empty(c)
arrS = np.empty(c)
arrW = np.empty(c)
w0 = rand.uniform(-4, 4)


for i in range(0, c):
    arrC[i] = rand.uniform(a, b)
    arrS[i] = rand.uniform(0.5, 1)
    arrW[i] = rand.uniform(-4, 4)


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
plt.scatter(trrX, trrY, color='g', s=5)

plt.tight_layout()
plt.grid()

fileName = 'out' + str(c) + '.png'
plt.savefig(fileName, format='png')
