#!/usr/bin/env python2.7

# This function has to either stay in this form or implement the
# feature mapping. For details refer to the handout pdf.
def transform(x_original):
    return x_original

def SGD(x):
	pass


if __name__ == "__main__":
	data = [];
	for line in sys.stdin:
        line = line.strip()
        label = int(line[0:2])
        features = line[3:].split()
        data.push( ( id, transform(features) ) )

    SGD(data)