#!/usr/bin/env python2.7

import numpy as np

data = np.load("../data/tiny_subset")['arr_0']

for dp in data:
	print " ".join(map(str,dp))