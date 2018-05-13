import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi as Vornoi, voronoi_plot_2d as voronoi_plot_2d


class Functions:

    # Functions used to generate random training points in shapes specified by user
    def set_shape_pts(self, shape, arrX, arrY, properties):
        x0 = properties[0]
        y0 = properties[1]
        maxIt = properties[-1]

        if shape == 'c':
            r = properties[2]
            self.random_circle_pts(arrX, arrY, x0, y0, r, maxIt)

        if shape == 'l':
            x1 = properties[2]
            y1 = properties[3]
            self.random_line_pts(arrX, arrY, x0, y0, x1, y1, maxIt)

        if shape == 'r':
            x1 = properties[2]
            y1 = properties[3]
            self.random_rectangle_pts(arrX, arrY, x0, y0, x1, y1, maxIt)

        if shape == 'w':
            r = properties[2]
            self.random_wheel_pts(arrX, arrY, x0, y0, r, maxIt)

    def random_circle_pts(self, arrX, arrY, x0, y0, r, maxIt):
        it = 0
        for it in range(maxIt):
            it += 1
            x = np.random.uniform(x0-r, x0+r)
            sign = np.random.randint(2)
            if sign == 0:
                sign = -1
            y = sign * math.sqrt(pow(r, 2) - pow(x - x0, 2)) - y0
            arrX.append(x)
            arrY.append(y)

    def random_line_pts(self, arrX, arrY, x1, y1, x2, y2, maxIt):
        it = 0
        for it in range(maxIt):
            it += 1
            x = np.random.uniform(x1, x2)
            y = (y2 - y1) / (x2 - x1) * x + (x2 * y1 - x1 * y2) / (x2 - x1)
            arrX.append(x)
            arrY.append(y)

    def random_rectangle_pts(self, arrX, arrY, x1, y1, x3, y3, maxIt):
        it = 0
        for it in range(maxIt):
            it += 1
            arrX.append(np.random.uniform(x1, x3))
            arrY.append(np.random.uniform(y1, y3))

    def random_wheel_pts(self, arrX, arrY, x0, y0, r, maxIt):
        it = 0
        while it < maxIt:
            x = np.random.uniform(x0-r, x0+r)
            y = np.random.uniform(y0-r, y0+r)
            if math.sqrt(pow(x0 - x, 2) + pow(y0 - y, 2)) <= r:
                it += 1
                arrX.append(x)
                arrY.append(y)

    def random_neurones_position(self, arrX, arrY, quaintity, area_range):
        for i in range(quaintity):
            arrX.append(np.random.uniform(area_range[0], area_range[1]))
            arrY.append(np.random.uniform(area_range[0], area_range[1]))

    def line_neurones_position(self, arrX, arrY, quantity):
        distance = 10 / (quantity - 1)
        currentY = 5
        for i in range(quantity):
            arrX.append(0)
            arrY.append(currentY)
            currentY -= distance

    def symmetric_neurones_position(self, arrX, arrY, quantity):
        distance = 10 / (quantity/2 - 1)
        currentY = 5
        for i in range(int(quantity / 2)):
            arrX.append(-5)
            arrY.append(currentY)
            currentY -= distance
        currentY = 5
        for i in range(int(quantity / 2)):
            arrX.append(5)
            arrY.append(currentY)
            currentY -= distance

    def add_quantization_error_plot(self, it, err, neurones):

        errX = np.arange(1, it+1)
        errY = np.array(err)

        # set label title
        labelTitle = str(neurones) + ' neurony'
        if 1 == neurones:
            labelTitle = str(neurones) + ' neuron'
        if 4 < neurones:
            labelTitle = str(neurones) + ' neuronów'

        plt.plot(errX, errY, label=labelTitle)

    def save_quantization_error_chart(self, name, neurones_quantity):
        # add legend if needed
        if neurones_quantity > 1:
            plt.legend(title='Liczba neuronow:')

        # chart axis range limits
        # plt.xlim(0, 15)
        # plt.ylim(0, 15)

        # file dimension
        figure = plt.gcf()
        figure.set_size_inches(4.5, 4.5)
        figure.tight_layout()

        plt.savefig(name + '.png', format='png', dpi=400)

    def save_history_chart(self, name, nrrX, nrrY, trrX, trrY):
        plt.clf()   # blank chart

        # scatter with training points
        plt.scatter(trrX, trrY, color='k', s=3)

        # plots with all neurones positions during learning
        for n in range(len(nrrX)):
            plt.plot(nrrX[n], nrrY[n], color='#ffb3b3')

        # highlighting first and last neurones positions
        for n in range(len(nrrX)):
            plt.scatter(nrrX[n], nrrY[n], color='#ffb3b3', s=15)
            plt.scatter(nrrX[n][0], nrrY[n][0], color='r', s=30)
            length = len(nrrX[n]) - 1
            plt.scatter(nrrX[n][length], nrrY[n][length], color='r', s=30)

        # chart axis range limits
        plt.xlim(-10, 10)
        plt.ylim(-10, 10)

        # file dimension
        figure = plt.gcf()
        figure.set_size_inches(4.5, 4.5)
        figure.tight_layout()

        plt.savefig(name + '.png', format='png', dpi=400)

    def save_vornoi_chart(self, name, nrrX, nrrY, trrX, trrY, chart_proximity):
        plt.clf()   # blank chart

        # Vornoi is not working for 2 points, so this stupid fix need to be there:
        if len(nrrX) == 2:
            nrrX.append(100)
            nrrY.append(100)

        nrr = np.column_stack((nrrX, nrrY))         # concatenate neurone arrays of X and Y
        vor = Vornoi(nrr)
        voronoi_plot_2d(vor, show_points=False, show_vertices=False, line_colors='#999999')

        # scatter with training points and neurones
        plt.scatter(trrX, trrY, color='k', s=3)
        if chart_proximity is False:
            plt.scatter(nrrX, nrrY, color='r', s=30)
        else:
            plt.plot(nrrX, nrrY, '-o', color='r')

        # chart axis range limits
        plt.xlim(-10, 10)
        plt.ylim(-10, 10)

        # file dimension
        figure = plt.gcf()
        figure.set_size_inches(4.5, 4.5)
        figure.tight_layout()

        plt.savefig(name + '.png', format='png', dpi=400)

    # saving data in file
    def save_in_file_adding(self, name, data_to_save):
        file = open(name + '.txt', 'a')
        file.write(data_to_save)
        file.close()
