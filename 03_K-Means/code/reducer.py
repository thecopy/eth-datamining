#!/usr/bin/env python2.7

import numpy as np
import sys
from ast import literal_eval

values = None
N = 0

#def listify(row):
#    return ' '.join(map(str, row.tolist()))

if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        key, value = line.split('\t')
        value = np.asmatrix(literal_eval(value))
        
        if values is None:
            values = value
        else:
            values += value
        
        N += 1
    
    values = values / float(N)
    
    i = 0
    values_list = values.tolist()
    while i < len(values_list):
        j = 0
        while j < len(values_list[i]):
            if j != len(values_list[i]) -1:
                sys.stdout.write(str(values_list[i][j]) + ' ')
            else:
                sys.stdout.write(str(values_list[i][j]) + '\n')
            
            j += 1
        i += 1 
#    print '\n'.join(np.apply_along_axis( listify, axis=1, arr=values / float(N) ) )
