#!/usr/bin/python3
for firstDigit in range(0, 10):
    for secDigit in range(firstDigit + 1, 10):
        if firstDigit == 8 and secDigit == 9:
            print("{}{}".format(firstDigit, secDigit))
        else:
            print("{}{}".format(firstDigit, secDigit), end=', ')
