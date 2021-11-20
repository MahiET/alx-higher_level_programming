0x03. Python - Data Structures: Lists, Tuples

Data Structures

 More on Lists

list.append(x)

Add an item to the end of the list. Equivalent to a[len(a):] = [x].

list.extend(iterable)

Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable.

list.insert(i, x)

Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).

list.remove(x)

Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.

list.pop([i])

Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. (The square brackets around the i in the method signature denote that the parameter is optional, not that you should type square brackets at that position. You will see this notation frequently in the Python Library Reference.)

list.clear()

Remove all items from the list. Equivalent to del a[:].

list.count(x)

Return the number of times x appears in the list.

list.sort(*, key=None, reverse=False)

Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).

list.reverse()

Reverse the elements of the list in place.

list.copy()
Return a shallow copy of the list. Equivalent to a[:].

Using Python as a Calculator

Numbers

The interpreter acts as a simple calculator: you can type an expression at it and it will write the value. Expression syntax is straightforward: the operators +, -, * and / work just like in most other languages (for example, Pascal or C); parentheses (()) can be used for grouping.

For example

2 + 2

4

50 - 5*6

20

(50 - 5*6) / 4

5.0

8 / 5  # division always returns a floating point number

1.6
