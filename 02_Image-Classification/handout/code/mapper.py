#!/usr/bin/env python
import numpy as np
import sys
import signal

curr_e = 1000
w = None
def signal_handler(signal, frame):
	global curr_e
	global w
	print curr_e
	print w
	exit(0)

# This function has to either stay in this form or implement the
# feature mapping. For details refer to the handout pdf.
def transform(x_original):
	return x_original

def SGD(data):
	global w
	global curr_e

	dim = 400 # 400 dimensions

	if(len(sys.argv) > 1):
		dim = int(sys.argv[1])

	a = 1 # learning rate = 1/iterations
	n = len(data) # number of data points
	C = 0.5 # regularization constant
	w = np.zeros(dim) # coefficents
	e = 0.01 # threshold
	i = 1 # iterations

	while(abs(curr_e) > e):
		for p in data:
			if(abs(curr_e) <= e):
				break;

			old_w = w
			y = p[0] #label
			x = p[1] #features

			if(y * np.dot(w.T,x) >= 1):
				w = w - (a/i)*  2*w/n
			else:
				w = w - (a/i)*( 2*w/n - C*x*y)

			curr_e = np.linalg.norm(old_w-w)
			i += 1

	for i in range(dim):
		sys.stdout.write(str(w[i]) + "  ")
	sys.stdout.write("\n")

if __name__ == "__main__":
	signal.signal(signal.SIGINT, signal_handler)
	#print(sys.version)
	#print("Reading input...")
	data = [];
	for line in sys.stdin:
		line = line.strip()
		label = int(line[0:2])
		features = np.array( map(float, line[3:].split()) )
		data.append( (label, features) )

	SGD(data)