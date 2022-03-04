# 0x0F. Python - Object-relational mapping

Full Stack Python
=

*/Object-relational Mappers (ORMs)/*

An object-relational mapper (ORM) is a code library that automates the transfer of data stored in relational database tables into objects that are more commonly used in application code.

  ORMs provide a high-level abstraction upon a relational database that allows a developer to write Python code instead ofSQL to create, read, update and delete data and schemas in their database. Developers can use the programming languagethey are comfortable with to work with a database instead of writing SQL statements or stored procedures.


SQLAlchemy ORM Tutorial for Python Developers
=

SQLAlchemy
=

SQLAlchemy is a library that facilitates the communication between Python programs and databases. Most of the times, this library is used as an Object Relational Mapper (ORM) tool that translates Python classes to tables on relational databases and automatically converts function calls to SQL statements. SQLAlchemy provides a standard interface that allows developers to create database-agnostic code to communicate with a wide variety of database engines.

 Python developer needs to understand before dealing with SQLAlchemy applications.

Python DBAPI

The Python DBAPI (an acronym for DataBase API) was created to specify how Python modules that integrate with databases should expose their interfaces. Although we won't interact with this API directly—we will use SQLAlchemy as a facade to it—it's good to know that it defines how common functions like connect, close, commit, and rollback must behave. Consequently, whenever we use a Python module that adheres to the specification, we can rest assured that we will find these functions and that they will behave as expected.

SQLAlchemy Engines
=

SQLAlchemy to interact with a database, we need to create an Engine. Engines, on SQLAlchemy, are used to manage two crucial factors: Pools and Dialects. The following two sections will explain what these two concepts are, but for now it suffices to say that SQLAlchemy uses them to interact with DBAPI functions.

from sqlalchemy import create_engine

engine = create_engine('postgresql://usr:pass@localhost:5432/sqlalchemy')

SQLAlchemy ORM
+

ORM, which stands for Object Relational Mapper, is the specialization of the Data Mapper design pattern that addresses relational databases like MySQL, Oracle, and PostgreSQL. As explained by Martin Fowler in the article, Mappers are responsible for moving data between objects and a database while keeping them independent of each other. As object-oriented programming languages and relational databases structure data on different ways, we need specific code to translate from one schema to the other.

SQLAlchemy Data Types

For example, booleans, dates, times, strings, and numeric values are a just a subset of the types that SQLAlchemy provides abstractions for. Besides these basic types, SQLAlchemy includes support for a few vendor-specific types (like JSON) and also allows developers to create custom types and redefine existing ones.

class Product(Base):

    __tablename__ = 'products'

    id=Column(Integer, primary_key=True)

    title=Column('title', String(32))

    in_stock=Column('in_stock', Boolean)

    quantity=Column('quantity', Integer)

    price=Column('price', Numeric)
    