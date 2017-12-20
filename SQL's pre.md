# SQL
## SQL RDBMS
*A Brief Overview of Common Relational Database Management Systems*
### BACKGROUND
**RELATIONAL DATABASE MANAGEMENT SYSTEMS (RDBMS)**
A relational database management system (RDBMS) is a program that lets you create, update, and administer a relational database. Most relational database management systems use SQL to access the database.
There are more similarities than differences between the different RDBMS, but the SQL syntax may be slightly different depending on which RDBMS you are using.
Here is a brief description of popular types of RDBMS
### SQLite
SQLite is a popular open source SQL database. It is able to store an entire database in a single file. One of the biggest advantages this provides is that all of the data can be stored locally without having to connect your database to a server.
SQLite is a popular choice for databases in cellphones, PDAs, MP3 players, set-top boxes, and other electronic gadgets. The SQL course on Codecademy also uses SQLite.
### MySQL
MySQL is the most popular open source SQL database. It is typically used for web application development, and often accessed using PHP.
The main advantages of MySQL are that it is easy to use, inexpensive, reliable (has been around since 1995) and has a large community of developers who can help answer questions.
Some of the disadvantages are that it has been known to suffer from poor performance when scaling, open source development has lagged since Oracle has taken control of MySQL, and it does not include some advanced features that developers may be used to.
### PostgreSQL
PostgreSQL is an open source SQL database that is not controlled by any corporation. It is typically used for web application development.
PostgreSQL shares many of the same advantages of MySQL. It is easy to use, inexpensive, reliable, and has a large community of developers. It also provides some additional features such as foreign key support without requiring complex configuration.
The main disadvantage of PostgreSQL is that it is slower in performance than other databases such as MySQL. It is also less popular than MySQL which makes it harder to come by hosts or service providers that offer managed PostgreSQL instances.
### Oracle DB
Oracle DB is owned by the Oracle corporation and the code is not open sourced.
Oracle is used for large applications, particularly in the banking industry. Most of the world’s top banks run Oracle applications because Oracle offers a powerful combination of technology and comprehensive, pre-integrated business applications, including key functionality built specifically for banks.
The main disadvantage of using Oracle is that it is not free to use like its open source competitors and can be quite expensive.
### SQL Server
SQL Server is owned by Microsoft. Like Oracle DB, the code is also close sourced.
SQL Server is mainly used by large enterprise applications. The major difference between Oracle and SQL Server is that SQL Server only supports the Windows Operating System.
Microsoft offers a free entry level version called Express, but can become very expensive as you scale your application.

## List of SQL commands
*Glossary of commonly used SQL commands*
### BACKGROUND
SQL, 'Structured Query Language', is a programming language designed to manage data stored in relational databases. SQL operates through simple, declarative statements. This keeps data accurate and secure, and helps maintain the integrity of databases, regardless of size.
Here's an appendix of commonly used commands.

### COMMANDS
* **ALTER TABLE**
`ALTER TABLE table_name ADD column datatype;`
ALTER TABLE lets you add columns to a table in a database.
* **AND**
```
SELECT column_name(s)
FROM table_name
WHERE column_1 = value_1
AND column_2 = value_2;
```
AND is an operator that combines two conditions. Both conditions must be true for the row to be included in the result set.
* **AS**
```
SELECT column_name AS 'Alias'
FROM table_name;
```
AS is a keyword in SQL that allows you to rename a column or table using an alias.
* **AVG**
```
SELECT AVG(column_name)
FROM table_name;
```
AVG() is an aggregate function that returns the average value for a numeric column.
* **BETWEEN**
```
SELECT column_name(s)
FROM table_name
WHERE column_name BETWEEN value_1 AND value_2;
```
The BETWEEN operator is used to filter the result set within a certain range. The values can be numbers, text or dates.
* **COUNT**
```
SELECT COUNT(column_name)
FROM table_name;
```
COUNT() is a function that takes the name of a column as an argument and counts the number of rows where the column is not NULL.
* **CREATE TABLE**
```
CREATE TABLE table_name (column_1 datatype, column_2 datatype, column_3 datatype);
```
CREATE TABLE creates a new table in the database. It allows you to specify the name of the table and the name of each column in the table.
* **DELETE**
`DELETE FROM table_name WHERE some_column = some_value;`
DELETE statements are used to remove rows from a table.
* **GROUP BY**
```
SELECT COUNT(*)
FROM table_name
GROUP BY column_name;
```
GROUP BY is a clause in SQL that is only used with aggregate functions. It is used in collaboration with the SELECT statement to arrange identical data into groups.
* **INNER JOIN**
```
SELECT column_name(s) FROM table_1
JOIN table_2
ON table_1.column_name = table_2.column_name;
```
An inner join will combine rows from different tables if the join condition is true.
* **INSERT**
```
INSERT INTO table_name (column_1, column_2, column_3) VALUES (value_1, 'value_2', value_3);
```
INSERT statements are used to add a new row to a table.
* **LIKE**
```
SELECT column_name(s)
FROM table_name
WHERE column_name LIKE pattern;
```
LIKE is a special operator used with the WHERE clause to search for a specific pattern in a column.
* **LIMIT**
```
SELECT column_name(s)
FROM table_name
LIMIT number;
```
LIMIT is a clause that lets you specify the maximum number of rows the result set will have.
* **MAX**
```
SELECT MAX(column_name)
FROM table_name;
```
MAX() is a function that takes the name of a column as an argument and returns the largest value in that column.
* **MIN**
```
SELECT MIN(column_name)
FROM table_name;
```
MIN() is a function that takes the name of a column as an argument and returns the smallest value in that column.
* **OR**
```
SELECT column_name
FROM table_name
WHERE column_name = value_1
OR column_name = value_2;
```
OR is an operator that filters the result set to only include rows where either condition is true.
* **ORDER BY**
```
SELECT column_name
FROM table_name
ORDER BY column_name ASC|DESC;
```
ORDER BY is a clause that indicates you want to sort the result set by a particular column either alphabetically or numerically.
* **OUTER JOIN**
```
SELECT column_name(s) FROM table_1
LEFT JOIN table_2
ON table_1.column_name = table_2.column_name;
```
An outer join will combine rows from different tables even if the the join condition is not met. Every row in the left table is returned in the result set, and if the join condition is not met, then NULL values are used to fill in the columns from the right table.
* **ROUND**
```
SELECT ROUND(column_name, integer)
FROM table_name;
```
ROUND() is a function that takes a column name and an integer as an argument. It rounds the values in the column to the number of decimal places specified by the integer.
* **SELECT**
`SELECT column_name FROM table_name;`
SELECT statements are used to fetch data from a database. Every query will begin with SELECT.
* **SELECT DISTINCT**
`SELECT DISTINCT column_name FROM table_name;`
SELECT DISTINCT specifies that the statement is going to be a query that returns unique values in the specified column(s).
* **SUM**
```
SELECT SUM(column_name)
FROM table_name;
```
SUM() is a function that takes the name of a column as an argument and returns the sum of all the values in that column.
* **UPDATE**
```
UPDATE table_name
SET some_column = some_value
WHERE some_column = some_value;
```
UPDATE statments allow you to edit rows in a table.
* **WHERE**
```
SELECT column_name(s)
FROM table_name
WHERE column_name operator value;
```
WHERE is a clause that indicates you want to filter the result set to include only rows where the following condition is true.
## Begin Lesson
1. **Introduction**
SQL, 'Structured Query Language', is a programming language designed to manage data stored in relational databases. SQL operates through simple, declarative statements. This keeps data accurate and secure, and helps maintain the integrity of databases, regardless of size.
The SQL language is widely used today across web frameworks and database applications. Knowing SQL gives you the freedom to explore your data, and the power to make better decisions. By learning SQL, you will also learn concepts that apply to nearly every data storage system.
The statements covered in this course, use SQLite Relational Database Management System (RDBMS). You can learn more about RDBMS's SQL RDBMS at above. You can also access a glossary of all the SQL commands taught in this course  at above.
Let's begin by entering a SQL command. In the code editor type
`SELECT * FROM celebs;`
You will run all of your SQL commands in this course by pressing the Run button at the bottom of the code editor.
Query Results
```
id	         name	             age
1	         Justin Bieber           22
2	         Beyonce Knowles	   33
3	         Jeremy Lin	             26
4	         Taylor Swift	   26

Database Schema

          celebs4                    rows
id                         INTEGER
name	                 TEXT
age	                 INTEGER
```






