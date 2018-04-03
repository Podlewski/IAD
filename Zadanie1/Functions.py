import csv
import numpy as np
import matplotlib.pyplot as pltE
import matplotlib.pyplot as pltL
import matplotlib.pyplot as pltT
import math as m


class Functions:

    def readFile(fileName, x, y):
        inFile = open(fileName, 'r')
        reader = csv.reader(inFile)
        arrX = []
        arrY = []
        for row in reader:
            i = list(map(float, row[0].split(" ")))
            arrX.append(i[0:x])
            arrY.append(i[-y:len(i)])
        inFile.close()
        return arrX, arrY

    def translate(translateFile, arrY):
        trFile = open(translateFile, 'r')
        reader = csv.reader(trFile)
        Y = []
        trY = []
        for row in reader:
            i = list(map(float, row[0].split(" ")))
            Y.append(i[0])
            trY.append(i[1:len(i)])
        for arrRow in range(len(arrY)):
            for trRow in range(len(Y)):
                if arrY[arrRow][0] == (Y[trRow]):
                    arrY[arrRow] = trY[trRow]
        trFile.close()
        return arrY

    def countMSE(x, y):
        sigma = 0
        for j in range(len(x)):
            for i in range(len(x[j])):
                sigma += pow(((x[j][i]) - y[j][i]), 2)
        return sigma/(2 * len(x) * len(x[0]))

    def countSD(x, y):
        sigma = 0
        for j in range(len(x)):
            for i in range(len(x[j])):
                sigma += pow(((x[j][i]) - y[j][i]), 2)
        return m.sqrt(sigma/(len(x) * len(x[0] - 1)))

    def checkCondition(it, itVal, err, errVal):
        if 0 != itVal:
            if it >= pow(10, itVal):
                return False
        else:
            if err < pow(10, (-1 * errVal)):
                return False
        return True

    def getTitle(args):
        subTitle = 'Warunek stopu: '
        if 0 != args.itValue:
            subTitle += str(pow(10, args.itValue)) + ' iteracji'
        else:
            subTitle += 'błąd ' + str(pow(10, (-1 * args.erValue)))
        subTitle += ', krok ' + str(args.alpha)
        if args.bias is True:
            subTitle += ', bias'
        else:
            subTitle += ', brak biasu'
        if 0 != args.beta:
            subTitle += ', momentum (krok ' + str(args.beta) + ')'
        else:
            subTitle += ', brak momentum'
        if 1 == len(args.hidNeurones):
            hiddenTitle = str(args.hidNeurones[0]) + ' neurony'
            if 1 == args.hidNeurones[0]:
                hiddenTitle = str(args.hidNeurones[0]) + ' neuron'
            if 4 < args.hidNeurones[0]:
                hiddenTitle = str(args.hidNeurones[0]) + ' neuronów'
            subTitle += ', ' + hiddenTitle

        return subTitle

    def saveHidden(fileName, arrX, arrW):
        hidFile = open(fileName, 'a')
        for k in range(len(arrX)):
            hidFile.write(str(np.squeeze(arrX[k])) + ' ; ' +
                          str(np.squeeze(arrW[k])) + '\n')
        hidFile.close()

    def saveResults(fileName, alpha, beta, itValue, it, error):
        resFile = open(fileName, 'a')
        resMessage = str(alpha) + ' ' + str(beta)
        if 0 != itValue:
            resMessage += ' ' + str(error)
        else:
            resMessage += ' ' + str(it)
        resMessage += '\n'
        resFile.write(resMessage)
        resFile.close()

    def saveResultsExtra(fileName, neurones, sDev1, sDev2, itValue, it, error):
        resFile = open(fileName, 'a')
        resMessage = str(neurones)
        if 0 != itValue:
            resMessage += ' ' + str(error)
            resMessage += ' ' + str(sDev1) + ' ' + str(sDev2)
        else:
            resMessage += ' ' + str(it)
        resMessage += '\n'
        resFile.write(resMessage)
        resFile.close()

    def addPlotE(arrX, arrY, hidNeurones, extraLabel):
        labelTitle = str(hidNeurones) + ' neurony'
        if 1 == hidNeurones:
            labelTitle = str(hidNeurones) + ' neuron'
        if 4 < hidNeurones:
            labelTitle = str(hidNeurones) + ' neuronów'
        labelTitle += extraLabel
        pltE.plot(arrX, arrY, label=labelTitle)

    def drawPlotE(fileName, subTitle, plots, showPlot):
        pltE.grid()
        pltE.xlabel('Iteracje')
        pltE.ylabel('Błąd średniokwadratowy')
        pltE.yscale('log')

        mainTitle = 'Zmiana błędu średniokwadratowego'

        pltE.suptitle(mainTitle, fontsize=14, fontweight='bold')
        pltE.title(subTitle, fontsize=10)
        if 1 < plots:
            pltE.legend(title='Liczba neuronow\nw warstwie ukrytej:')

        # figure size
        figure = pltE.gcf()
        figure.set_size_inches(10, 5)

        pltE.savefig(fileName, format='png', dpi=1000)

        if showPlot is True:
            pltE.show()

    def addPlotL(query, it):
        if 1 == it:
            labelTitle = 'Przebieg poczatkowy'
        else:
            labelTitle = str(it) + ' iteracji'
        arrX = np.arange(-4, 4, 0.01)
        arrY = []
        for x in range(len(arrX)):
            arrY.append(np.squeeze(query(arrX[x])))
        pltL.plot(arrX, arrY, label=labelTitle)

    def drawPlotL(fileName, subTitle, showPlot):
        pltL.grid()
        pltT.xlabel('Oś X')
        pltT.ylabel('Oś Y')

        mainTitle = 'Zmiana funkcji realizowanej przez sieć w czasie'

        pltT.suptitle(mainTitle, fontsize=14, fontweight='bold')
        pltT.title(subTitle, fontsize=10)
        pltT.legend(title='Ilość iteracji:')

        # figure size
        figure = pltT.gcf()
        figure.set_size_inches(10, 5)

        pltT.savefig(fileName, format='png', dpi=1000)

        if showPlot is True:
            pltL.show()

    def addPlotT(query, hidNeurones):
        labelTitle = str(hidNeurones) + ' neurony'
        if 1 == hidNeurones:
            labelTitle = str(hidNeurones) + ' neuron'
        if 4 < hidNeurones:
            labelTitle = str(hidNeurones) + ' neuronów'
        arrX = np.arange(-4, 4, 0.01)
        arrY = []
        for x in range(len(arrX)):
            arrY.append(np.squeeze(query(arrX[x])))
        pltT.plot(arrX, arrY, label=labelTitle)

    def drawPlotT(fileName, subTitle, plots, arrX, arrY, brrX, brrY, showPlot):
        pltT.grid()
        pltT.xlabel('Oś X')
        pltT.ylabel('Oś Y')

        pltT.scatter(arrX, arrY, s=3, color='k', label='Punkty treningowe')
        pltT.scatter(brrX, brrY, s=0.5, color='c', label='Punkty testowe')

        mainTitle = 'Aproksymacja dla punktów trenignowych'

        pltT.suptitle(mainTitle, fontsize=14, fontweight='bold')
        pltT.title(subTitle, fontsize=10)
        if 1 < plots:
            pltT.legend(title='Liczba neuronow\nw warstwie ukrytej:')

        # figure size
        figure = pltT.gcf()
        figure.set_size_inches(10, 5)

        pltT.savefig(fileName, format='png', dpi=1000)

        if showPlot is True:
            pltT.show()
