import numpy as np


class RBF:

    def gauss(self, neurone, x):
        # euclidean distance
        distance = np.fabs(x - self.centers[neurone])
        exp = np.exp((-1 * distance * distance) / (2 * self.sigma * self.sigma))
        return float(1 * exp / (np.sqrt(2 * np.pi) * self.sigma))

    def f(self, x):
        sum = self.bias
        for n in range(self.neurones):
            sum += (self.weights[n] * self.gauss(n, x))
        return sum

    def __init__(self, neurones_quantity, array_x, sigma_multiplier, alpha):
        self.neurones = neurones_quantity
        self.alpha = alpha
        # create arrays for centers -> numpy.empty returns a new array of given shape
        # and type, without initializing entries (marginally faster than numpy.zeros)
        # NEXT set centers array from given (traning) values
        self.centers = np.empty(self.neurones)
        for n in range(self.neurones):
            random_input = np.random.randint(len(array_x))
            self.centers[n] = array_x[random_input]
        # create array for sigma from values <sigma_values - 0.05, sigma_values + 0.05)
        self.sigma = 1.1 * sigma_multiplier
        # create arrays for bias and weights from values <-0.5, 0.5)
        self.bias = np.random.uniform(-0.5, 0.5)
        self.weights = np.random.uniform(-0.5, 0.5, self.neurones)

    def train(self, array_x, array_y):
        weights_delta = np.zeros(self.neurones)
        bias_delta = 0

        for i in range(len(array_x)):
            gauss = np.empty(self.neurones)
            for g in range(self.neurones):
                gauss[g] = self.gauss(g, array_x[i])

            sum = self.bias
            for w in range(self.neurones):
                sum += gauss[w] * self.weights[w]

            error = sum - array_y[i]

            bias_delta += error
            for w in range(self.neurones):
                weights_delta[w] += gauss[w] * error

        self.bias -= self.alpha * bias_delta / len(array_x)

        for w in range(self.neurones):
            self.weights[w] -= self.alpha * weights_delta[w] / len(array_x)

    def error(self, array_x, array_y):
        sum = 0
        for i in range(len(array_x)):
            sum += pow(self.f(array_x[i]) - array_y[i], 2)
        return (1 / (2 * len(array_x))) * sum
