###############################################################
#                                                             #
# Calculates the non-cumulative data from the cumulative data #
# i.e. numerically calculates the derivative                  #
#                                                             #
###############################################################

from numpy import *

data = genfromtxt('/data/test/result/name_of_input_file')

# reduces data size by reading every 10th data point
dtrim = data[::10]

d = []
for i in range(len(dtrim)-1):
    d.append(dtrim[i+1][1:] - dtrim[i][1:])

print d

savetxt('/data/mekhala/sync_again/buffer_uncumul.dat', d, fmt='%.7f')
