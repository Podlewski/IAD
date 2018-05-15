#!/usr/bin/python

import numpy as np

from Algorithm import Algorithm
from Parser import Parser
from Saver import Saver
from Setter import Setter

Alg = Algorithm()
Par = Parser()
Sav = Saver()
Set = Setter()

Par.parse()

algorithm = Par.get_algorithm()
area_range, line_area, symetric_area = Par.get_area_settings()
connect_neurones = Par.get_charts_settings()
data_fn = Par.get_data_file_name()
debug = Par.get_debug()
error_cfn, history_cfn, vornoi_cfn = Par.get_charts_file_name()
learning_parameters = Par.get_lerning_parameters()
neurones = Par.get_neurones()
own_learning_parameters = Par.get_own_learning_parameters()
shapes, shapes_settings = Par.get_shapes()

# get name_suffix
name_suffix = Set.set_title(algorithm, neurones, len(shapes))

# arrays of training points
trrX = []
trrY = []

# add "training shapes"
for s in range(len(shapes)):
    Set.set_shape_pts(trrX, trrY, shapes[s], shapes_settings[s])

# create arrays for iterations and quantization_errors for specific neuones quantity
iterations_array = []
quantization_error_array = []

for n in range(len(neurones)):
    iteration = 0
    quantization_error = []

    # arrays of neurones
    nrrX = []
    nrrY = []

    # starting neuornes position
    if (line_area is False) and (symetric_area is False):
        Set.random_neurones_position(nrrX, nrrY, neurones[n], area_range)
    if line_area is True:
        Set.line_neurones_position(nrrX, nrrY, neurones[n])
    if symetric_area is True:
        Set.symmetric_neurones_position(nrrX, nrrY, neurones[n])

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

        quantization_error.append(Alg.count_error(nrrX, nrrY, trrX, trrY))

        inactive_neurones = Alg.train(algorithm, nrrX, nrrY, trrX, trrY,
                                      learning_parameters, iteration, own_learning_parameters)

        avg_inactive_neurones += inactive_neurones

        if debug is True:
            print(str(iteration) + ' : ' + str(inactive_neurones))

        # eventually setting new min_inactive_neurones
        if min_inactive_neurones > inactive_neurones:
            min_inactive_neurones = inactive_neurones

    avg_inactive_neurones /= iteration

    iterations_array.append(iteration)
    quantization_error_array.append(quantization_error)

    if data_fn != '':
        data_to_save = ''

        if algorithm != 'C':
            data_to_save += str(learning_parameters[0]) + ' '
            data_to_save += str(learning_parameters[1]) + ' '

        # iterations starts from 1, because there are increased add beggining - so need to be it-1
        data_to_save += str(np.squeeze(quantization_error[iteration-1])) + ' '

        data_to_save += str(min_inactive_neurones) + ' '
        data_to_save += str(avg_inactive_neurones) + '\n'

        file_name = data_fn + name_suffix + '_D'
        Sav.save_in_file_adding(file_name, data_to_save)

if error_cfn != '':
    file_name = error_cfn + name_suffix + '_E'
    Sav.save_quantization_error_chart(file_name, iterations_array, quantization_error_array, neurones)

if history_cfn != '':
    file_name = history_cfn + name_suffix + '_H'
    Sav.save_history_chart(file_name, nrrX_history, nrrY_history, trrX, trrY)

if vornoi_cfn != '':
    file_name = vornoi_cfn + name_suffix + '_V'
    Sav.save_vornoi_chart(file_name, nrrX, nrrY, trrX, trrY, connect_neurones)
