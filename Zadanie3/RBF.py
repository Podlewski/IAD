import numpy as np
import random


class RBF:

    def gauss(self, neurone, x):
        # euclidean distance
        distance = np.fabs(x - self.centers[neurone])
        exp = np.exp((-1 * distance * distance) / (2 * self.sigmas[neurone] * self.sigmas[neurone]))
        return float(1 * exp / (np.sqrt(2 * np.pi) * self.sigmas[neurone]))

    def f(self, x):
        sum = self.bias
        for n in range(self.n_quantity):
            sum += (self.weights[n] * self.gauss(n, x))
        return sum

    def count_centers(self, array_x):
        rand_tab = random.sample(range(1, len(array_x)), self.n_quantity)

        for c in range(self.n_quantity):
            self.centers[c] = array_x[rand_tab[c]]

    def count_sigmas(self, sigma_multiplier):
        for s in range(self.n_quantity):
            l_index = -1
            r_index = -1
            for c in range(self.n_quantity):
                if (s != c):
                    if (self.centers[s] > self.centers[c]):
                        l_index = c
                    else:
                        r_index = c

            distance = 0
            if l_index != -1:
                distance += self.centers[s] - self.centers[l_index]
            if r_index != -1:
                distance += self.centers[r_index] - self.centers[s]
            if l_index != -1 and r_index != -1:
                distance /= 2

            if distance != 0:
                self.sigmas[s] = (2 * sigma_multiplier) / (distance)
            else:
                self.sigmas[s] = 1.1

    def __init__(self, neurones_quantity, array_x, sigma_multiplier, alpha):
        # centers, sgimas and weights quantity
        self.n_quantity = neurones_quantity
        # learning coef
        self.alpha = alpha
        # set values for centers
        self.centers = np.empty(self.n_quantity)
        self.count_centers(array_x)
        # set values for sigmas
        self.sigmas = np.empty(self.n_quantity)
        self.count_sigmas(sigma_multiplier)
        # create arrays for bias and weights from values <-0.5, 0.5)
        self.bias = np.random.uniform(-0.5, 0.5)
        self.weights = np.random.uniform(-0.5, 0.5, self.n_quantity)

    def train(self, array_x, array_y):
        for i in range(len(array_x)):
            gauss = np.empty(self.n_quantity)
            for g in range(self.n_quantity):
                gauss[g] = self.gauss(g, array_x[i])

            sum = self.bias
            for w in range(self.n_quantity):
                sum += gauss[w] * self.weights[w]

            error = sum - array_y[i]

            self.bias -= self.alpha * error
            for w in range(self.n_quantity):
                self.weights[w] -= self.alpha * error * gauss[w]

    def error(self, array_x, array_y):
        sum = 0
        for i in range(len(array_x)):
            sum += (self.f(array_x[i]) - array_y[i]) * (self.f(array_x[i]) - array_y[i])
        return (1 / (2 * len(array_x))) * sum
