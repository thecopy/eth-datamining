#!/usr/bin/env python
import sys
import numpy as np

if __name__ == "__main__":
	skipFirst = False
	filename = "w.data"
	if(len(sys.argv) == 2 and sys.argv[1] == 's'):
		skipFirst = True

	if(len(sys.argv) == 3 and sys.argv[2] == 's'):
		skipFirst = True
		filename = sys.argv[1]

	with open(filename) as f:
		w = np.array( map(float, f.readline().split()) )

	for line in sys.stdin:
		x = np.array( map(float, line.split()) )
		if(skipFirst):
			x = x[1:]

		y = int(np.sign(np.dot(w.T, x)))
		if(y == 0):
			y = -1

		print str(y)

