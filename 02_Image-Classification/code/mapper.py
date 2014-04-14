#!/usr/bin/env python

import numpy as np
import sys
from sklearn import preprocessing, linear_model


# This function has to either stay in this form or implement the
# feature mapping. For details refer to the handout pdf.
def transform(x):
#     print('transform: transforming data')
    x_transformed = preprocessing.scale(x)
    return x_transformed 

def read_input():
#     print('read_input: reading input')
    input_stream = sys.stdin
#     input_stream = open('training', 'r')
    for line in input_stream:
        line = line.strip()
        label = int(line[0:2])
        feature = np.array(map(float, line[3:].split()))
        
        labels.append(label)
        features.append(feature)
                
def train():
#     print('train: training data')
    classifier = linear_model.SGDClassifier(loss='hinge', penalty='l2', alpha=0.1, shuffle=True, fit_intercept=False, n_iter=10)
    classifier.fit(features_tranformed, labels);

    for coefficient in np.nditer(classifier.coef_):
        sys.stdout.write(str(coefficient) + " ")
    sys.stdout.write("\n")
    
    
if __name__ == '__main__':
#     print(sys.version)
    labels = []
    features = []
    read_input()
    features_tranformed = transform(features)
    train()
    
