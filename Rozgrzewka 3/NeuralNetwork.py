import numpy as np
import numpy.random as rand


class NeuralNetwork:

    def __init__(self, inNodes, hidNodes, outNodes, alpha, settings):
        self.iNodes = inNodes
        self.hNodes = hidNodes
        self.oNodes = outNodes

        # learning rate
        self.alpha = alpha

        self.hWeights = rand.normal(0.0, 0.5, (self.hNodes, self.iNodes))
        self.oWeights = rand.normal(0.0, 0.5, (self.oNodes, self.hNodes))

        # settings[0] - turning on/off bias
        if 0 == settings[0]:
            self.hBias = rand.normal(0.0, 0.5, (self.hNodes, 1))
            self.oBias = rand.normal(0.0, 0.5, (self.oNodes, 1))
        else:
            self.hBias = None
            self.oBias = None

        # settings[0] - turning on/off momentum
        if 0 == settings[1]:
            self.momentum = 0

        # settings[2] - activation function for hidden layer
        if 0 == settings[2]:
            self.hFun = 'sigmoid'
        else:
            self.hFun = 'linear'

        # settings[3] - activation function for output layer
        if 0 == settings[3]:
            self.oFun = 'sigmoid'
        else:
            self.oFun = 'linear'

    def hFunction(self, x):
        if self.hFun == 'sigmoid':
            z = np.inner(x, self.hWeights) + self.hBias.T
            return 1/(1+np.exp(-1 * z))
        if self.hFun == 'linear':
            return x

    def oFunction(self, x):
        if self.oFun == 'sigmoid':
            z = np.inner(x, self.oWeights) + self.oBias.T
            return 1/(1+np.exp(-1 * z))
        if self.oFun == 'linear':
            return x

    def train(self, arrU, V):
        # arrX - hidden layer output
        arrX = self.hFunction(arrU)
        # Y - output layer output
        Y = self.oFunction(arrX)

        # oErr, hErr - backward propagation of errors for specific layers
        oErr = np.squeeze((V - Y) * Y * (1 - Y))
        hErr = (np.inner(self.oWeights, oErr) * arrX * (1 - arrX)).T

        self.oWeights += self.alpha * oErr * arrX
        self.oBias += self.alpha * oErr

        self.hWeights += self.alpha * hErr * arrU
        self.hBias += self.alpha * hErr

    def query(self, arrU):
        arrX = self.hFunction(arrU)
        return np.squeeze(self.oFunction(arrX))
