#!/usr/local/bin/python -u

import sys
import numpy as np

if __name__ == "__main__":
    coefficients = []
    for line in sys.stdin:
        coefficients.append(map(float, line.split()))

    coefficients_mean = np.mean(coefficients, axis=0)
    for coefficient in coefficients_mean:
        sys.stdout.write (str(coefficient) + " ")
