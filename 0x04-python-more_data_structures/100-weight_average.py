#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    numbre = 0
    count = 0

    for yun in my_list:
        numbre += yun[0] * yun[1]
        count += yun[1]

    return (numbre / count)
