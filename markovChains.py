'''
Created on Nov 10, 2014

@author: eotles
'''

import numpy as np

FIG_1 = [[0, 1, 0],
         [0, 0, 1],
         [1, 0, 0]]
#Watch by p^n trick!

FIG_2 = [[0, 1, 0],
         [0, 0, 1],
         [0, 0, 1]]


HEALTHY_SICK = [[0.9, 0.1],
                [0.5, 0.5]]

HEALTHY_SICK_DEAD = [[0.899, 0.1  , 0.001],
                     [0.8  , 0.195, 0.005],
                     [0    , 0    , 1    ]]


def main():
    tpm = np.matrix(FIG_2)
    
    examineConvergence(tpm, 10000)


def exactLPD(tpm):
    #print(tpm**0)
    print((tpm - (tpm**0))**-1)

#could store values for faster computation.
def examineConvergence(tpm, n):
    for i in xrange(n):
        print("%s Step Transition Matrix" %(i))
        print(tpm**i)
    

if __name__ == '__main__':
    main()