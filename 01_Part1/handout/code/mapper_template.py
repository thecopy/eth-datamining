#!/usr/bin/env python

import numpy as np
import sys

# Configuration
num_permutations = 1

def partition(video_id, shingles):
	# Initialize column vector representing this video's
	#  column in the signature matrix.

	M = np.empty((num_permutations,1,))

	for p in range(num_permutations):
		pass

def get_permutation:
	a = np.random.randint(num_permutations)
	b = np.random.randint(num_permutations)

	return {a,b}

if __name__ == "__main__":
    # Very important. Make sure that each machine is using the
    # same seed when generating random numbers for the hash functions.
    np.random.seed(seed=42)

    for line in sys.stdin:
        line = line.strip()
        video_id = int(line[6:15])
        shingles = np.fromstring(line[16:], sep=" ")
        partition(video_id, shingles)
