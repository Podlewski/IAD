import math
import copy as cp
import numpy as np

from Algorithm import Algorithm


class NeuralGas:

    def __init__(self):
        self.A = Algorithm()

    def count_error(self, nrrX, nrrY, trrX, trrY):
        # nrr - neuone array
        # trr - training array
        return self.A.count_error(nrrX, nrrY, trrX, trrY)

    def neurones_ranking(self, nrrX, nrrY, tX, tY):
        # orr - ranking of training points (trr - arrays of training poins)
        orr = np.zeros(len(nrrX))
        # drr - array with distance
        drr = []
        for n in range(len(nrrX)):
            drr.append(math.sqrt(pow((nrrX[n] - tX), 2) + pow((nrrY[n] - tY), 2)))
        # srr - sorted drr
        srr = cp.deepcopy(drr)
        srr.sort()
        for s in range(len(srr)):
            for d in range(len(drr)):
                if srr[s] == drr[d]:
                    orr[d] = s
        return orr

    def train(self, nrrX, nrrY, trrX, trrY, eta, lambd):
        inactive_neurones = 0

        oldX = cp.deepcopy(nrrX)
        oldY = cp.deepcopy(nrrY)

        for t in range(len(trrX)):
            assign = self.neurones_ranking(nrrX, nrrY, trrX[t], trrY[t])

            for n in range(len(nrrX)):
                nrrX[n] = nrrX[n] + eta * math.exp((-1 * assign[n]) / lambd) * (trrX[t] - nrrX[n])
                nrrY[n] = nrrY[n] + eta * math.exp((-1 * assign[n]) / lambd) * (trrY[t] - nrrY[n])

        for n in range(len(nrrX)):
            if (math.fabs(oldX[n] - nrrX[n]) < 0.01):
                if (math.fabs(oldY[n] - nrrY[n]) < 0.01):
                    inactive_neurones += 1
        return inactive_neurones

    def train_with_own_lp(self, nrrX, nrrY, trrX, trrY, it):
        eta = 0.05 * pow(0.003 / 0.05, it / 20)
        tmp = len(nrrX) / 2
        lambd = (tmp * pow(0.01 / tmp, it / 20))/2

        return self.train(nrrX, nrrY, trrX, trrY, eta, lambd)
