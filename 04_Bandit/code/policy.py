#!/usr/bin/env python2.7

import numpy as np
import math

article_features = dict()
A = dict()
A_inverse = dict()
b = dict()
d = 12
alpha = 0.3
chosen_article = 0
chosen_feature = []

# Evaluator will call this function and pass the article features.
# Check evaluator.py description for details.


def set_articles(articles):
    global article_features, A, A_inverse, b, d, alpha, chosen_article, \
        chosen_feature

    for article in articles:
        article_features[article] = articles[article]

# This function will be called by the evaluator.
# Check task description for details.


def update(reward):
    global article_features, A, A_inverse, b, d, alpha, chosen_article, \
        chosen_feature

    if reward == -1:
        return

    A[chosen_article] += np.outer(chosen_feature, chosen_feature)
    b[chosen_article] += reward * chosen_feature
    A_inverse[chosen_article] = np.linalg.inv(A[chosen_article])

# This function will be called by the evaluator.
# Check task description for details.


def reccomend(timestamp, user_feature, articles):
    global article_features, A, A_inverse, b, d, alpha, chosen_article, \
        chosen_feature

    p = []
    article_ids = []

    for article in articles:
        if article not in A:
            A[article] = np.identity(d)
            A_inverse[article] = np.identity(d)
            b[article] = np.zeros(d)

        article_A_inverse = A_inverse[article]
        article_b = b[article]
        feature = np.array(article_features[article] + user_feature)

        article_theta = np.dot(article_A_inverse, article_b)
        article_p = np.dot(article_theta, feature) + \
            alpha * math.sqrt(
                np.dot(
                    np.dot(
                        feature,
                        article_A_inverse
                    ),
                    feature
                )
            )
        p.append(article_p)
        article_ids.append(article)

    chosen_article = article_ids[np.argmax(p)]
    chosen_feature = np.array(article_features[chosen_article] + user_feature)
    return chosen_article
