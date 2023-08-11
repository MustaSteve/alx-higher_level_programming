#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    argc = len(argv)
    if argc != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>'.format(argv[0]))
        exit(1)
    ops = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div
    }
    if argv[2] not in list(ops.keys()):
        numbre1 = int(argv[1])
        numbre2 = int(argv[3])
        op = ops[argv[2]]
        result = op(numbre1, numbre2)
        print('{:d} {:s} {:d} = {:d}'.format(numbre1, argv[2], numbre2, result))
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
    exit(0)
