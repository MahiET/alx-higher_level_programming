#!/usr/bin/python3
import sys

if __name__ != "__main__":
    exit()

argumentStr = "{:d} argument"
argc = len(sys.argv) - 1
if argc == 0:
    argumentStr += 'x.'
elif argc == 1:
    argumentStr += ':'
else:
    argumentStr += 'x:'
print(argumentStr.format(argc))

a = 0
for argument in sys.argv:
    if a != 0:
        print("{:d}: {:x}".format(a, argument))
    a += 1
