#!/usr/bin/python

from Functions import Functions as Fun
from NeuralNetwork import NeuralNetwork as NN
import argparse

parser = argparse.ArgumentParser(
    prog='Exercise 1',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description='Lodz University of Technology (TUL)\
                \nInteligentna Analiza Danych (Intelligent Data Analysis)\
                \n\nExercise 1 - Neural Network\
                \nAuthors:\tJustyna Hubert\tKarol Podlewski')
parser.add_argument('fileName', metavar='DATA_FILE',
                    help='file with traning data')
parser.add_argument('inNeurones', metavar='IN_NEURONES', type=int,
                    help='specify quantity of neurones in input layer and\
                          number of columns to read from DATA_FILE')
parser.add_argument('outNeurones', metavar='OUT_NEURONES', type=int,
                    help='specify quantity of neurones in output layer and \
                         number of columns to read from DATA_FILE (if \
                         diffrent, use -t option to translate meanings)')
parser.add_argument('-a', metavar='STEP', dest='alpha', default=0.1,
                    type=float, help='specify learning STEP for network')
parser.add_argument('-b', '--bias', dest='bias', action='store_true',
                    help='turn on Bias in Network')
parser.add_argument('-e', metavar='VALUE', dest='erValue', default=4, type=int,
                    help='stop training when 10^-VALUE is bigger than error')
parser.add_argument('-i', metavar='VALUE', dest='itValue', default=0,
                    type=int, help='stop training after 10^VALUE iterations \
                                    (overwrites -e)')
parser.add_argument('--lino', dest='outputLinear', action='store_true',
                    help='set Linear activation function to output layer')
parser.add_argument('-m', metavar='STEP', dest='beta', default=0, type=float,
                    help='turn on Momentum with specified learning STEP')
parser.add_argument('-n', metavar='N', dest='hidNeurones', default=[2],
                    type=int, nargs='+',
                    help='specify quaintity N of neurones in hidden layer')
parser.add_argument('-pe', metavar='FILE', dest='savePlotE', default='',
                    help='save plot(errors) in FILE')
parser.add_argument('-pt', metavar='FILE', dest='savePlotT', default='',
                    help='save plot(training points) in FILE')
parser.add_argument('--show', dest='showPlot', action='store_true',
                    help='show plot (need -pe or -pt)')
parser.add_argument('-sh', metavar='FILE', dest='saveHidden', default='',
                    help='save outputs from hidden layer in FILE')
parser.add_argument('-sr', metavar='FILE', dest='saveResults', default='',
                    help='append to FILE data from run: alpha, beta\
                          and iterations\error')
parser.add_argument('-q', metavar=('FILE'), dest='querryFile', default='',
                    help='check error using data from FILE')
parser.add_argument('-Q', dest='extraQuerry', action='store_true',
                    help='check error DATA_FILE too (need -q to work)')
parser.add_argument('-t', metavar=('FILE'), dest='translate', default='',
                    help='read last column from DATA_FILE and translate\
                    them using FILE')
parser.add_argument('-v', '--version', action='version',
                    version='%(prog)s 1.0')
args = parser.parse_args()

arrU = []
arrV = []

if '' == args.translate:
    arrU, arrV = Fun.readFile(args.fileName, args.inNeurones, args.outNeurones)
else:
    arrU, arrV = Fun.readFile(args.fileName, args.inNeurones, 1)
    Fun.translate(args.translate, arrV)

extraLabel = ''

if '' != args.querryFile:
    qrrU, qrrV = Fun.readFile(args.querryFile, args.inNeurones,
                              args.outNeurones)
    if args.extraQuerry is True:
        args.hidNeurones += args.hidNeurones
        extraLabel = ', dane testowe'

for n in range(len(args.hidNeurones)):
    network = (NN(args.inNeurones, args.hidNeurones[n], args.outNeurones,
               args.alpha, args.beta, args.bias, args.outputLinear))

    if ('' != args.querryFile) and (args.extraQuerry is True):
        if n == (len(args.hidNeurones)/2):
            extraLabel = ', dane treningowe'
            args.querryFile = ''

    it = 0
    errX = []
    errY = []
    condition = True

    while condition is True:
        it += 1

        for k in range(len(arrU)):
            network.train(arrU[k], arrV[k])

        arrE = []
        if '' == args.querryFile:
            for k in range(len(arrU)):
                arrE.append(network.query(arrU[k]))
            err = Fun.countMSE(arrE, arrV)
        else:
            for k in range(len(qrrU)):
                arrE.append(network.query(qrrU[k]))
            err = Fun.countMSE(arrE, qrrV)

        errX.append(it)
        errY.append(err)

        condition = Fun.checkCondition(it, args.itValue, err, args.erValue)

    if '' != args.saveResults:
        Fun.saveResults(args.saveResults, args.alpha, args.beta,
                        args.itValue, it, err)

    if '' != args.savePlotE:
        Fun.addPlotE(errX, errY, args.hidNeurones[n], extraLabel)

    if '' != args.savePlotT:
        Fun.addPlotT(network.query, args.hidNeurones[n])

if '' != args.saveHidden:
    hidWeights = []
    for k in range(len(arrU)):
        hidWeights.append(network.hiddenQuery(arrU[k]))
    Fun.saveHidden(args.saveHidden, arrU, hidWeights)

if '' != args.savePlotE:
    subTitle = Fun.getTitle(args)
    Fun.drawPlotE(args.savePlotE, subTitle, len(args.hidNeurones),
                  args.showPlot)

if '' != args.savePlotT:
    subTitle = Fun.getTitle(args)
    Fun.drawPlotT(args.savePlotT, subTitle, len(args.hidNeurones),
                  arrU, arrV, qrrU, qrrV, args.showPlot)
