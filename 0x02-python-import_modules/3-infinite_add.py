#!/usr/bin/python3


if __name__ != "__main__":
    exit()
    
import sys

a = 0
result = 0
for argument in sys.argv:
    if a != 0:
        result += int(argument)
    else:
        a += 1
print("{:d}".format(result))
