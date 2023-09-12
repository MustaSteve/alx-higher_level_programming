#!/usr/bin/python3
'''Write a function that creates an Object from a “JSON file”'''


import json
'''the json module'''


def load_from_json_file(filename):
    '''creates an Object from a “JSON file"'''
    with open(filename, "r", encoding="utf-8") as f:
        return json.loads(f.read())
