# 0x09. Python - Everything is object

A list is an ordered set of values, where each value is identified by an index. The values that make up a list are called its elements. Lists are similar to strings, which are ordered sets of characters, except that the elements of a list can have any type. Lists and strings — and other things that behave like ordered sets — are called sequences.

# The Object Metaphor

Objects combine data values with behavior. Objects represent information, but also behave like the things that they represent. The logic of how an object interacts with other objects is bundled along with the information that encodes the object's value. When an object is printed, it knows how to spell itself out in text. If an object is composed of parts, it knows how to reveal those parts on demand. Objects are both information and processes, bundled together to represent the properties, interactions, and behaviors of complex things.

Object behavior is implemented in Python through specialized object syntax and associated terminology, which we can introduce by example. A date is a kind of object.

    >>> from datetime import date

The name date is bound to a class. As we have seen, a class represents a kind of value. Individual dates are called instances of that class. Instances can be constructed by calling the class on arguments that characterize the instance.

   >>> tues = date(2014, 5, 13)
   
While tues was constructed from primitive numbers, it behaves like a date. For instance, subtracting it from another date will give a time difference, which we can print.

>>> print(date(2014, 5, 19) - tues)

    6 days, 0:00:00

# Sequence Objects

Instances of primitive built-in values such as numbers are immutable. The values themselves cannot change over the course of program execution. Lists on the other hand are mutable.

Mutable objects are used to represent values that change over time. A person is the same person from one day to the next, despite having aged, received a haircut, or otherwise changed in some way. Similarly, an object may have changing properties due to mutating operations. For example, it is possible to change the contents of a list. Most changes are performed by invoking methods on list objects.

# Immutable vs Mutable types

I'm confused on what an immutable type is. I know the float object is considered to be immutable, with this type of example from my book:
class RoundFloat(float):

    def __new__(cls, val):
   
        return float.__new__(cls, round(val, 2))
	
this considered to be immutable because of the class structure / hierarchy?, meaning float is at the top of the class and is its own method call. Similar to this type of example (even though my book says dict is mutable):

class SortedKeyDict(dict):

    def __new__(cls, val):
    
        return dict.__new__(cls, val.clear())

Whereas something mutable has methods inside the class, with this type of example:

class SortedKeyDict_a(dict):

    def example(self):
    
        return self.keys()
