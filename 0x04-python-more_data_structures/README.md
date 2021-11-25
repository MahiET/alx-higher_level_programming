0x04. Python - More Data Structures: Set, Dictionary

Sets

Python also includes a data type for sets. A set is an unordered collection with no duplicate elements. Basic uses include membership testing and eliminating duplicate entries. Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.

Curly braces or the set() function can be used to create sets. Note: to create an empty set you have to use set(), not {}; the latter creates an empty dictionary, a data structure that we discuss in the next section.

For Example

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}

print(basket)                      # show that duplicates have been removed

{'orange', 'banana', 'pear', 'apple'}

'orange' in basket                 # fast membership testing

True

'crabgrass' in basket

False

 Dictionaries


Another useful data type built into Python is the dictionary (see Mapping Types — dict). Dictionaries are sometimes found in other languages as “associative memories” or “associative arrays”. Unlike sequences, which are indexed by a range of numbers, dictionaries are indexed by keys, which can be any immutable type; strings and numbers can always be keys. Tuples can be used as keys if they contain only strings, numbers, or tuples; if a tuple contains any mutable object either directly or indirectly, it cannot be used as a key. You can’t use lists as keys, since lists can be modified in place using index assignments, slice assignments, or methods like append() and extend()

Performing list(d) on a dictionary returns a list of all the keys used in the dictionary, in insertion order (if you want it sorted, just use sorted(d) instead). To check whether a single key is in the dictionary, use the in keyword.

For Example

tel = {'jack': 4098, 'sape': 4139}

tel['guido'] = 4127

tel

{'jack': 4098, 'sape': 4139, 'guido': 4127}

tel['jack']

4098

del tel['sape']

tel['irv'] = 4127

tel

{'jack': 4098, 'guido': 4127, 'irv': 4127}

list(tel)

['jack', 'guido', 'irv']

sorted(tel)

['guido', 'irv', 'jack']

'guido' in tel

True

'jack' not in tel

False

More on Conditions

he comparison uses lexicographical ordering: first the first two items are compared, and if they differ this determines the outcome of the comparison; if they are equal, the next two items are compared, and so on, until either sequence is exhausted. If two items to be compared are themselves sequences of the same type, the lexicographical comparison is carried out recursively. If all items of two sequences compare equal, the sequences are considered equal.

ForExample

(1, 2, 3)              < (1, 2, 4)

[1, 2, 3]              < [1, 2, 4]

'ABC' < 'C' < 'Pascal' < 'Python'

(1, 2, 3, 4)           < (1, 2, 4)

(1, 2)                 < (1, 2, -1)

(1, 2, 3)             == (1.0, 2.0, 3.0)

(1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)