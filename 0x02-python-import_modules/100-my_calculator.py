#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    len = len(argv)
    if len != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    ops = {"+": add, "-": sub, "*": mul, "/": div}
    if sys.argv[2] not in list(ops.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    if argv[2] in ops:
        a = int(argv[1])
        b = int(argv[3])
        op = ops[argv[2]]
        result = op(a, b)
        print('{:d} {:s} {:d} = {:d}'.format(a, argv[2], b, result))
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
    exit(0)
    
