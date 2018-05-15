import math
import numpy as np


class Setter:

    # Functions used to generate random training points in shapes specified by user
    def set_shape_pts(self, trrX, trrY, shape, properties):
        x0 = properties[0]
        y0 = properties[1]
        training_points_quantity = properties[-1]

        if shape == 'c':
            r = properties[2]
            self.random_circle_pts(trrX, trrY, x0, y0, r, training_points_quantity)

        if shape == 'l':
            x1 = properties[2]
            y1 = properties[3]
            self.random_line_pts(trrX, trrY, x0, y0, x1, y1, training_points_quantity)

        if shape == 'r':
            x1 = properties[2]
            y1 = properties[3]
            self.random_rectangle_pts(trrX, trrY, x0, y0, x1, y1, training_points_quantity)

        if shape == 'w':
            r = properties[2]
            self.random_wheel_pts(trrX, trrY, x0, y0, r, training_points_quantity)

    def random_circle_pts(self, trrX, trrY, x0, y0, r, maxIt):
        for i in range(0, maxIt):
            t = 2 * np.pi * np.random.uniform(0, 1)
            trrX.append(x0 + r * np.cos(t))
            trrY.append(x0 + r * np.sin(t))

    def random_line_pts(self, trrX, trrY, x1, y1, x2, y2, maxIt):
        for it in range(maxIt):
            x = np.random.uniform(x1, x2)
            y = (y2 - y1) / (x2 - x1) * x + (x2 * y1 - x1 * y2) / (x2 - x1)
            trrX.append(x)
            trrY.append(y)

    def random_rectangle_pts(self, trrX, trrY, x1, y1, x3, y3, maxIt):
        for it in range(maxIt):
            trrX.append(np.random.uniform(x1, x3))
            trrY.append(np.random.uniform(y1, y3))

    def random_wheel_pts(self, trrX, trrY, x0, y0, r, maxIt):
        for i in range(0, maxIt):
            t = 2 * np.pi * np.random.uniform(0, 1)
            R = np.random.uniform(0, r)
            trrX.append(x0 + R * np.cos(t))
            trrY.append(x0 + R * np.sin(t))

        it = 0
        while it < maxIt:
            x = np.random.uniform(x0-r, x0+r)
            y = np.random.uniform(y0-r, y0+r)
            if math.sqrt(pow(x0 - x, 2) + pow(y0 - y, 2)) <= r:
                it += 1
                trrX.append(x)
                trrY.append(y)

    def random_neurones_position(self, nrrX, nrrY, quaintity, area_range):
        for i in range(quaintity):
            nrrX.append(np.random.uniform(-1 * area_range[0], area_range[0]))
            nrrY.append(np.random.uniform(-1 * area_range[1], area_range[1]))

    def line_neurones_position(self, nrrX, nrrY, quantity):
        distance = 10 / (quantity - 1)
        currentY = 5

        for i in range(quantity):
            nrrX.append(0)
            nrrY.append(currentY)
            currentY -= distance

    def symmetric_neurones_position(self, nrrX, nrrY, quantity):
        distance = 10 / (quantity/2 - 1)
        currentY = 5

        for i in range(int(quantity / 2)):
            nrrX.append(-5)
            nrrY.append(currentY)
            currentY -= distance

        for i in range(int(quantity / 2)):
            nrrX.append(5)
            nrrY.append(currentY)
            currentY += distance

    def set_title(self, algorithm, neurones, shapes_len):
        if algorithm == 'K':
            title = '_Koh'
        if algorithm == 'G':
            title = '_NG'
        if algorithm == 'C':
            title = '_KMC'

        if len(neurones) == 1:
            title += '_' + str(neurones[0])
        else:
            title += '_X'

        title += '_' + str(shapes_len)

        return title
