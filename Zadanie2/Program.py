#!/usr/bin/python

import copy as cp
import numpy as np

from Parser import Parser
from Functions import Functions

from Kohonen import Kohonen
from NeuralGas import NeuralGas
from KMClustering import KMClustering

Fun = Functions()

P = Parser()
P.parse()

algorithm = P.get_algorithm()
area_range, line_area, symetric_area = P.get_area_settings()
c_proxmity = P.get_charts_settings()
data_fn = P.get_data_file_name()
debug = P.get_debug()
error_cfn, history_cfn, vornoi_cfn = P.get_charts_file_name()
learning_par_1, learning_par_2 = P.get_lerning_parameters()
neurones = P.get_neurones()
own_learning_parameters = P.get_own_learning_parameters()
shapes = P.get_shapes()

name_suffix = ''

if algorithm == 'K':
    A = Kohonen()
    name_suffix += '_Koh'

if algorithm == 'G':
    A = NeuralGas()
    name_suffix += '_NG'

if algorithm == 'C':
    A = KMClustering()
    name_suffix += '_KMC'

# arrays of training points
trrX = []
trrY = []

# add "training shapes"
for s in range(len(shapes)):
    if s % 2 == 0:
        Fun.set_shape_pts(shapes[s], trrX, trrY, shapes[s+1])

iterations_array = []
quantization_error_array = []

if len(neurones) == 1:
    name_suffix += '_' + str(neurones[0])
else:
    name_suffix += '_X'

name_suffix += '_' + str(int(len((shapes))/2))

for n in range(len(neurones)):
    iteration = 0
    quantization_error = []

    # arrays of neurones
    nrrX = []
    nrrY = []

    # starting neuornes position
    if (line_area is False) and (symetric_area is False):
        Fun.random_neurones_position(nrrX, nrrY, neurones[n], area_range)
    if line_area is True:
        Fun.line_neurones_position(nrrX, nrrY, neurones[n])
    if symetric_area is True:
        Fun.symmetric_neurones_position(nrrX, nrrY, neurones[n])

    # if user want to plot will all past neuornes positions
    if history_cfn != '':
        nrrX_history = []
        nrrY_history = []
        for h in range(len(nrrX)):
            nrrX_history.append([])
            nrrY_history.append([])

    # inactive neurones "remembers"
    inactive_neurones = 0                   # cant start program with 0 neurones
    avg_inactive_neurones = 0
    min_inactive_neurones = neurones[n]     # higest posible value, surely to change

    while (inactive_neurones != neurones[n]):
        iteration += 1

        if history_cfn != '':
            for h in range(len(nrrX)):
                nrrX_history[h].append(nrrX[h])
                nrrY_history[h].append(nrrY[h])

        quantization_error.append(A.count_error(nrrX, nrrY, trrX, trrY))

        if own_learning_parameters is False:
            inactive_neurones = A.train(nrrX, nrrY, trrX, trrY, learning_par_1, learning_par_2)
        else:
            inactive_neurones = A.train_with_own_lp(nrrX, nrrY, trrX, trrY, iteration)

        avg_inactive_neurones += inactive_neurones

        if debug is True:
            print(str(iteration) + ' : ' + str(inactive_neurones))

        # eventually setting new min_inactive_neurones
        if min_inactive_neurones > inactive_neurones:
            min_inactive_neurones = cp.deepcopy(inactive_neurones)

    avg_inactive_neurones /= iteration

    iterations_array.append(iteration)
    quantization_error_array.append(quantization_error)

    if data_fn != '':
        data_to_save = ''

        if algorithm != 'C':
            data_to_save += str(learning_par_1) + ' '
            data_to_save += str(learning_par_2) + ' '

        # iterations starts from 1, because there are increased add beggining - so need to be it-1
        data_to_save += str(np.squeeze(quantization_error[iteration-1])) + ' '

        data_to_save += str(min_inactive_neurones) + ' '
        data_to_save += str(avg_inactive_neurones) + '\n'

        file_name = data_fn + name_suffix + '_D'
        Fun.save_in_file_adding(file_name, data_to_save)

if error_cfn != '':
    for n in range(len(neurones)):
        Fun.add_quantization_error_plot(iterations_array[n], quantization_error_array[n], neurones[n])

    file_name = error_cfn + name_suffix + '_E'
    Fun.save_quantization_error_chart(file_name, len(neurones))

if history_cfn != '':
    file_name = history_cfn + name_suffix + '_H'
    Fun.save_history_chart(file_name, nrrX_history, nrrY_history, trrX, trrY)

if vornoi_cfn != '':
    file_name = vornoi_cfn + name_suffix + '_V'
    Fun.save_vornoi_chart(file_name, nrrX, nrrY, trrX, trrY, c_proxmity)
