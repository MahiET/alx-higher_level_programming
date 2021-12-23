# 0x0B. Python - Input/Output

# Fancier Output Formatting
So far we’ve encountered two ways of writing values: expression statements and the print() function. (A third way is using the write() method of file objects; the standard output file can be referenced as sys.stdout. See the Library Reference for more information on this.)

Often you’ll want more control over the formatting of your output than simply printing space-separated values. There are several ways to format output.

To use formatted string literals, begin a string with f or F before the opening quotation mark or triple quotation mark. Inside this string, you can write a Python expression between { and } characters that can refer to variables or literal values.

 year = 2016

   event = 'Referendum'

     f'Results of the {year} {event}'

       'Results of the 2016 Referendum'

The str.format() method of strings requires more manual effort. You’ll still use { and } to mark where a variable will be substituted and can provide detailed formatting directives, but you’ll also need to provide the information to be formatted.

yes_votes = 42_572_654

  no_votes = 43_132_495

    percentage = yes_votes / (yes_votes + no_votes)

      '{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)

          ' 42572654 YES votes  49.67%'

Finally, you can do all the string handling yourself by using string slicing and concatenation operations to create any layout you can imagine. The string type has some methods that perform useful operations for padding strings to a given column width.

# Reading and Writing Files

open() returns a file object, and is most commonly used with two arguments: open(filename, mode).

The first argument is a string containing the filename. The second argument is another string containing a few characters describing the way in which the file will be used. mode can be 'r' when the file will only be read, 'w' for only writing (an existing file with the same name will be erased), and 'a' opens the file for appending; any data written to the file is automatically added to the end. 'r+' opens the file for both reading and writing. The mode argument is optional; 'r' will be assumed if it’s omitted.

# Methods of File Objects


o read a file’s contents, call f.read(size), which reads some quantity of data and returns it as a string (in text mode) or bytes object (in binary mode). size is an optional numeric argument. When size is omitted or negative, the entire contents of the file will be read and returned; it’s your problem if the file is twice as large as your machine’s memory. Otherwise, at most size characters (in text mode) or size bytes (in binary mode) are read and returned. If the end of the file has been reached, f.read() will return an empty string ('').

# Python Test Cases

. Allowed editors: vi, vim, emacs

. All your files should end with a new line

. All your test files should be inside a folder tests

. All your test files should be text files (extension: .txt)

. All your tests should be executed by using this command: python3 -m doctest ./tests/*

. All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')

. All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')

. All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')

. A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

. We strongly encourage you to work together on test cases, so that you don’t miss any edge case
