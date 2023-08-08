#!/usr/bin/python3
j = 0
for n in range(ord('p'), ord('d') - 1, -1):
    print("{}".format(chr(n - j)), end="")
    j = 32 if j == 0 else 0
