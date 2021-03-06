#!/bin/bash
#
# $1 and $2 are special variables in bash that contain the 1st and 2nd
# command line arguments to the script, which are the names of the
# Dakota parameters and results files, respectively.
#
#echo 'init' >> test
#
params=$1
results=$2
#
###############################################################################
##
## Pre-processing Phase -- Generate/configure an input file for your simulation
##  by substiting in parameter values from the Dakota paramters file.
##
###############################################################################
#
#echo 'ciao' >> test
#echo "$params" >> test
#echo "$results" >> test
#
dprepro $params input.template input.i
#
#python function.py -i input.i -o out
python function.py -i input.i > out.out
#sed -i 's/\r$//' out^M
#
# post processing:

A=$(awk 'NR == 4' out.out)
S=$(awk 'NR == 6' out.out)
V=$(awk 'NR == 8' out.out)

#echo $y
#
echo "$A A" > $results
echo "$S S" >> $results
echo "$V V" >> $results

#
