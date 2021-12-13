0x08. Python - More Classes and Objects

Object Oriented Programming

Classes and objects are the two main aspects of object oriented programming. A class creates a new type where objects are instances of the class. An analogy is that you can have variables of type int which translates to saying that variables that store integers are variables which are instances (objects) of the int class.

Objects can store data using ordinary variables that belong to the object. Variables that belong to an object or class are referred to as fields. Objects can also have functionality by using functions that belong to a class. Such functions are called methods of the class. This terminology is important because it helps us to differentiate between functions and variables which are independent and those which belong to a class or object. Collectively, the fields and methods can be referred to as the attributes of that class.

Fields are of two types - they can belong to each instance/object of the class or they can belong to the class itself. They are called instance variables and class variables respectively.

Classes

The simplest class possible is shown in the following example (save as oop_simplestclass.py).

class Person:

    pass  # An empty block

     p = Person()

      print(p)

Output:

$ python oop_simplestclass.py

  <__main__.Person instance at 0x10171f518>

Class And Object Variables


We have already discussed the functionality part of classes and objects (i.e. methods), now let us learn about the data part. The data part, i.e. fields, are nothing but ordinary variables that are bound to the namespaces of the classes and objects. This means that these names are valid within the context of these classes and objects only. That's why they are called name spaces.

There are two types of fields - class variables and object variables which are classified depending on whether the class or the object owns the variables respectively.

Class variables are shared - they can be accessed by all instances of that class. There is only one copy of the class variable and when any one object makes a change to a class variable, that change will be seen by all the other instances.

Object variables are owned by each individual object/instance of the class. In this case, each object has its own copy of the field i.e. they are not shared and are not related in any way to the field by the same name in a different instance. An example will make this easy to understand (save as oop_objvar.py):


lass Robot:

  """Represents a robot, with a name."""

    # A class variable, counting the number of robots
    population = 0

    def __init__(self, name):

 """Initializes the data."""
        self.name = name

      print("(Initializing {})".format(self.name))

        # When this person is created, the robot

    # adds to the population

  Robot.population += 1

     def die(self):
 
   """I am dying."""

      print("{} is being destroyed!".format(self.name))

        Robot.population -= 1

           if Robot.population == 0:

       print("{} was the last one.".format(self.name))
	    

     else:

       print("There are still {:d} robots working.".format(
                  Robot.population))

    def say_hi(self):
    
        """Greeting by the robot.

          Yeah, they can do that."""

       print("Greetings, my masters call me {}.".format(self.name))

    @classmethod
     
      def how_many(cls):

     """Prints the current population."""

   print("We have {:d} robots.".format(cls.population))


droid1 = Robot("R2-D2")

  droid1.say_hi()

 Robot.how_many()

droid2 = Robot("C-3PO")

 droid2.say_hi()

  Robot.how_many()

   print("\nRobots can do some work here.\n")

print("Robots have finished their work. So let's destroy them.")

droid1.die()

  droid2.die()

Robot.how_many()


Output:

$ python oop_objvar.py

(Initializing R2-D2)

Greetings, my masters call me R2-D2.

We have 1 robots.

(Initializing C-3PO)

Greetings, my masters call me C-3PO.

We have 2 robots.

Robots can do some work here.

Robots have finished their work. So let's destroy them.

R2-D2 is being destroyed!

There are still 1 robots working.

C-3PO is being destroyed!

C-3PO was the last one.

We have 0 robots.
