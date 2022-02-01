# 0x0D. SQL - Introduction

Basic SQL statements: DDL and DML

SQL statements are divided into two major categories: data definition language (DDL) and data manipulationlanguage (DML). Both of these categories contain far more statements than we can present here, and each ofthe statements is far more complex than we show in this introduction.

Data definition language(DDL)

DDL statements are used to build and modify the structure of your tables and other objects in the database. When you execute a DDL statement, it takes effect immediately.

  CREATE TABLE <table name>

    ( 
        <attribute name 1> <data type 1>,
	
            ...
	
           <attribute name n> <data type n>)


Data manipulation language(DML)

DML statements are used to work with the data in tables. When you are connected to most multi-user databases (whether in a client program or by a connection from a Web page script), you are in effect working with a private copy of your tables that can’t be seen by anyone else until you are finished (or tell the system that you are finished). You have already seen the SELECT statement; it is considered to be part of DML even though it just retreives data rather than modifying it.

INSERT INTO <table name>

    VALUES (<value 1>, ... <value n>);

Basic queries: SQL and RA
=

SQL

In SQL, to retrieve data stored in our tables, we use the SELECT statement. The result of this statement is always in the form of a table that we can view with our database client software or use with programming languages to build dynamic web pages or desktop applications. While the result may look like a table, it is not stored in the database like the named tables are. The result of a SELECT statement can also be used as part of another statement.

Basic syntax of SELECT statement

SELECT {attribute}+

  FROM {table}+

  [ WHERE {boolean predicate to pick rows} ]
  
     [ ORDER BY {attribute}+ ];


