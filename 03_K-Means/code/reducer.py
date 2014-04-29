#!/usr/bin/env python2.7
import sys
import numpy as np

def merge_and_compress(left,right):
	k = 100
	merged = left + right;

	return compress_naive(merged,k)

def compress_naive(coreset,k):
	indices = np.random.randint(low = 0, high = len(coreset), size = k)
	return np.array(coreset)[indices]

if __name__ == "__main__":
	
	current = [] # we will keep filling this up
	last = [] # this is the last coreset we filled up
	merged = None # the merged and compressed coreset (of current and last)

	k = 100
	i = 0
	for line in sys.stdin:
		data = map(float, line.split(" "))
		current.append(data)

		i+=1 # number of data-points collected

		if(i == k): # We are finished with the current coreset

			if(len(last) > 0): # We have collected two coresets; merge them
				_merged = merge_and_compress(current,last) # this is our compressed set to the right 

				if merged is None: # This is the exception, only happens the first time, move it to the left
					merged = _merged
				else: # We have a coreset to the left, so we merge them
					merged = merge_and_compress(_merged, merged)

				last = []
			else: # Or else, we only have one complete coreset; set current to the last and begin collecting another
				last = current
				current = []
			i = 0

	if(merged is None):
		merged = last

	# No more coresets, thus merged is the final coreset, so we print it
	for point in merged:
		print " ".join(map(str, point))
