#!/usr/bin/python

import csv
import sys
import numpy as np
import matplotlib.pyplot as plt


def derivative(x, y):
    return (f(x) - y) * f(x) * (1 - f(x))


def e(x, y):
    sigma = 0
    for j in range(ammount):
        sigma += pow((f(x[j]) - y[j]), 2)
    return sigma/(2 * ammount)


def f(x):
    return 1/(1+np.exp(-1 * (np.inner(x, w) + w0)))


def readFile(in_file):
    reader = csv.reader(in_file)
    outX = []
    outY = []
    for row in reader:
        i = list(map(float, row[0].split(";")))
        outX.append(i[0:-1])
        outY.append(i[-1])
    return outX, outY


inFile = open(sys.argv[1], "r")
outFile = open(sys.argv[2], 'w')

arrX = []
arrY = []
arrX, arrY = readFile(inFile)

error = 1
errX = []
errY = []

alpha = 1
ammount = len(arrX)
size = len(arrX[0])
it = 0

w0 = np.random.uniform(-1, 1)
w = []
for i in range(size):
    w.append(np.random.uniform(-1, 1))


while error > pow(10, -5):
    sigma = 0
    for j in range(ammount):
        sigma += derivative(arrX[j], arrY[j])
    w0 -= alpha * 1/ammount * sigma

    for i in range(size):
        sigma = 0
        for j in range(ammount):
            sigma += derivative(arrX[j], arrY[j]) * arrX[j][i]
        w[i] -= alpha * sigma / ammount

    error = e(arrX, arrY)
    it += 1
    errY.append(error)
    errX.append(it)

    if it % 10000 == 0:
        print(error)

outFile.write(str(w0))
for i in range(size):
    outFile.write("\n")
    outFile.write(str(w[i]))

qChName = "Quality " + sys.argv[1].split(".")[0][-1]
qFiName = "quality" + sys.argv[1].split(".")[0][-1] + ".png"

plt.grid()
plt.yscale("log")
plt.xscale('linear', basex=1000000)
plt.plot(errX, errY)
plt.title(qChName)
plt.savefig(qFiName)
plt.show()

inFile.close()
outFile.close()
