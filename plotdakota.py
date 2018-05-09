import matplotlib.pyplot as plt
import numpy
import sys
import os.path
from pprint import pprint
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("filename", help="Filename")
parser.add_argument('-x', type=int, action='store', dest='x_index', help='Comumn index of x starting from 1')
parser.add_argument('-y', type=int, action='store', dest='y_index', help='Comumn index of y starting from 1')
parser.add_argument("-xs", "--xsort", action="store_true", help="Sort x vector")
parser.add_argument("--max", action="store_true", help="Take max of y up to now")
parser.add_argument("--min", action="store_true", help="Take min of y up to now")
parser.add_argument("--abs", action="store_true", help="Take abs of y")
parser.add_argument('--update', type=float, action='store', dest='update_time', help='Comumn index of y starting from 1')
parser.add_argument("--xlog", action="store_true", help="Axis x logarithmic")
parser.add_argument("--ylog", action="store_true", help="Axis y logarithmic")
parser.add_argument("--loglog", action="store_true", help="Axis x and y logarithmic")
parser.add_argument("--point", action="store_true", help="Point instead of lines", default=False)
params = parser.parse_args()
print(params)

if params.x_index == None or params.y_index == None:
    print('-x, -y parameters are mandatory.')
else:
    x_index = params.x_index - 1
    y_index = params.y_index - 1

    
    plt.show()
    first = True

    while first or params.update_time != None: # always true if update is set
        first = False
        try:
            data = numpy.loadtxt(params.filename, skiprows=1, usecols=(x_index, y_index))
            #print(data)
            x = data[:, 0]
            y = data[:, 1]
            ##################################################
            if params.xsort:
                x.sort()
            ##################################################
            if params.abs:
                y = abs(y)
            ##################################################
            if params.max or params.min:
                y_new = [0] * len(y)
                y_new[0] = y[0] #first item is y[0] in any case
                print(len(y_new))
                for i in range(1,len(y)):
                    if params.max:
                        y_new[i] = max(y[0:i])
                    elif params.min:
                        y_new[i] = min(y[0:i])
                y = y_new
            ##################################################
            if params.xlog or params.loglog:
                plt.xscale('log')
            if params.ylog or params.loglog:
                plt.yscale('log')
            ##################################################
            if params.point:
                plt.plot(x, y, '*')
            else: plt.plot(x, y)
            plt.grid()
        except Exception as e:
            print('Error extracting columns')
            print(e)
        plt.pause(params.update_time)
        plt.clf()