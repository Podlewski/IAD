import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi as Vornoi, voronoi_plot_2d as voronoi_plot_2d


class Saver:

    def add_quantization_error_plot(self, it, err, neurones):

        iterations = np.arange(1, it+1)
        error = np.array(err)

        # set label title
        labelTitle = str(neurones) + ' neurony'
        if 1 == neurones:
            labelTitle = str(neurones) + ' neuron'
        if 4 < neurones:
            labelTitle = str(neurones) + ' neuronów'

        plt.plot(iterations, error, label=labelTitle)

    def save_quantization_error_chart(self, name, iterations, errors, neurones):
        for n in range(len(neurones)):
            self.add_quantization_error_plot(iterations[n], errors[n], neurones[n])

        # add legend if needed
        if len(neurones) > 1:
            plt.legend(title='Liczba neuronow:')

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

        for n in range(len(nrrX)):
            # smoothly highlighting every neurones positions
            plt.scatter(nrrX[n], nrrY[n], color='#ffb3b3', s=15)

            # highlighting first and last neurones positions
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

    def save_vornoi_chart(self, name, nrrX, nrrY, trrX, trrY, connect_neurones):
        plt.clf()   # blank chart

        # Vornoi is not working for 2 points, so this stupid fix need to be there:
        if len(nrrX) == 2:
            nrrX.append(100)
            nrrY.append(100)

        nrr = np.column_stack((nrrX, nrrY))         # concatenate neurone arrays of X and Y for vornoi
        vor = Vornoi(nrr)
        voronoi_plot_2d(vor, show_points=False, show_vertices=False, line_colors='#999999')

        # scatter with training points and neurones
        plt.scatter(trrX, trrY, color='k', s=3)
        plt.scatter(nrrX, nrrY, color='r', s=30)

        if connect_neurones is True:
            plt.plot(nrrX, nrrY, color='r')

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
