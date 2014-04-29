#!/usr/bin/env python2.7
import sys
import numpy as np

def dist(x,y):
	return np.linalg.norm(x-y)

def calculateCoreset_naive(data,k):
    indices = np.random.randint(low = 0, high = len(data), size = k)
    return data[indices]

def calculateCoreset_adative(data,k):
	dim = data.shape[1]
	e = 0.5
	delta = 0.9999

	print "Calculating Coreset"
	print "             Method: Adaptive Sampling"
	print "   Size of data-set: " + str(data.shape)
	print "                  k: " + str(k)
	print "                  d: " + str(dim)
	print "                  e: " + str(e)
	print "              delta: " + str(delta)
	print "             len(D): " + str(len(data))
	print "           decision: " + str(int(10 * dim * k * np.log(1 / delta)))
	print "  ------------------------------"

	B = np.empty(shape=[0, 750], dtype=float)
	D = data # D'

	while( len(D) > 10 * dim * k * np.log(1 / delta) ):
		# Get S
		b = int( 10 * dim * k * np.log(1 / delta) )
		s_indices = np.random.randint(low = 0, high = len(D), size = b)
		S = D[s_indices];

		# Remove |D/2| points from D which are the closest to S
		distances = []
		for i, D_point in enumerate(D):
			for S_point in S:
				distances.append([ dist(S_point,D_point), i])

		pointsToDelete = []
		for i, point in enumerate(sorted(distances, key=lambda p: p[0])):
			if(i >= len(D)/2):
				break
			pointsToDelete.append(point[1])

		print "                  b: " + str(b)
		print "   Points to delete: " + str(len(pointsToDelete))
		return "a"

def readInput():
 	# Remove this for production. Uses a local file so i can run from Sublime
	# return only_dev_read_data_from_file();

	ret = []
	for line in sys.stdin:
		ret.append(map(float,line.split(" ")))
	return np.array(ret);

def printResult(coreset):
	for line in coreset:
		print(" ".join(map(str, line)))


# Used for dev. 
def only_dev_read_data_from_file():
	data = np.load("../data/tiny_subset")['arr_0']
	return data;

if __name__ == "__main__":
	data = readInput()
	k = 200
	coreset = calculateCoreset_naive(data ,k)
	printResult(coreset)

