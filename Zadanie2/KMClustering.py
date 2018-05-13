import math
import copy as cp
import numpy as np

from Algorithm import Algorithm


class KMClustering:

    def __init__(self):
        self.A = Algorithm()

    def count_error(self, nrrX, nrrY, trrX, trrY):
        # nrr - neuone array
        # trr - training array
        return self.A.count_error(nrrX, nrrY, trrX, trrY)

    '''
        train

        Przyjmuje:  tablice nrrX oraz nrrY neuronow, tablice trrX oraz trrY danych treningowych
                    oraz dwie zmienne ktore sa niepotrzebne dla tego algorytmu
        Zwraca: oblicza nowe polozenie neuronow na podstawie algorytmu k-średnich
    '''
    def train(self, nrrX, nrrY, trrX, trrY, useless, also_useless):
        inactive_neurones = 0

        oldX = cp.deepcopy(nrrX)
        oldY = cp.deepcopy(nrrY)

        newX = np.zeros((len(nrrX), 1))
        newY = np.zeros((len(nrrY), 1))
        counter = np.zeros((len(nrrY), 1))

        for t in range(len(trrX)):
            assigned_neruone = self.A.closest_neurone(nrrX, nrrY, trrX[t], trrY[t])
            newX[assigned_neruone] += trrX[t]
            newY[assigned_neruone] += trrY[t]
            counter[assigned_neruone] += 1

        for n in range(len(newX)):
            if counter[n] != 0:
                nrrX[n] = (newX[n] / counter[n])
                nrrY[n] = (newY[n] / counter[n])

            if (math.fabs(oldX[n] - nrrX[n]) < 0.01):
                if (math.fabs(oldY[n] - nrrY[n]) < 0.01):
                    inactive_neurones += 1

        return inactive_neurones
