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


def AssingPoint(x, y, krrX, krrY):
    dMin = 100
    for k in range(len(krrX)):
        d = math.sqrt(pow((krrX[k] - x), 2) +
                      pow((krrY[k] - y), 2))
        if d < dMin:
            dMin = d
            assigment = k
    return assigment


def CountError(arrX, arrY, krrX, krrY):
    error = 0
    for a in range(len(arrX)):
        assign = AssingPoint(arrX[a], arrY[a], krrX, krrY)
        error += pow(arrX[a] - krrX[assign], 2)
        error += pow(arrY[a] - krrY[assign], 2)
    return error / len(arrX)


def SOM(arrX, arrY, krrX, krrY, alpha, theta):
    oldX = cp.deepcopy(krrX)
    oldY = cp.deepcopy(krrY)
    for a in range(len(arrX)):
        assign = AssingPoint(arrX[a], arrY[a], krrX, krrY)

        for i in range(assign - theta, assign + theta + 1):
            if (i >= 0) and (i < len(krrX)):
                krrX[i] = krrX[i] + alpha * (arrX[a] - krrX[i])
                krrY[i] = krrY[i] + alpha * (arrY[a] - krrY[i])

    for k in range(len(krrX)):
        if (math.fabs(oldX[k] - krrX[k]) > 0.01):
            if (math.fabs(oldY[k] - krrY[k]) > 0.01):
                return False
    return True


arrX = []
arrY = []
wtaX = []
wtaY = []
wtaError = []

RandomCirclePoints(arrX, arrY, -3, 0, 2, 100)
RandomCirclePoints(arrX, arrY, 3, 0, 2, 100)
RandomSquarePoints(wtaX, wtaY, 0, 0, 10, 10)

wtmX = cp.deepcopy(wtaX)
wtmY = cp.deepcopy(wtaY)
wtmError = []

# fig size
figure = plt.gcf()
figure.set_size_inches(7, 7)

wtaIt = 0
condition = False

while condition is False:
    wtaIt += 1
    alpha = 0.05
    if wtaIt > 2:
        alpha = 0.01

    Plot(wtaIt, 'WTA: ')
    fileName = 'WTA/' + str(wtaIt) + '.png'
    plt.plot(wtaX, wtaY, '-o', color='r')
    plt.savefig(fileName, format='png')

    theta = 0
    wtaError.append(CountError(arrX, arrY, wtaX, wtaY))
    condition = SOM(arrX, arrY, wtaX, wtaY, alpha, theta)

wtmIt = 0
condition = False
error = []

while condition is False:
    wtmIt += 1
    alpha = 0.05
    if wtmIt > 2:
        alpha = 0.01

    Plot(wtmIt, 'WTM: ')
    fileName = 'WTM/' + str(wtmIt) + '.png'
    plt.plot(wtmX, wtmY, '-o', color='r')
    plt.savefig(fileName, format='png')

    theta = 1
    wtmError.append(CountError(arrX, arrY, wtmX, wtmY))
    condition = SOM(arrX, arrY, wtmX, wtmY, alpha, theta)

plt.clf()
plt.grid()
plt.xlabel('Iteracja')
plt.ylabel('Błąd kwantyzacji')
errX = np.arange(1, wtaIt+1)
errY = np.array(wtaError)
plt.plot(errX, errY)
fileName = 'outWTA.png'
plt.savefig(fileName, format='png')

plt.clf()
plt.grid()
plt.xlabel('Iteracja')
plt.ylabel('Błąd kwantyzacji')
errX = np.arange(1, wtmIt+1)
errY = np.array(wtmError)
plt.plot(errX, errY)
fileName = 'outWTM.png'
plt.savefig(fileName, format='png')
