#!/usr/bin/python3
if __name__ == "__main__":
    import sys


     element= len(sys.argv) - 1
    if element == 0:
        print("0 arguments.")
    elif element == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(element))
    for j in range(element):
        print("{}: {}".format(j + 1, sys.argv[j + 1]))
