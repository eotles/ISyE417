'''
Created on Apr 13, 2015

@author: eotles
'''
from markovChains import examineConvergence
import numpy as np

def p1_2():
    v_dict = {0:{0:0.5, 1:0.5}, 1:{0:0.2, 1:0.8}}
    p_dict = {0:{0:0.25, 1:0.75}, 1:{0:0.4, 1:0.6}}
    
    for v_from,  v_to_dict in v_dict.iteritems():
        for p_from,  p_to_dict in p_dict.iteritems():
            for v_to, p_v in v_to_dict.iteritems():
                for p_to, p_p in p_to_dict.iteritems():
                    print("P(V=%d n P=%d | V=%d n P=%d) = %0.3f" %(v_to, p_to, v_from, p_from, p_v*p_p))


def p2_3():
    tpm = [[.99, .01, 0],
           [  0,   0, 1],
           [  1,   0, 0]]
    
        
    tpm = [[.9604, .0196,   0, .0196, .0004,   0,   0,   0, 0],
           [    0,   0, .98,   0,     0, .02,   0,   0, 0],
           [  .98,   0,   0, .02,     0,   0,   0,   0, 0],
           [    0,   0,   0,   0,     0,   0, .98, .02, 0],
           [    0,   0,   0,   0,     0,   0,   0,   0, 1],
           [    0,   0,   0,   0,     0,   0,   1,   0, 0],
           [  .98, .02,   0,   0,     0,   0,   0,   0, 0],
           [    0,   0,   1,   0,     0,   0,   0,   0, 0],
           [    1,   0,   0,   0,     0,   0,   0,   0, 0]]
    
    tpm = np.matrix(tpm)
    #print((tpm - (tpm**0))**-1)
    print(tpm**500)

def main():
    p1_2()


if __name__ == '__main__':
    main()