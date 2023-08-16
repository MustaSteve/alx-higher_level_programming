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
    current_num = 0
    num_prev = 0
    character_before = ""
    reslut = 0
    for i in roman_string:
        if i in roman_nums:
            current_num += roman_nums[i]
            if num_prev < roman_nums[i]:
                current_num -= number_prev * 2
            num_prev = roman_nums[i]
            if i == character_before:
                result += 1
                if result == 3:
                    return 0
            else:
                result = 0
            character_before = i[:]
    return current_num
