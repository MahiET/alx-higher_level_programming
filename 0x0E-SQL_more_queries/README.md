# 0x0E. SQL - More queries

Primary key
=

The PRIMARY KEY constraint uniquely identifies each record in a database table. It is a special case of unique keys. Primary keys cannot be NULL, unique keys can be. There can be more UNIQUE columns, but only one primary key in a table. Primary keys are important when designing the database tables. Primary keys are unique ids. We use them to refer to table rows. Primary keys become foreign keys in other tables, when creating relations among tables.

mysql> DROP TABLE Brands;

mysql> CREATE TABLE Brands(Id INTEGER PRIMARY KEY, BrandName VARCHAR(30) UNIQUE);


The Id column of the Brands table becomes a primary key.

mysql> DESCRIBE Brands;

+-----------+-------------+------+-----+---------+-------+
| Field     | Type        | Null | Key | Default | Extra |
+-----------+-------------+------+-----+---------+-------+
| Id        | int(11)     | NO   | PRI | NULL    |       |
| BrandName | varchar(30) | YES  | UNI | NULL    |       |
+-----------+-------------+------+-----+---------+-------+


Foreign key

A FOREIGN KEY in one table points to a PRIMARY KEY in another table. It is a referential constraint between two tables. The foreign key identifies a column or a set of columns in one (referencing) table that refers to a column or set of columns in another (referenced) table.

ENUM constraint
+
An ENUM is a string object with a value chosen from a list of permitted values. They are enumerated explicitly in the column specification at table creation time.

mysql> CREATE TABLE Shops(Id INTEGER, Name VARCHAR(55),

    -> Quality ENUM('High', 'Average', 'Low'));

The table has an Id, Name, and Quality columns defined. The Quality column is an ENUM. It permits to have one of three specified values: High, Average, or Low.

mysql> INSERT INTO Shops VALUES(1, 'Boneys', 'High');

mysql> INSERT INTO Shops VALUES(2, 'AC River', 'Average');

mysql> INSERT INTO Shops VALUES(3, 'AT 34', '**');

mysql> SELECT * FROM Shops;

+------+----------+---------+
| Id   | Name     | Quality |
+------+----------+---------+
|    1 | Boneys   | High    |
|    2 | AC River | Average |
|    3 | AT 34    |         |
+------+----------+---------+
