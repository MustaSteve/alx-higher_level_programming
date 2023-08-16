#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    dict_neu = a_dictionary.copy()
    for k, x in dict_neu.items():
        if x == value:
            del a_dictionary[k]
    return a_dictionary
