#!/usr/bin/python

from Functions import Functions as Fun
from RBF import RBF
from Parser import Parser

Par = Parser()

args = Par.get_args()

train_x, train_y = Fun.readFile(args.train_file)
test_x, test_y = Fun.readFile(args.test_file)

for n in range(len(args.neurones)):
    rbf = RBF(args.neurones[n], train_x, args.sigma, args.alpha)

    it = 0
    condition = True

    while it < args.iterations:
        it += 1
        rbf.train(train_x, train_y)

        if ('' != args.hist_plot) and ("" == args.plot):
            if ((it % (args.iterations/5) == 0) or it == 1):
                Fun.add_plot(rbf.f, it, False)

    if "" != args.plot:
        Fun.add_plot(rbf.f, args.neurones[n])

    if "" != args.save_res:
        data_to_save = str(args.neurones[n]) + ' '
        data_to_save += str(rbf.error(train_x, train_y)) + ' '
        data_to_save += str(rbf.error(test_x, test_y)) + '\n'
        Fun.save_in_file(args.save_res, data_to_save)

    if ("" != args.rad_plot) and ("" == args.hist_plot) and ("" == args.plot):
        Fun.add_plot(rbf.f, args.neurones[n], True, "Funkcja sieci")
        for m in range(args.neurones[n]):
            Fun.add_rad_plot(m, rbf.gauss, rbf.weights[m], args.neurones[n])

if "" != args.plot:
    Fun.draw_plot(args.plot, train_x, train_y, test_x, test_y)

if ("" != args.hist_plot) and ("" == args.plot):
    Fun.draw_hist_plot(args.hist_plot)

if ("" != args.rad_plot) and ("" == args.hist_plot) and ("" == args.plot):
    Fun.draw_plot(args.rad_plot, train_x, train_y, test_x, test_y)
