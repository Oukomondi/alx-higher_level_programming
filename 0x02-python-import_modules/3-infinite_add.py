#!/usr/bin/python3
from sys import argv


def addArgs():
    argc = len(argv)
    if argc == 1:
        return 0

    add = 0
    index = 1
    while index < argc:
        add += int(argv[index])
        index += 1

    return add


if __name__ == '__main__':
    print(addArgs())
