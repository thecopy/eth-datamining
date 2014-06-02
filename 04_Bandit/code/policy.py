#!/usr/bin/env python2.7

import numpy as np
import math

article_features = dict()
A = dict()
b = dict()
d = 6
alpha = 2.15
chosen = 0

# Evaluator will call this function and pass the article features.
# Check evaluator.py description for details.
def set_articles(articles):
    for article in articles:
        article_features[article] = np.array(articles[article],
                                             dtype=np.float64)

# This function will be called by the evaluator.
# Check task description for details.
def update(reward):
    if reward == -1:
        return

    article_A = A[chosen]
    article_b = b[chosen]
    article_feature = article_features[chosen]
    A[chosen] = article_A + np.dot(article_feature, np.transpose(article_feature))
    b[chosen] = article_b + reward * article_feature

# This function will be called by the evaluator.
# Check task description for details.
def reccomend(timestamp, user_features, articles):
    p = []
    article_ids = []
    for article in articles:
        if article not in A:
            A[article] = np.identity(d)
            b[article] = np.zeros(d)

        article_A = A[article]
        article_A_inverse = np.linalg.inv(article_A)
        article_b = b[article]
        article_feature = article_features[article]

        article_theta = np.dot(article_A_inverse, article_b)
        article_p = np.dot(np.transpose(article_theta), article_feature)
        + alpha * math.sqrt(
            np.dot(
                np.dot(
                    np.transpose(article_feature),
                    article_A_inverse
                ),
                article_feature
            )
        )
        article_ids.append(article)
        p.append(article_p)

    global chosen
    chosen = article_ids[np.argmax(p)]
    return chosen