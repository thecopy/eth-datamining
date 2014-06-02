#!/usr/bin/env python2.7

import numpy as np
import math
import random

article_features = dict()
A = dict()
A_inverse = dict()
b = dict()
d = 6
alpha = 0.2
chosen = 0

# Evaluator will call this function and pass the article features.
# Check evaluator.py description for details.
def set_articles(articles):
    for article in articles:
        article_features[article] = np.array(articles[article])

# This function will be called by the evaluator.
# Check task description for details.
def update(reward):
    if reward == -1:
        return

    article_A = A[chosen]
    article_b = b[chosen]
    article_feature = article_features[chosen]
    A[chosen] = article_A + np.dot(article_feature, article_feature.T)
    b[chosen] = article_b + reward * article_feature
    A_inverse[chosen] = np.linalg.inv(A[chosen])

# This function will be called by the evaluator.
# Check task description for details.
def reccomend(timestamp, user_features, articles):
    p = []
    article_ids = []
    for article in articles:
        if article not in A:
            A[article] = np.identity(d)
            A_inverse[article] = np.linalg.inv(np.identity(d))
            b[article] = np.zeros(d)

        article_A_inverse = A_inverse[article]
        article_b = b[article]
        article_feature = article_features[article]

        article_theta = np.dot(article_A_inverse, article_b)
        article_p = np.dot(article_theta.T, article_feature)
        + alpha * math.sqrt(
            np.dot(
                np.dot(
                    article_feature.T,
                    article_A_inverse
                ),
                article_feature
            )
        )
        article_ids.append(article)
        p.append(article_p)

    global chosen

    max_p_indices = [i for i, j in enumerate(p) if j == max(p)]
    chosen = article_ids[random.randint(0, len(max_p_indices) - 1)]
    return chosen