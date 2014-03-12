#!/usr/bin/env python

import sys

list = []

for line in sys.stdin:
	line = line.strip()
	key, video_id = line.split('\t')
	list.append((key, video_id))

for pair in sorted(list, key=lambda p: p[0]):
	sys.stdout.write(pair[0] + '\t' + pair[1] + '\n')