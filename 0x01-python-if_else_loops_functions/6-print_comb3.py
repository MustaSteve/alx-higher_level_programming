#!/usr/bin/python3
for di in range(0, 10):
    for di2 in range(di1 + 1, 10):
        if di1 == 8 and di2 == 9:
            print("{}{}".format(di1, di2))
        else:
            print("{}{}".format(di1, di2), end=", ")
