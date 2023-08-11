#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    summry = 0
    for j in range(1, len(sys.argv)):
        summry += int(sys.argv[j])
    print("{}".format(summry)
