0x01. Python - if/else, loops, functions

General

Why Python programming is awesome

Why indentation is so important in Python

How to use the if, if ... else statements

How to use comments

How to affect values to variables

How to use the while and for loops

How is Python’s for different from C‘s?

How to use the break and continues statements

How to use else clauses on loops

What does the pass statement do, and when to use it

How to use range

What is a function and how do you use functions

What does return a function that does not use any return statement

Scope of variables

What’s a traceback

What are the arithmetic operators and how to use them

Requirements

Python Scripts

Allowed editors: vi, vim, emacs

All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)

All your files should end with a new line

The first line of all your files should be exactly #!/usr/bin/python3

A README.md file, at the root of the folder of the project, is mandatory

Your code should use the pycodestyle (version 2.7.*)

All your files must be executable

The length of your files will be tested using wc


EXample

>>> for n in range(2, 10):
...     for x in range(2, n):
...         if n % x == 0:
...             print(n, 'equals', x, '*', n//x)
...             break
...     else:
...         # loop fell through without finding a factor
...         print(n, 'is a prime number')
...
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3


Example

>>> for num in range(2, 10):
...     if num % 2 == 0:
...         print("Found an even number", num)
...         continue
...     print("Found an odd number", num)
...
Found an even number 2
Found an odd number 3
Found an even number 4
Found an odd number 5
Found an even number 6
Found an odd number 7
Found an even number 8
Found an odd number 9
