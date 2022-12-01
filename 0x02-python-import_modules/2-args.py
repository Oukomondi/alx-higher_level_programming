#!/usr/bin/python3
from sys import argv

argc = len(argv)

if __name__ == '__main__':
    if argc == 1:
        print(f"{argc - 1} arguments.")
    elif argc == 2:
        print(f"{argc - 1} argument:")
    else:
        print(f"{argc - 1} arguments:")

    index = 1
    while index < argc:
        print(f"{index}: {argv[index]}")
        index += 1
