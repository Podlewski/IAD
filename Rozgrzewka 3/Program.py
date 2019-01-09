#!/usr/bin/python

import csv
import sys
import matplotlib.pyplot as plt
from NeuralNetwork import NeuralNetwork


def readFile(in_file):
    reader = csv.reader(in_file)
    outX = []
    outY = []
    for row in reader:
        i = list(map(float, row[0].split(" ")))
        outX.append(i[0:-1])
        outY.append(i[-1])
    return outX, outY


def countError(x, y):
    sigma = 0
    for j in range(sizeK):
        sigma += pow((x[j] - y[j]), 2)
    return sigma/(2 * sizeK)


inFile = open(sys.argv[1], "r")

arrU = []
arrV = []
arrU, arrV = readFile(inFile)

inFile.close()

sizeI = len(arrU[0])
sizeK = len(arrU)

settings = (0, 0, 0, 0)
neurone = NeuralNetwork(sizeI, 2, 1, 0.1, settings)

error = 1
errX = []
errY = []
it = 0

while error > pow(10, -5):
    for k in range(sizeK):
        neurone.train(arrU[k], arrV[k])

    err = []
    for k in range(sizeK):
        err.append(neurone.query(arrU[k]))

    error = countError(err, arrV)
    it += 1
    errY.append(error)
    errX.append(it)

    if it % 10000 == 0:
        print(error)

qChName = "Quality " + sys.argv[1].split(".")[0][-1]
qFiName = "quality" + sys.argv[1].split(".")[0][-1] + ".png"

plt.grid()
plt.yscale("log")
plt.xscale('linear', basex=1000000)
plt.plot(errX, errY)
plt.title(qChName)
plt.savefig(qFiName)
# plt.show()
