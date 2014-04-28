#!/usr/bin/env python2.7

import numpy as np
import sys
from sklearn import preprocessing, linear_model

# This function has to either stay in this form or implement the
# feature mapping. For details refer to the handout pdf.
def transform(x):
    x_power = x ** 2 
    x_transformed = np.hstack((x, x_power))
    return x_transformed

def read_input():
    input_stream = sys.stdin
#     input_stream = open('training', 'r')
    for line in input_stream:
        line = line.strip()
        label = int(line[0:2])
        feature = transform(np.array(map(float, line[3:].split())))
        labels.append(label)
        features.append(feature)
                
def train():
    classifier = linear_model.SGDClassifier(loss='hinge', penalty='l2', alpha=0.5, shuffle=True, fit_intercept=False, n_iter=150, learning_rate='invscaling', eta0=0.05)
    classifier.fit(features, labels);

    for coefficient in np.nditer(classifier.coef_):
        sys.stdout.write(str(coefficient) + " ")
    sys.stdout.write("\n")
    
if __name__ == '__main__':
    labels = []
    features = []
    read_input()
    features = preprocessing.scale(features)
    train()
    