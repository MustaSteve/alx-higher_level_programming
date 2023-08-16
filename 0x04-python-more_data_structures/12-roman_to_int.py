#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    my_dictionary = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    num_curr = 0
    num_bef = 0
    char_bef = ""
    count = 0
    for i in roman_string:
        if i in my_dictionary:
            num_curr += my_dictionary[i]
            if num_bef < my_dictionary[i]:
                num_curr -= num_bef * 2
            num_bef = my_dictionary[i]
            if i == character_before:
                count += 1
                if count == 3:
                    return 0
            else:
                count = 0
            char_bef = i[:]
    return num_curr
