if __name__ == "__main__":
    import sys

    ele = len(sys.argv) - 1
    if ele == 0:
        print("0 arguments.")
    elif ele == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(ele))
    for j in range(ele):
        print("{}: {}".format(j + 1, sys.argv[j + 1]))
