#!/usr/bin/env python

import numpy as np
import sys

# Probably should move this somewhere else
THRESHOLD = 0.85

def jaccard_similarity(A, B):
    return len(A & B)/float(len(A | B))

def print_duplicates(videos):
#   print(videos)
    if len(videos) < 2:
        return

    # [(id, {shingles})]
    shingles = map(lambda string : (string.split()[0], set(string.split()[1:])), videos)
    for i in range(len(shingles)):
        id_i = int(shingles[i][0])
        s_i = shingles[i][1]
        for j in range(i+1, len(shingles)):
            id_j = int(shingles[j][0])
            s_j = shingles[j][1]
            sim = jaccard_similarity(s_i, s_j)
            if sim >= THRESHOLD:
                print("%d\t%d" % (min(id_i, id_j), max(id_i, id_j)))

last_key = None
key_count = 0
duplicates = []

for line in sys.stdin:
    line = line.strip()
    key, video_id = line.split("\t")

#   print(video_id + ' has key ' + key)

    if last_key is None:
        last_key = key

    if key == last_key:
        duplicates.append(video_id)
    else:
        # Key changed (previous line was k=x, this line is k=y)
        print_duplicates(duplicates)
        duplicates = [video_id]
        last_key = key

if len(duplicates) > 0:
    print_duplicates(duplicates)
