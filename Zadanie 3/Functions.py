import csv
import numpy as np
import matplotlib.pyplot as plt


class Functions:

    def readFile(fileName):
        inFile = open(fileName, 'r')
        reader = csv.reader(inFile)
        arrX = []
        arrY = []
        for row in reader:
            i = list(map(float, row[0].split(" ")))
            arrX.append(i[0])
            arrY.append(i[1])
        inFile.close()
        return arrX, arrY

    def checkCondition(it, it_val, err, err_val):
        if 0 != it_val:
            if it >= pow(10, it_val):
                return False
        else:
            if err < pow(10, (-1 * err_val)):
                return False
        return True

    # saving data in file
    def save_in_file(name, data_to_save):
        file = open(name + '.txt', 'a')
        file.write(data_to_save)
        file.close()

    # normal plot
    def add_plot(function, number, bool=True, text=""):
        if bool is True:
            labelTitle = str(number) + ' neurony'
            if 1 == number:
                labelTitle = str(number) + ' neuron'
            if 4 < number:
                labelTitle = str(number) + ' neuronów'
        else:
            labelTitle = str(number) + ' iteracje'
            if 1 == number:
                labelTitle = str(number) + ' iteracja'
            if 4 < number:
                labelTitle = str(number) + ' iteracji'

        if text != "":
            labelTitle = text

        array_x = np.arange(-4, 4, 0.01)
        array_y = []
        for x in range(len(array_x)):
            array_y.append(np.squeeze(function(array_x[x])))

        plt.plot(array_x, array_y, label=labelTitle)

    def draw_plot(file_name, arr_x, arr_y, brr_x, brr_y):
        plt.scatter(arr_x, arr_y, s=3, color='k', label='Punkty treningowe')
        plt.scatter(brr_x, brr_y, s=0.5, color='c', label='Punkty testowe')

        plt.legend()

        # figure size
        figure = plt.gcf()
        figure.set_size_inches(4.5, 4.5)
        figure.tight_layout()

        plt.savefig(file_name + '.png', format='png', dpi=400)

    def draw_hist_plot(file_name):
        plt.legend(title='Iteracje:')

        # figure size
        figure = plt.gcf()
        figure.set_size_inches(4.5, 4.5)
        figure.tight_layout()

        plt.savefig(file_name + '.png', format='png', dpi=400)

    def add_rad_plot(n, function, scalar, number, bool=True):
        array_x = np.arange(-4, 4, 0.01)
        array_y = []
        for x in range(len(array_x)):
            array_y.append(np.squeeze(function(n, array_x[x]) * scalar))

        if n == 0:
            plt.plot(array_x, array_y, color='m', linewidth=0.5, label='Funkcje radialne')
        else:
            plt.plot(array_x, array_y, color='m', linewidth=0.5)
