#!/usr/bin/env python
import sys
import numpy as np

if __name__ == "__main__":
	skipFirst = False
	if(len(sys.argv) > 1 and sys.argv[1] == 's'):
		skipFirst = True

	with open('w.data') as f:
		w = np.array( map(float, f.readline().split()) )


	for line in sys.stdin:
		x = np.array( map(float, line.split()) )
		if(skipFirst):
			x = x[1:]

		y = np.sign(np.dot(w.T, x))
		print str(int(y))

