#!/usr/bin/python

import math
import copy as cp
import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt


def Plot(it, prefix):
    plt.clf()
    plt.grid()
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)

    plotTitle = prefix + str(it) + ' epoka'
    plt.title(plotTitle)
    plt.scatter(arrX, arrY, color='k', s=3)


def RandomCirclePoints(arrX, arrY, x0, y0, r, maxIt):
    it = 0
    while it < maxIt:
        x = rand.uniform(x0-r, x0+r)
        y = rand.uniform(y0-r, y0+r)
        if math.sqrt(pow(x0 - x, 2) + pow(y0 - y, 2)) <= r:
            it += 1
            arrX.append(x)
            arrY.append(y)


def RandomSquarePoints(arrX, arrY, x0, y0, r, it):
    for i in range(it):
        arrX.append(rand.uniform(x0-r, x0+r))
        arrY.append(rand.uniform(y0-r, y0+r))


def ClosestPoint(x, y, krrX, krrY):
    dMin = 100
    for k in range(len(krrX)):
        d = math.sqrt(pow((krrX[k] - x), 2) + pow((krrY[k] - y), 2))
        if d < dMin:
            dMin = d
            cPoint = k
    return cPoint


def CountError(arrX, arrY, krrX, krrY):
    error = 0
    for a in range(len(arrX)):
        assign = ClosestPoint(arrX[a], arrY[a], krrX, krrY)
        error += pow(arrX[a] - krrX[assign], 2)
        error += pow(arrY[a] - krrY[assign], 2)
    return error / len(arrX)


def AssingPoint(x, y, krrX, krrY):
    # orr - ranking array
    orr = np.zeros(len(krrX))
    # drr - array of distance
    drr = []
    for k in range(len(krrX)):
        drr.append(math.sqrt(pow((krrX[k] - x), 2) + pow((krrY[k] - y), 2)))
    # srr - sorted drr
    srr = cp.deepcopy(drr)
    srr.sort()
    for s in range(len(srr)):
        for d in range(len(drr)):
            if srr[s] == drr[d]:
                orr[d] = s
    return orr


def CountEta(it):
    eMax = 0.05
    eMin = 0.003
    k = it
    kMax = 20
    return eMax * pow(eMin / eMax, k / kMax)


def CountLambda(it, quantity):
    lMax = quantity / 2
    lMin = 0.01
    k = it
    kMax = 20
    return lMax * pow(lMin / lMax, k / kMax)


def NeuralGas(arrX, arrY, krrX, krrY, it):
    eta = CountEta(it)
    lambd = CountLambda(it, len(krrX))/2

    oldX = cp.deepcopy(krrX)
    oldY = cp.deepcopy(krrY)
    for a in range(len(arrX)):
        assign = AssingPoint(arrX[a], arrY[a], krrX, krrY)

        for k in range(len(krrX)):
            krrX[k] = krrX[k] + eta * math.exp((-1 * assign[k]) / lambd) * (arrX[a] - krrX[k])
            krrY[k] = krrY[k] + eta * math.exp((-1 * assign[k]) / lambd) * (arrY[a] - krrY[k])

    for k in range(len(krrX)):
        if (math.fabs(oldX[k] - krrX[k]) > 0.01):
            if (math.fabs(oldY[k] - krrY[k]) > 0.01):
                return False
    return True


arrX = []
arrY = []

krrX = []
krrY = []
error = []

RandomCirclePoints(arrX, arrY, -3, 0, 2, 100)
RandomCirclePoints(arrX, arrY, 3, 0, 2, 100)
RandomSquarePoints(krrX, krrY, 0, 0, 10, 10)

# fig size
figure = plt.gcf()
figure.set_size_inches(7, 7)

it = 0
condition = False

while condition is False:
    it += 1

    Plot(it, '')
    fileName = 'Results/' + str(it) + '.png'
    plt.scatter(krrX, krrY, color='r', s=20)
    plt.savefig(fileName, format='png')

    error.append(CountError(arrX, arrY, krrX, krrY))
    condition = NeuralGas(arrX, arrY, krrX, krrY, it)


plt.clf()
plt.grid()
plt.xlabel('Iteracja')
plt.ylabel('Błąd kwantyzacji')
errX = np.arange(1, it+1)
errY = np.array(error)
plt.plot(errX, errY)
fileName = 'out.png'
plt.savefig(fileName, format='png')
