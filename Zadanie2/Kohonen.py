import math
import copy as cp

from Algorithm import Algorithm


class Kohonen:

    def __init__(self):
        self.A = Algorithm()

    def count_error(self, nrrX, nrrY, trrX, trrY):
        # nrr - neuone array
        # trr - training array
        return self.A.count_error(nrrX, nrrY, trrX, trrY)

    def train(self, nrrX, nrrY, trrX, trrY, alpha, theta):
        inactive_neurones = 0

        oldX = cp.deepcopy(nrrX)
        oldY = cp.deepcopy(nrrY)

        for t in range(len(trrX)):
            assign = self.A.closest_neurone(nrrX, nrrY, trrX[t], trrY[t])
            for i in range(assign - int(theta), assign + int(theta) + 1):
                if (i >= 0) and (i < len(nrrX)):
                    nrrX[i] = nrrX[i] + alpha * (trrX[t] - nrrX[i])
                    nrrY[i] = nrrY[i] + alpha * (trrY[t] - nrrY[i])

        for n in range(len(nrrX)):
            if (math.fabs(oldX[n] - nrrX[n]) < 0.01):
                if (math.fabs(oldY[n] - nrrY[n]) < 0.01):
                    inactive_neurones += 1

        return inactive_neurones
