import math
# import numpy as np


class Algorithm:

    '''
        closest_neurone

        Przyjmuje:  tablice nrrX oraz nrrY neuronow, pojedynczy punkt tX, tY
        Zwraca: identyfikator najblizszego neuronu dla danego punktu treningowego
    '''
    def closest_neurone(self, nrrX, nrrY, tX, tY):
        dMin = 100
        for n in range(len(nrrX)):
            d = math.sqrt(pow((nrrX[n] - tX), 2) + pow((nrrY[n] - tY), 2))
            if d < dMin:
                dMin = d
                closest_neurone_number = n
        return closest_neurone_number

    '''
        count_error

        Przyjmuje:  tablice nrrX oraz nrrY neuronow, tablice trrX oraz trrY danych treningowych
        Zwraca: blad obliczony na podstawie sumy odleglosci kazdego punktu treningowego od najblizszego
                neuronu podzielonego przez ilosc punktow treningowych
    '''
    def count_error(self, nrrX, nrrY, trrX, trrY):
        error = 0
        for a in range(len(trrX)):
            assign = self.closest_neurone(nrrX, nrrY, trrX[a], trrY[a])
            d = pow(trrX[a] - nrrX[assign], 2) + pow(trrY[a] - nrrY[assign], 2)
            error += math.sqrt(d)
        return error / len(trrX)
