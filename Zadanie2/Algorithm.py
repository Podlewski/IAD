import math
import copy as cp
import numpy as np


class Algorithm:

    '''
        closest_neurone

        Przyjmuje:  tablice nrrX oraz nrrY neuronow, pojedynczy punkt tX, tY
        Zwraca: indeks najblizszego neuronu dla danego punktu treningowego
    '''
    def closest_neurone(self, nrrX, nrrY, tX, tY):
        dMin = math.sqrt(pow((nrrX[0] - tX), 2) + pow((nrrY[0] - tY), 2))
        closest_neurone_id = 0
        for n in range(len(nrrX)):
            d = math.sqrt(pow((nrrX[n] - tX), 2) + pow((nrrY[n] - tY), 2))
            if d < dMin:
                dMin = d
                closest_neurone_id = n
        return closest_neurone_id

    '''
        neurones_ranking

        Przyjmuje:  tablice nrrX oraz nrrY neuronow, tablice trrX oraz trrY danych treningowych
        Zwraca: tablice rankingu neuronow (np jezeli neuron o indeksie 0 jest 7 w kolejnosci, to
                w 0 idenksie zwracanej tablicy znajdziemy wartosc 7)
    '''
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

    '''
        count_error

        Przyjmuje:  tablice nrrX oraz nrrY neuronow, tablice trrX oraz trrY danych treningowych
        Zwraca: blad obliczony na podstawie sumy odleglosci kazdego punktu treningowego od najblizszego
                neuronu podzielonego przez ilosc punktow treningowych
    '''
    def count_error(self, nrrX, nrrY, trrX, trrY):
        error = 0
        for t in range(len(trrX)):
            neurone_id = self.closest_neurone(nrrX, nrrY, trrX[t], trrY[t])
            d = pow(trrX[t] - nrrX[neurone_id], 2) + pow(trrY[t] - nrrY[neurone_id], 2)
            error += math.sqrt(d)
        return error / len(trrX)

    '''
        train

        Przyjmuje:  tablice nrrX oraz nrrY neuronow, tablice trrX oraz trrY danych treningowych
                    oraz dwie zmienne ktore sa niepotrzebne dla tego algorytmu
        Zwraca: oblicza nowe polozenie neuronow na podstawie algorytmu k-średnich
    '''
    def train(self, algorithm, nrrX, nrrY, trrX, trrY, parameters, it, olp):

        inactive_neurones = 0

        oldX = cp.deepcopy(nrrX)
        oldY = cp.deepcopy(nrrY)

        if algorithm == 'K':
            self.kohonen(nrrX, nrrY, trrX, trrY, parameters[0], parameters[1])

        if algorithm == 'G':
            if olp is True:
                self.neural_gas_olp(nrrX, nrrY, trrX, trrY, it)
            else:
                self.neural_gas(nrrX, nrrY, trrX, trrY, parameters[0], parameters[1])

        if algorithm == 'C':
            self.km_clustering(nrrX, nrrY, trrX, trrY)

        for n in range(len(nrrX)):
            if (math.fabs(oldX[n] - nrrX[n]) < 0.01):
                if (math.fabs(oldY[n] - nrrY[n]) < 0.01):
                    inactive_neurones += 1

        return inactive_neurones

    def kohonen(self, nrrX, nrrY, trrX, trrY, alpha, theta):
        for t in range(len(trrX)):
            neurone_id = self.closest_neurone(nrrX, nrrY, trrX[t], trrY[t])

            for i in range(neurone_id - int(theta), neurone_id + int(theta) + 1):
                if (i >= 0) and (i < len(nrrX)):
                    nrrX[i] = nrrX[i] + alpha * (trrX[t] - nrrX[i])
                    nrrY[i] = nrrY[i] + alpha * (trrY[t] - nrrY[i])

    def neural_gas(self, nrrX, nrrY, trrX, trrY, eta, lambd):
        for t in range(len(trrX)):
            neurones_ranking = self.neurones_ranking(nrrX, nrrY, trrX[t], trrY[t])

            for n in range(len(nrrX)):
                nrrX[n] = nrrX[n] + eta * math.exp((-1 * neurones_ranking[n]) / lambd) * (trrX[t] - nrrX[n])
                nrrY[n] = nrrY[n] + eta * math.exp((-1 * neurones_ranking[n]) / lambd) * (trrY[t] - nrrY[n])

    def neural_gas_olp(self, nrrX, nrrY, trrX, trrY, it):
        eta = 0.05 * pow(0.003 / 0.05, it / 20)
        tmp = len(nrrX) / 2
        lambd = (tmp * pow(0.01 / tmp, it / 20))/2

        self.train(nrrX, nrrY, trrX, trrY, eta, lambd)

    def km_clustering(self, nrrX, nrrY, trrX, trrY):
        newX = np.zeros((len(nrrX), 1))
        newY = np.zeros((len(nrrY), 1))
        counter = np.zeros((len(nrrY), 1))

        for t in range(len(trrX)):
            neurone_id = self.closest_neurone(nrrX, nrrY, trrX[t], trrY[t])
            newX[neurone_id] += trrX[t]
            newY[neurone_id] += trrY[t]
            counter[neurone_id] += 1

        for n in range(len(newX)):
            if counter[n] != 0:
                nrrX[n] = (newX[n] / counter[n])
                nrrY[n] = (newY[n] / counter[n])
