#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        for count, v in enumerate(x):
            print("{:d}".format(v), end="")
            if count != (len(x) - 1):
                print("{}".format(" "), end="")
        print()
