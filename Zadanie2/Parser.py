import argparse
import sys


class Parser:

    def __init__(self):
        self.parser = argparse.ArgumentParser(
            prog='Exercise 2', formatter_class=argparse.RawDescriptionHelpFormatter,
            description='Lodz University of Technology (TUL)\
                        \nInteligentna Analiza Danych (Intelligent Data Analysis)\
                        \n\nExercise 2 - Self Organizing Map\
                        \nAuthors:\tJustyna Hubert\tKarol Podlewski')

        # algorithm
        self.parser.add_argument('-ac', action='store_const', dest='algorithm',
                                 help='K-Means Clustering Algorithm', const='C')
        self.parser.add_argument('-ag', action='store_const', dest='algorithm',
                                 help='Neural Gas Algorithm', const='G')
        self.parser.add_argument('-ak', action='store_const', dest='algorithm',
                                 help='Kohonen Algorithm', const='K')

        # neurones quantity, learning parameters
        self.parser.add_argument('-n', metavar='Q', dest='neurones', default=[2], type=int,
                                 nargs='+', help='Specify quaintity Q of neurones')
        self.parser.add_argument('-lp', metavar=('PAR1', 'PAR2'), nargs=2, action='store',
                                 dest='learning_parameters', type=float, default=[0.01, 0.01],
                                 help='Set learning parameters PAR1 and PAR2 (0.01 by default)')
        self.parser.add_argument('-olp', action='store_true', dest='own_learning_parameters', default=False,
                                 help='Algorithm counts learning parameteres based on iteration')

        # geometrical shapes
        self.parser.add_argument('-sc', '--circle', metavar=('X', 'Y', 'R', 'Q'), nargs=4,
                                 action='store', dest='circle', type=int, default=0,
                                 help='Create circle on X,Y with R radius and Q training data')
        self.parser.add_argument('-sl', '--line', metavar=('X0', 'Y0', 'X1', 'Y1', 'Q'), nargs=5,
                                 action='store', dest='line', type=int, default=0,
                                 help='Create line from X0,Y0 to X1,Y1 with Q training data')
        self.parser.add_argument('-sr', '--rectangle', metavar=('X0', 'Y0', 'X2', 'Y2', 'Q'), nargs=5,
                                 action='store', dest='rectangle', type=int, default=0,
                                 help='Create rectange with oposite vertex (X0,Y0 & X2,Y2) and\
                                       with Q training data')
        self.parser.add_argument('-sw', '--wheel', metavar=('X', 'Y', 'R', 'Q'), nargs=4,
                                 action='store', dest='wheel', type=int, default=0,
                                 help='Create circle on X,Y with R radius and Q training data')

        # saving results
        self.parser.add_argument('-ce', metavar='FILE', dest='error_chart_file_name', default='',
                                 help='Save chart with error quantization change in FILE')
        self.parser.add_argument('-ch', metavar='FILE', dest='history_chart_file_name', default='',
                                 help='Save chart with history of neurone position FILE')
        self.parser.add_argument('-cv', metavar='FILE', dest='vornoi_chart_file_name', default='',
                                 help='Save chart with Vornoi diagram in FILE')
        self.parser.add_argument('-d', metavar='FILE', dest='data_file_name', default='',
                                 help='Save both learning parameters, quantization error, \
                                       min & avg inactive neurones for it FILE')

        # other
        self.parser.add_argument('-r', '--area', metavar=('PAR1', 'PAR2'), nargs=2, action='store',
                                 dest='area', type=float, default=[-10, 10],
                                 help='Set area range for starting neurones position')
        self.parser.add_argument('-rl', action='store_true', dest='line_area',
                                 default=False, help='Line area for starting neurone positions')
        self.parser.add_argument('-rs', action='store_true', dest='symetric_area',
                                 default=False, help='Symetrix area for starting neurone positions')
        self.parser.add_argument('-nc', action='store_true', dest='connect_neurones',
                                 default=False, help='Show connected neurones on chart')
        self.parser.add_argument('--debug', action='store_true', dest='debug',
                                 default=False, help='Show current iteration')

    def parse(self):
        self.args = self.parser.parse_args()

    # getters
    def get_algorithm(self):
        if self.args.algorithm is None:
            self.parser.print_usage()
            sys.exit("Exercise 2: error: You must specify algorithm")
        else:
            return self.args.algorithm

    def get_lerning_parameters(self):
        return self.args.learning_parameters

    def get_own_learning_parameters(self):
        return self.args.own_learning_parameters

    def get_shapes(self):
        shapes = []
        shapes_settings = []
        if self.args.circle != 0:
            shapes.append('c')
            shapes_settings.append(self.args.circle)
        if self.args.line != 0:
            shapes.append('l')
            shapes_settings.append(self.args.line)
        if self.args.rectangle != 0:
            shapes.append('r')
            shapes_settings.append(self.args.rectangle)
        if self.args.wheel != 0:
            shapes.append('w')
            shapes_settings.append(self.args.wheel)

        if len(shapes) == 0:
            self.parser.print_usage()
            sys.exit("Exercise 2: error: You must specify at least 1 shape")
        else:
            return shapes, shapes_settings

    def get_area_settings(self):
        return self.args.area, self.args.line_area, self.args.symetric_area

    def get_charts_file_name(self):
        err = self.args.error_chart_file_name
        his = self.args.history_chart_file_name
        vor = self.args.vornoi_chart_file_name
        return err, his, vor

    def get_charts_settings(self):
        return self.args.connect_neurones

    def get_neurones(self):
        return self.args.neurones

    def get_data_file_name(self):
        return self.args.data_file_name

    def get_debug(self):
        return self.args.debug
