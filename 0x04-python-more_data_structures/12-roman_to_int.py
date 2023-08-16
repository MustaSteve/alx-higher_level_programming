#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    my_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
    count = 0
    number_before = 0

    for char in reversed(roman_string):
        count = my_dict.get(char, 0)
        if value >= number_before:
            count += value
        else:
            count -= value
        number_before = value
    return count
