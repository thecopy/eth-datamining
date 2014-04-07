#!/usr/bin/env python
import numpy as np
import sys

# This function has to either stay in this form or implement the
# feature mapping. For details refer to the handout pdf.
def transform(x_original):
	return x_original

def SGD(data):
	dim = 400 # 400 dimensions
	n = 0.5
	C = 2
	w = np.zeros(shape=(1,dim))

	print("Running SGD...")

	for i,p in enumerate(data):
		if(label*w*p[1].T >= 1):
			w = w - n*( 2*w/(i+1) )
		else:
			w = w - n*( 2*w/(i+1) - C*label*p[1])

	for i in range(dim):
		sys.stdout.write(str(w[0,i]) + "  ")

if __name__ == "__main__":
	print(sys.version)
	print("Reading input...")
	data = [];
	for line in sys.stdin:
		line = line.strip()
		label = int(line[0:2])
		features = transform(np.matrix( map(float, line[3:].split()) ))
		data.append( (id, features) )

	SGD(data)