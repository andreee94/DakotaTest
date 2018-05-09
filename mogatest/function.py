import numpy as np
import sys
import os.path
import argparse
#from __future__ import print_function

def ackley(x, a=20, b=0.2, c=2*np.pi):
	"""
	x: vector of input values
	"""
	d = len(x) # dimension of input vector x
	sum_sq_term = -a * np.exp(-b * np.sqrt(sum(x*x) / d))
	cos_term = -np.exp(sum(np.cos(c*x) / d))
	return a + np.exp(1) + sum_sq_term + cos_term

def myprint(f, line):
	if f == None:
		print(line)
	else:
		#print(line, file=f) # python3
		print >> f, line # python2

def removeComment(line):
	try:
		commentIndex = line.index('#')
		line = line[:commentIndex]
		return line
	except ValueError:
		return line

# parse input arguments
parser = argparse.ArgumentParser()
parser.add_argument('-i', action='store', dest='in_file', help='Input filename')
parser.add_argument('-o', action='store', dest='out_file', help='Output filename', default=None)

params = parser.parse_args()

with open(params.in_file,"r") as f:
	rawInput = f.readlines()

x = []
for i, line in enumerate(rawInput):
	line = line.strip()
	line = removeComment(line)
	try:
		x.append(float(line))
	except ValueError:
		pass

#x = sys.argv[1:]  # remove python filename
#x = list(map(float, list(x)))

y = ackley(np.asarray(x))

#import pdb; pdb.set_trace()

#print(params.out_file)

if params.out_file != None:
	out_file = open(params.out_file, "w+")
else: out_file = None

myprint(out_file, 'Ackley input vector is:')
myprint(out_file, str(x))
myprint(out_file, 'Ackley value is:')
myprint(out_file, str(y))
myprint(out_file, 'Ackley^-1 value is:')
myprint(out_file, str(1/y))
#myprint(out_file, str(1/y-abs(y)))
