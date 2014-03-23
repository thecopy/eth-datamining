#!/usr/bin/env python

import numpy as np
import sys

def emit(key, value):
    # write to stdout
    print(key + '\t' + value)

def getMinHashSignature(shingles, hash_fns):
    #print("number of hash fns: " + str(len(hash_fns)))
    M = len(hash_fns) * [int(max(shingles))+100]

    for row in range(int(max(shingles))+1):
        if row in shingles:

            #print("Video has shingle " + str(row))
            for i,hash_fn in enumerate(hash_fns):
                #print('hashfn: ' + str(hash_fn))
                M[i] = min(M[i], h(hash_fn,row))

    #print(M)
    return M

def partition(value, shingles, R, B, hash_fns):
    M = getMinHashSignature(shingles, hash_fns);

    for b in range(B):  
        key = ''
        for r in range(R):
            row = b*R+r;

            key += str(M[row])

        emit(key, value)

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
    num_features = 10000;
    t = 0.85
    n = 100; # number of hashes

    # B and R will produce threshhold of 0.8. Giving more FP.
    # This produces "only more work"
    B = 6;
    R = 15;

    # Generate hash functions
    hash_sigs = []
    for i in range(n):
        hash_sigs.append( get_permutation_descriptor(num_features) )

    for line in sys.stdin:
        line = line.strip()
        video_id = int(line[6:15])
        shingles = line[16:].split()
        value = str(video_id) + " " + line[16:]
        shingles = np.fromstring(line[16:], sep=" ")
        partition(value, shingles, R, B, hash_sigs)

    #print("-----")
    #print("Config: R=" + str(R) + " B=" + str(B))
