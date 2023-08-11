#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    len = len(argv)
    if len != 4:
        print("Usage: ./100-my_calculator.py <num1> <operator> <num2>")
        exit(1)
    num1 = int(argv[1])
    num2 = int(argv[3])
    if argv[2] == '+':
        print("{:d} + {:d} = {:d}".format(num1, num2, add(num1, num2)))
    elif argv[2] == '-':
        print("{:d} - {:d} = {:d}".format(num1, num2, sub(num1, num2))) 
    elif argv[2] == '*':
        print("{:d} * {:d} = {:d}".format(num1, num2, mul(num1, num2)))
    elif argv[2] == '/':
        print("{:d} / {:d} = {:d}".format(num1, num2, div(num1, num2)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
