#!/usr/bin/python3
for di1 in range(0, 10):
    for di2 in range(di1 + 1, 10):
        if di1 == 8 and di2 == 9:
            print("{:02d}".format(di1, di2))
        else:
            print("{:02d}".format(di1, di2), end=", ")
