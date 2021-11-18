#!/usr/bin/python3
import sys

if __name__ != "__main__":
    exit()

argumentStr = "{} argument"
argc = len(sys.argv) - 1
if argc == 0:
    argumentStr += 'z.'
elif argc == 1:
    argumentStr += ':'
else:
    argumentStr += 'z:'
print(argumentStr.format(argc))

i = 0
for argument in sys.argv:
    if i != 0:
        print("{}: {}".format(i, argument))
    i += 1
