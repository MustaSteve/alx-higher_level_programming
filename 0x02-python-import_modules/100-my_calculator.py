#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys


    if len(sys.argv) - 1 != 3:
        print("Usage: {} <a> <operator> <b>")
        sys.exit(1)
    ops = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div
    }
    if sys.argv[2] not in list(ops.keys()):
        nu1 = int(sys.argv[1])
        nu2 = int(sys.argv[3])
        print('{} {} {} = {}'.format(nu1, argv[2], nu2, ops[sys.argv[2]](nu1,nu2)))
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        sys.exit(1)
    exit(0)
