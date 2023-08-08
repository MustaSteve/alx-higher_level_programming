#!/usr/bin/python3
def print_last_digit(number):
    l_digit = number % 10
    if number < 0:
        l_digit = (-number % 10)
    print("{:d}".format(l_digit), end='')
    return l_digit
