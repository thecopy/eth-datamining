#!/usr/bin/env python2.7

import sys
import numpy as np

if __name__ == "__main__":
	W = []
	n = 0
	for line in sys.stdin:
		W.append(map(float, line.split()))

	Wmean = np.mean(W, axis=0)
	for coeff in Wmean:
		sys.stdout.write (str(coeff) + " ")

