import numpy as np
import numpy.random as rand
import scipy.special as ss


class NeuralNetwork:

    def __init__(self, inNodes, hidNodes, outNodes, alpha, beta, bias,
                 outputActivationFun):

        self.iNodes = inNodes
        self.hNodes = hidNodes
        self.oNodes = outNodes

        # learning rate
        self.alpha = alpha
        self.beta = beta

        self.hWeights = rand.normal(0.0, 0.5, (self.hNodes, self.iNodes))
        self.hWeightsDelta = np.zeros((self.hNodes, self.iNodes))

        self.oWeights = rand.normal(0.0, 0.5, (self.oNodes, self.hNodes))
        self.oWeightsDelta = np.zeros((self.oNodes, self.hNodes))

        # turning on/off bias (default bias turned off)
        if bias is False:
            self.bias = 0
            self.hBias = np.zeros((self.hNodes, 1))
            self.hBiasDelta = np.zeros((self.hNodes, 1))

            self.oBias = np.zeros((self.oNodes, 1))
            self.oBiasDelta = np.zeros((self.oNodes, 1))
        else:
            self.bias = 1
            self.hBias = rand.normal(0.0, 0.5, (self.hNodes, 1))
            self.hBiasDelta = np.zeros((self.hNodes, 1))

            self.oBias = rand.normal(0.0, 0.5, (self.oNodes, 1))
            self.oBiasDelta = np.zeros((self.oNodes, 1))

        self.hActFun = lambda z: ss.expit(z)

        # activation function for output layer
        if outputActivationFun is False:
            self.oActFun = lambda z: ss.expit(z)
            self.oErrFun = lambda x, y: ((x - y) * y * (1 - y))
        else:
            self.oActFun = lambda z: z
            self.oErrFun = lambda x, y: ((x - y))

    def train(self, arrU, V):
        arrU = np.array(arrU, ndmin=2)

        # arrX - hidden layer output
        hidZ = np.inner(arrU, self.hWeights) + self.hBias.T
        arrX = self.hActFun(hidZ)

        # Y - output layer output
        outZ = np.inner(arrX, self.oWeights) + self.oBias.T
        Y = self.oActFun(outZ)

        # oErr - backward propagation of errors for output layer
        oErr = self.oErrFun(V, Y)

        # hErr - backward propagation of errors for hidden layer
        sigma = np.inner(oErr, self.oWeights.T)
        hErr = ((sigma * arrX * (1 - arrX)))

        self.oWeights += self.alpha * oErr.T * arrX + self.oWeightsDelta
        self.hWeights += self.alpha * hErr.T * arrU + self.hWeightsDelta

        if self.bias != 0:
            self.oBias += self.alpha * oErr.T + self.oBiasDelta
            self.hBias += self.alpha * hErr.T + self.hBiasDelta

        if self.beta != 0:
            self.oWeightsDelta = (self.beta * (self.alpha * oErr.T * arrX +
                                  self.oWeightsDelta))
            self.hWeightsDelta = (self.beta * (self.alpha * hErr.T * arrU +
                                  self.hWeightsDelta))
            if self.bias != 0:
                self.oBiasDelta += (self.beta * (self.alpha * oErr.T +
                                    self.oBiasDelta))
                self.hBiasDelta += (self.beta * (self.alpha * hErr.T +
                                    self.hBiasDelta))

    def query(self, arrU):
        arrU = np.array(arrU, ndmin=2)
        hidZ = np.inner(arrU, self.hWeights) + self.hBias.T
        arrX = self.hActFun(hidZ)
        outZ = np.inner(arrX, self.oWeights) + self.oBias.T

        return (self.oActFun(outZ)[0])

    def hiddenQuery(self, arrU):
        arrU = np.array(arrU, ndmin=2)
        hidZ = np.inner(arrU, self.hWeights) + self.hBias.T
        return np.squeeze(self.hActFun(hidZ))
