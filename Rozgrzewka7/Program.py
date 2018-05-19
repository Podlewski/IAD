#!/usr/bin/python

import math
import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt
import sys


def d(x, y):
    return math.fabs(x-y)


def k(x, c, s):
    exp = math.exp(-1*d(x, c)*d(x, c)/2*s*s)
    return float(1/(math.sqrt(2*math.pi)*s) * exp)


def f(w0, x, arrC, arrS, arrW):
    suma = 0
    for c in range(len(arrC)):
        suma += arrW[c] * k(x, arrC[c], arrS[c])
    return w0 + suma


arrC = []
arrS = []   # sigma
arrW = []   # wages
w0 = rand.uniform(-4, 5)

for c in range(int(sys.argv[1])):
    arrC.append(rand.uniform(0, 11))
    arrW.append(rand.uniform(-4, 5))
    arrS.append(rand.uniform(0, 1))

arrX = np.linspace(0, 10, 1001)
arrY = np.zeros((1001, 1))

for i in range(len(arrC)):
    y = []
    for x in range(len(arrX)):
        y.append(f(w0, arrX[x], arrC, arrS, arrW))
    plt.plot(arrX, y, color='r')
    arrY += y

plt.clf()
plt.tight_layout()
plt.grid()

# plt.plot(arrX, arrY, color='k')

fileName = 'Results.png'
plt.savefig(fileName, format='png')
