#!/usr/bin/python

import sys
import math
import numpy as np
import numpy.random as rand
import matplotlib.pyplot as pltG
import matplotlib.pyplot as pltE


def randomCirclePoints(arrX, arrY, x0, y0, r, maxIt):
    it = 0
    while it < maxIt:
        x = rand.uniform(x0-r, x0+r)
        y = rand.uniform(y0-r, y0+r)
        if math.sqrt(pow(x0 - x, 2) + pow(y0 - y, 2)) < r:
            it += 1
            arrX.append(x)
            arrY.append(y)


def randomSquarePoints(arrX, arrY, x0, y0, r, it):
    for i in range(it):
        arrX.append(rand.uniform(x0-r, x0+r))
        arrY.append(rand.uniform(y0-r, y0+r))


def assingPoints(arrX, arrY, frr, krrX, krrY):
    for a in range(len(arrX)):
        dMin = 100
        for k in range(len(krrX)):
            d = math.sqrt(pow((krrX[k] - arrX[a]), 2) +
                          pow((krrY[k] - arrY[a]), 2))
            if d < dMin:
                dMin = d
                frr[a] = k


def quantizationError(arrX, arrY, frr, krrX, krrY):
    error = 0
    for a in range(len(arrX)):
        error += pow(arrX[a] - krrX[frr[a]], 2)
        error += pow(arrY[a] - krrY[frr[a]], 2)
    return error / len(arrX)


def kMeansClustering(arrX, arrY, frr, krrX, krrY):
    boolTab = []
    for k in range(len(krrX)):
        counter = 0
        newX = 0
        newY = 0
        for f in range(len(frr)):
            if k == frr[f]:
                newX += arrX[f]
                newY += arrY[f]
                counter += 1
        if counter != 0:
            if (krrX[k] == (newX / counter)) and (krrY[k] == (newY / counter)):
                boolTab.append(True)
            else:
                boolTab.append(False)
            krrX[k] = (newX / counter)
            krrY[k] = (newY / counter)
    bool = True
    for b in range(len(boolTab)):
        if boolTab[b] is False:
            bool = False
            break
    return bool


arrX = []
arrY = []
frr = []
err = []
krrX = []
krrY = []
quantityK = int(sys.argv[1])

randomCirclePoints(arrX, arrY, -3, 0, 2, 100)
randomCirclePoints(arrX, arrY, 3, 0, 2, 100)
for f in range(200):
    frr.append(0)
randomSquarePoints(krrX, krrY, 0, 0, 10, quantityK)

it = 0
condition = False
error = []

while condition is False:
    it += 1

    pltG.clf()
    pltG.tight_layout()
    pltG.xlim(-10, 10)
    pltG.ylim(-10, 10)
    pltG.grid()
    plotTitle = str(it) + ' iteracja'
    pltG.title(plotTitle)

    pltG.scatter(arrX, arrY, color='k', s=3)
    pltG.scatter(krrX, krrY, color='r', s=20)

    # fig size
    figure = pltG.gcf()
    figure.set_size_inches(7, 7)

    fileName = 'Results/' + str(it) + '.png'
    pltG.savefig(fileName, format='png')

    assingPoints(arrX, arrY, frr, krrX, krrY)
    error.append(quantizationError(arrX, arrY, frr, krrX, krrY))
    condition = kMeansClustering(arrX, arrY, frr, krrX, krrY)

pltE.clf()
pltE.tight_layout()
pltE.grid()
pltE.xlabel('Iteracja')
pltE.ylabel('Błąd kwantyzacji')
errX = np.arange(1, it+1)
errY = np.array(error)
pltE.plot(errX, errY)
fileName = 'Results/out' + str(quantityK) + '.png'
pltE.savefig(fileName, format='png')
