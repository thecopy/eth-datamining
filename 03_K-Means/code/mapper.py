#!/usr/bin/env python2.7

import sys
import numpy as np
from sklearn.cluster import MiniBatchKMeans

def emit(key, value):
    print('%s\t%s' % (key, value))

if __name__ == "__main__":
    X = np.zeros(shape=(0, 750))
    for line in sys.stdin:
        sample = np.fromstring(line, sep=" ")
        
        X = np.vstack( (X, sample) )
    
    mbk = MiniBatchKMeans(n_clusters=200, init='k-means++', n_init=5, batch_size=150)
    mbk.fit(X)
    
    emit(1, mbk.cluster_centers_.tolist())