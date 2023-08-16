#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_nums = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
    result_i = 0
    value_bef = 0

    for charc in reversed(roman_string):
        value_i = roman_nums.get(charc, 0)
        if value_i >= value_bef:
            result_i += value_i
        else:
            result_i -= value_i
        value_bef = value_i
    return result_i
