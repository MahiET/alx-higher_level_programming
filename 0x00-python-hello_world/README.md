0x00. Python - Hello, World


Python is an easy to learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python’s elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms.

Python enables programs to be written compactly and readably. Programs written in Python are typically much shorter than equivalent C, C++, or Java programs, for several reasons:

the high-level data types allow you to express complex operations in a single statement;

statement grouping is done by indentation instead of beginning and ending brackets;

no variable or argument declarations are necessary.

The Interpreter and Its Environment

Source Code Encoding

# -*- coding: encoding -*

# -*- coding: cp1252 -*-

#!/usr/bin/env python3
# -*- coding: cp1252 -*


Using Formatters

Formatters work by putting in one or more replacement fields or placeholders — defined by a pair of curly braces {} — into a string and calling the str.format() method. You’ll pass into the method the value you want to concatenate with the string. This value will be passed through in the same place that your placeholder is positioned when you run the program.

Example

print("Sammy has {} balloons.".format(5))

Output

Sammy has 5 balloons.
