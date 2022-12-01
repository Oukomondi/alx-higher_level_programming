#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDig = abs(number) % 10
if number < 0:
    lastDig = -lastDig
print(f"Last digit of {number} is {lastDig} and is", end=" ")
if lastDig > 5:
    print("greater than 5")
elif lastDig == 0:
    print("0")
else:
    print("less than 6 and not 0")
