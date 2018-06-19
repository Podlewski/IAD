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
        distance_min = math.sqrt(pow((nrrX[0] - tX), 2) + pow((nrrY[0] - tY), 2))
        closest_neurone_id = 0
        for n in range(len(nrrX)):
            distance = math.sqrt(pow((nrrX[n] - tX), 2) + pow((nrrY[n] - tY), 2))
            if (distance < distance_min and self.prr[n] > self.p_hold):
                distance_min = distance
                closest_neurone_id = n

        self.prr[closest_neurone_id] = max(self.prr[closest_neurone_id] - self.p_hold, self.p_min)
        for p in range(len(self.prr)):
            if (p != closest_neurone_id):
                self.prr[p] = min(self.p_max, self.prr[p] + self.p_diff)

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
        set_tiredness

        Przyjmuje:  wartosc true/false, ilosc neuronow i algorytm
    '''
    def set_tiredness(self, tiredness, neurones, algorithm):
        if (tiredness is True):
            self.p_hold = 0.85
        else:
            self.p_hold = 0
        self.p_max = 1
        self.p_min = 0
        self.p_diff = 1/len(neurones)

        self.prr = np.ones(len(neurones))

    '''
        closest_neurone_for_error

        Przyjmuje:  tablice nrrX oraz nrrY neuronow, pojedynczy punkt tX, tY
        Zwraca: indeks najblizszego neuronu dla danego punktu treningowego
    '''
    def closest_neurone_for_error(self, nrrX, nrrY, tX, tY):
        distance_min = math.sqrt(pow((nrrX[0] - tX), 2) + pow((nrrY[0] - tY), 2))
        closest_neurone_id = 0
        for n in range(len(nrrX)):
            distance = math.sqrt(pow((nrrX[n] - tX), 2) + pow((nrrY[n] - tY), 2))
            if (distance < distance_min):
                distance_min = distance
                closest_neurone_id = n
        return closest_neurone_id

    '''
        count_error

        Przyjmuje:  tablice nrrX oraz nrrY neuronow, tablice trrX oraz trrY danych treningowych
        Zwraca: blad obliczony na podstawie sumy odleglosci kazdego punktu treningowego od najblizszego
                neuronu podzielonego przez ilosc punktow treningowych
    '''
    def count_error(self, nrrX, nrrY, trrX, trrY):
        error = 0
        for t in range(len(trrX)):
            neurone_id = self.closest_neurone_for_error(nrrX, nrrY, trrX[t], trrY[t])
            d = pow(trrX[t] - nrrX[neurone_id], 2) + pow(trrY[t] - nrrY[neurone_id], 2)
            error += math.sqrt(d)
        return error / len(trrX)

    '''
        train

        Przyjmuje:  tablice nrrX oraz nrrY neuronow, t/f zmeczenia, tablice trrX oraz trrY
                    danych treningowych oraz dwie zmienne ktore sa niepotrzebne dla tego algorytmu
        Zwraca: oblicza nowe polozenie neuronow na podstawie algorytmu k-średnich
    '''
    def train(self, algorithm, nrrX, nrrY, tiredness, trrX, trrY, parameters, it, olp):
        inactive_neurones = 0

        self.set_tiredness(tiredness, nrrX)

        oldX = cp.deepcopy(nrrX)
        oldY = cp.deepcopy(nrrY)

        if algorithm == 'R':
            self.kohonen_rec(nrrX, nrrY, trrX, trrY, parameters[0], parameters[1])

        if algorithm == 'K':
            if olp is True:
                self.kohonen_gauss_olp(nrrX, nrrY, trrX, trrY, it)
            else:
                self.kohonen_gauss(nrrX, nrrY, trrX, trrY, parameters[0], parameters[1])

        if algorithm == 'G':
            if olp is True:
                self.neural_gas_olp(nrrX, nrrY, trrX, trrY, it)
            else:
                self.neural_gas(nrrX, nrrY, trrX, trrY, parameters[0], parameters[1])

        if algorithm == 'C':
            self.km_clustering(nrrX, nrrY, trrX, trrY)

        for n in range(len(nrrX)):
            if (oldX[n] == nrrX[n] and oldY[n] == nrrY[n]):
                inactive_neurones += 1

        return inactive_neurones

    def kohonen_rec(self, nrrX, nrrY, trrX, trrY, alpha, theta):
        for t in range(len(trrX)):
            neurone_id = self.closest_neurone(nrrX, nrrY, trrX[t], trrY[t])

            for i in range(neurone_id - int(theta), neurone_id + int(theta) + 1):
                if (i >= 0) and (i < len(nrrX)):
                    nrrX[i] = nrrX[i] + alpha * (trrX[t] - nrrX[i])
                    nrrY[i] = nrrY[i] + alpha * (trrY[t] - nrrY[i])

    def kohonen_gauss(self, nrrX, nrrY, trrX, trrY, eta, lambd):
        for t in range(len(trrX)):
            neurone_id = self.closest_neurone(nrrX, nrrY, trrX[t], trrY[t])

            for i in range(len(nrrX)):
                d = math.fabs(neurone_id - i)
                g = math.exp(-1 * math.pow(d, 2) / (2 * lambd * lambd))
                nrrY[i] = nrrY[i] + eta * g * (trrY[t] - nrrY[i])
                nrrX[i] = nrrX[i] + eta * g * (trrX[t] - nrrX[i])

    def kohonen_gauss_olp(self, nrrX, nrrY, trrX, trrY, it):
        eta = 0.3
        lambd = max(math.exp(-1 * it/75), 0.1)
        self.kohonen_rec(nrrX, nrrY, trrX, trrY, eta, lambd)

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

        self.neural_gas(nrrX, nrrY, trrX, trrY, eta, lambd)

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
