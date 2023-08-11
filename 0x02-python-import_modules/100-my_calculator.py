#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    len = len(argv)
    if len != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    n1 = int(argv[1])
    n2 = int(argv[3])
    if argv[2] == '+':
        print("{:d} + {:d} = {:d}".format(n1, n2, add(n1, n2)))
    elif argv[2] == '-':
        print("{:d} - {:d} = {:d}".format(n1, n2, sub(n1, n2))) 
    elif argv[2] == '*':
        print("{:d} * {:d} = {:d}".format(n1, n2, mul(n1, n2)))
    elif argv[2] == '/':
        print("{:d} / {:d} = {:d}".format(n1, n2, div(n1, n2)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
