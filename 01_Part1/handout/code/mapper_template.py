#!/usr/bin/env python

import numpy as np
import sys

def emit(key, value):
    # write to stdout
    print(key + '\t' + str(value))

def partition(video_id, shingles, R, B, hash_fns):

    for r in range(R):  
        key = ''
        for b in range(B):
            row = r*R + b
            row_permutated = h(hash_fns[r], row);
            #print('Checking if ' + str(video_id) + ' contains shingle ' + str(row_permutated))
            if(row_permutated in shingles[r*B  : (r+1)*B - 1]):
                key += str(b)

        if(key != ''):
            emit(key, video_id)

def h(permutator, row):
    return (permutator[0] * row + permutator[1]) % permutator[2]

def get_permutation_descriptor(size):
    a = np.random.randint(size)
    b = np.random.randint(size)
    return (a,b,size)

if __name__ == "__main__":
    # Very important. Make sure that each machine is using the
    # same seed when generating random numbers for the hash functions.
    np.random.seed(seed=42)
    
    # Configuration
    num_shingles = 10000
    R = 20
    B = int(num_shingles/R)

    # Generate hash functions
    hash_sigs = []
    for i in range(R):
        hash_sigs.append( get_permutation_descriptor(10000) )


    for line in sys.stdin:
        line = line.strip()
        video_id = int(line[6:15])
        shingles = np.fromstring(line[16:], sep=" ")
        partition(video_id, shingles, R, B, hash_sigs)

    #print("-----")
    #print("Config: R=" + str(R) + " B=" + str(B))
