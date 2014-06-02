#!/usr/bin/env python2.7
import numpy as np
import sklearn as sl
import sys

# This function has to either stay in this form or implement the
# feature mapping. For details refer to the handout pdf.
def transform(x):
	x_transformed =  normalize(x)
	return x_transformed

def normalize(x):
	x_mean = np.mean(x, axis=0)
	x_std = np.std(x, axis=0)
	return (x-x_mean)/x_std

def SGD(labels, data):

	dim = len(data[0]) # dimensions

	a = 1 # learning rate = 1/iterations
	n = len(data) # number of data points
	C = 1 # regularization constant
	w = np.zeros(dim) # coefficents
	e = 0.01 # threshold
	iters = 1 # iterations

	useL1 = True

	for i,x in enumerate(data):
		y = labels[i] # label
		if(y * np.dot(w.T,x) >= 1): # if data-point is correctly classified
			w = w - (a/iters)*  regularizationTerm(w,useL1)/n
		else:						# if data-point is incorrectly classified
			w = w - (a/iters)*( regularizationTerm(w,useL1)/n - C*x*y)

	for i in range(dim):
		sys.stdout.write(str(w[i]) + " ")
	sys.stdout.write("\n")

def regularizationTerm(w, useL1):
	if(useL1):
		return np.sign(w)
	else:
		return 2*w

if __name__ == "__main__":
	#print(sys.version)
	#print("Reading input...")
	data = [];
	labels = [];
	for line in sys.stdin:
		line = line.strip()
		label = int(line[0:2])
		features = np.array( map(float, line[3:].split()) )

		labels.append( label )
		data.append( features )


	SGD( labels, transform(data) )