#!/usr/bin/python3

def best_score(a_dictionary):
    score = 0
    key = None
    if a_dictionary is None:
        return key
    for x, y in a_dictionary.items():
        if score < y:
            score = y
            key = x
    return key
