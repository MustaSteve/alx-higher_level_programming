#!/usr/bin/python3
def fizzbuzz():
    c = 1
    while(c < 100):

        if c % 5 == 0 and c % 3 == 0:
            print("FizzBuzz ", end='')
        elif c % 3 == 0:
            print("Fizz ", end='')
        elif c % 5 == 0:
            print("Buzz ", end='')
        else:
            print("{:d} ".format(c), end='')
        c += 1
    print("Buzz ", end='')
