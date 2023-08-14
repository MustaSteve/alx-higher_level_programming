#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_multi = []
    for i in my_list:
        if i % 2 == 0:
            new_multi.append(True)
        else:
            new_multi.append(False)
    
    return new_multi
