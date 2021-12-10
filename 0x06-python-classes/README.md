0x06. Python - Classes and Objects

Class Attributes

Instance attributes are owned by the specific instances of a class. That is, for two different instances, the instance attributes are usually different. You should by now be familiar with this concept which we introduced in our previous chapter.

Class attributes are attributes which are owned by the class itself. They will be shared by all the instances of the class. Therefore they have the same value for every instance. We define class attributes outside all the methods, usually they are placed at the top, right below the class header.

we can see that the class attribute "a" is the same for all instances, in our examples "x" and "y". Besides this, we see that we can access a class attribute via an instance or via the class name:


class A:

    a = "I am a class attribute!"
    
x = A()

y = A()

x.a

OUTPUT:

'I am a class attribute!'

Properties vs. Getters and Setters

belief that a proper Python class should encapsulate private attributes by using getters and setters. As soon as one of these programmers introduces a new attribute, he or she will make it a private variable and creates "automatically" a getter and a setter for this attribute. Such programmers may even use an editor or an IDE, which automatically creates getters and setters for all private attributes. These tools even warn the programmer if she or he uses a public attribute! Java programmers will wrinkle their brows, screw up their noses, or even scream with horror when they read the following: The Pythonic way to introduce attributes is to make them public.

example

class P:
    def __init__(self, x):
        self.__x = x
    def get_x(self):
        return self.__x
    def set_x(self, x):
        self.__x = x

from mutators import P
p1 = P(42)
p2 = P(4711)
p1.get_x()


OUTPUT:

42

p1.set_x(47)
p1.set_x(p1.get_x()+p2.get_x())
p1.get_x()

OUTPUT:

4758

Let's rewrite the class P in a Pythonic way. No getter, no setter and instead of the private attribute self.__x we use a public one:

class P:
    def __init__(self,x):
        self.x = x
	