
                       0x07. Python - Test-driven development

doctest — Testing Through Documentation

doctest tests source code by running examples embedded in the documentation and verifying that they produce the expected results. It works by parsing the help text to find examples, running them, then comparing the output text against the expected value. Many developers find doctest easier to use than unittest because, in its simplest form, there is no API to learn before using it. However, as the examples become more complex the lack of fixture management can make writing doctest tests more cumbersome than using unittest.

Getting Started

The first step to setting up doctests is to use the interactive interpreter to create examples and then copy and paste them into the docstrings in the module. Here, my_function() has two examples given:

# doctest_simple.py

def my_function(a, b):
    """

    >>> my_function(2, 3)

       6
    >>> my_function('a', 3)

       'aaa'
    
      """

       return a * b


The doctest module searches for pieces of text that look like interactive Python sessions, and then executes those sessions to verify that they work exactly as shown. There are several common ways to use doctest:

. To check that a module’s docstrings are up-to-date by verifying that all interactive examples still work as documented.

. To perform regression testing by verifying that interactive examples from a test file or a test object work as expected.

. To write tutorial documentation for a package, liberally illustrated with input-output examples. Depending on whether the examples or the expository text are emphasized, this has the flavor of “literate testing” or “executable documentation”.

    Option Flags

doctest.DONT_ACCEPT_TRUE_FOR_1

if an expected output block contains just 1, an actual output block containing just 1 or just True is considered to be a match, and similarly for 0 versus False. When DONT_ACCEPT_TRUE_FOR_1 is specified, neither substitution is allowed.

doctest.DONT_ACCEPT_BLANKLINE

When specified, all sequences of whitespace (blanks and newlines) are treated as equal. Any sequence of whitespace within the expected output will match any sequence of whitespace within the actual output. By default, whitespace must match exactly. NORMALIZE_WHITESPACE is especially useful when a line of expected output is very long, and you want to wrap it across multiple lines in your source.

doctest.ELLIPSIS

When specified, an ellipsis marker (...) in the expected output can match any substring in the actual output. This includes substrings that span line boundaries, and empty substrings, so it’s best to keep usage of this simple. Complicated uses can lead to the same kinds of “oops, it matched too much!” surprises that .* is prone to in regular expressions.

doctest.IGNORE_EXCEPTION_DETAIL

When specified, an example that expects an exception passes if an exception of the expected type is raised, even if the exception detail does not match. For example, an example expecting ValueError: 42 will pass if the actual exception raised is ValueError: 3*14, but will fail, e.g., if TypeError is raised.

       Directives

Doctest directives may be used to modify the option flags for an individual example. Doctest directives are special Python comments following an example’s source code:

directive             ::=  "#" "doctest:" directive_options

directive_options     ::=  directive_option ("," directive_option)\*

directive_option      ::=  on_or_off directive_option_name

on_or_off             ::=  "+" \| "-"

directive_option_name ::=  "DONT_ACCEPT_BLANKLINE" \| "NORMALIZE_WHITESPACE" \| ...

Whitespace is not allowed between the + or - and the directive option name. The directive option name can be any of the option flag names explained above.
