#!/usr/bin/env python

import sys
import numpy as np

if __name__ == "__main__":
	filename = "result.txt"

	with open(filename) as f:
		w = np.array( map(float, f.readline().split()) )	

	input = open('training', 'r')	
	count = 0
	for line in input:
		x = np.array( map(float, line.split()) )
		x = x[1:]
		y = int(np.sign(np.dot(w.T, x)))
		if(y == 0):
			y = -1		

		print str(y)
		count += 1
		if count == 150:
			break
