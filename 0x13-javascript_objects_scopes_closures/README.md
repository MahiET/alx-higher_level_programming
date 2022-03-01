# 0x13. JavaScript - Objects, Scopes and Closures

Object basics
=

An object is a collection of related data and/or functionality. These usually consist of several variables and functions (which are called properties and methods when they are inside objects). Let's work through an example to understand what they look like.

Now open your browser's JavaScript console, enter person into it, and press Enter/Return. You should get a result similar to one of the below lines:

[object Object]
Object { }
{ }

Classes in JavaScript
=

Classes and constructors

This declares a class called Person, with:

a name property.

a constructor that takes a name parameter that is used to initialize the new object's name property

an introduceSelf() method that can refer to the object's properties using this.

The name; declaration is optional: you could omit it, and the line this.name = name; in the constructor will create the name property before initializing it. However, listing properties explicitly in the class declaration might make it easier for people reading your code to see which properties are part of this class.

You could also initialize the property to a default value when you declare it, with a line like name = '';.

const giles = new Person('Giles');

giles.introduceSelf(); // Hi! I'm Giles

Classes
=

Classes are a template for creating objects. They encapsulate data with code towork on that data. Classes in JS are built on prototypes but also have some syntax and semantics that are not shared with ES5 class-like semantics. 

Class declarations

One way to define a class is using a class declaration. To declare a class, youuse the class keyword with the name of the class ("Rectangle" here).

class Rectangle {
  constructor(height, width) {
    this.height = height;
    this.width = width;
  }
}


The prototype chain
=
This is an object with one data property, city, and one method, greet(). If youtype the object's name followed by a period into the console, like myObject., then the console will pop up a list of all the properties available to this object. You'll see that as well as city and greet, there are lots of other properties!

__defineGetter__

__defineSetter__

__lookupGetter__

__lookupSetter__

__proto__

city

constructor

greet

hasOwnProperty

isPrototypeOf

propertyIsEnumerable

toLocaleString

toString

toValueOf
