#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_diction_i = {}
    for x in a_dictionary.keys():
        new_diction_i[x] = a_dictionary[x] * 2
    return new_diction_i
