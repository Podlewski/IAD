import argparse


class Parser:

    def __init__(self):
        self.parser = argparse.ArgumentParser(
            prog='Exercise 3', formatter_class=argparse.RawDescriptionHelpFormatter,
            description='Lodz University of Technology (TUL)\
                        \nInteligentna Analiza Danych (Intelligent Data Analysis)\
                        \n\nExercise 3 - RBF\
                        \nAuthors:\tJustyna Hubert\tKarol Podlewski')

        # necessarily args
        self.parser.add_argument('train_file', metavar='TRAIN_FILE',
                                 help='file with traning data')
        self.parser.add_argument('test_file', metavar='TEST_FILE',
                                 help='file with test data')
        self.parser.add_argument('neurones', metavar='NEURONES', type=int, nargs='+',
                                 help='specify quantity of neurones')

        # stop condition
        self.parser.add_argument('-i', metavar='VALUE', dest='iterations', default=25, type=int,
                                 help='stop training after VALUE iterations (25 by default)')

        # save args
        self.parser.add_argument('-p', metavar='FILE', dest='plot', default='',
                                 help='save plot with rbf querry & training and test data')
        self.parser.add_argument('-ph', metavar='FILE', dest='hist_plot', default='',
                                 help='save history plot')
        self.parser.add_argument('-pr', metavar='FILE', dest='rad_plot', default='',
                                 help='save plot with rbf querry, rad querry & training and test data')
        self.parser.add_argument('-sr', metavar='FILE', dest='save_res', default='',
                                 help='append to FILE: neurones, error for training and test data')

        # another
        self.parser.add_argument('-a', metavar='ALPHA', dest='alpha', default=0.1,
                                 type=float, help='specify learning step ALPHA for RBF')
        self.parser.add_argument('-s', metavar='SIGMA', dest='sigma', default=1, type=float,
                                 help='specify SIGMA multiplier for RFB radial layer')

    def parse(self):
        self.args = self.parser.parse_args()

    # getters
    def get_args(self):
        self.parse()
        return self.args
