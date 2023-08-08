#!/usr/bin/python3
for l in range(97, 123):
    if chr(l) not in ('q', 'e'):
        print("{}".format(chr(l)), end="")
