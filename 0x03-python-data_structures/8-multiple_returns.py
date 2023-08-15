#!/usr/bin/python3

def multiple_returns(sentence):
    if len(sentence) == 0:
        cni = None
    else:
        cni = sentence[0]
    return (len(sentence), cni)
