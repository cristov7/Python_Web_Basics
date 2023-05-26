-- Basic SQL Commands:



-- Create a Table using SQL:

CREATE TABLE example_table
(id SERIAL PRIMARY KEY,
email VARCHAR (30) NOT NULL,
first_name VARCHAR (30),
last_name VARCHAR (30));
-- example_table -> table name
-- id, email, first_name, last_name -> columns



-- Inserting Data Using SQL:


-- The SQL INSERT command - values for all columns:

INSERT INTO example_table VALUES (1, 'first_eamil@abv.bg', 'Asen' , 'Asenov');
-- example_table -> table name
-- (1, 'first_eamil@abv.bg', 'Asen' , 'Asenov') -> values


-- The SQL INSERT command - values for specific columns:

INSERT INTO example_table(email) VALUES ('some_random_eamil@abv.bg');
-- example_table -> table name
-- email -> column
-- ('some_random_eamil@abv.bg') -> value


-- Bulk data can be recorded in a single query, separated by comma:

INSERT INTO example_table VALUES
                              (100, 'email100@abv.bg', 'Lionel', 'Messi'),
                              (101, 'email101@abv.bg', 'Cristiano', 'Ronaldo'),
                              (102, 'email103@abv.bg', 'Kristian', 'Hristov');
-- example_table -> table name
-- (...), (...), (...); -> values



-- Retrieve/Read Records Using SQL:


-- Get all information from a table:

SELECT * FROM example_table;
-- * -> all
-- example_table -> table name


SELECT * FROM example_table ORDER BY id ASC;
-- * -> all
-- example_table -> table name
-- ORDER BY ASC / DESC -> ordered by ascending or descending order


-- You can limit the columns and number of records:

SELECT first_name, last_name FROM example_table LIMIT 3;
-- first_name, last_name -> List of columns
-- example_table -> table name
-- LIMIT -> Number of records


SELECT first_name, last_name FROM public.example_table ORDER BY id DESC LIMIT 3;
-- first_name, last_name -> List of columns
-- example_table -> table name
-- ORDER BY ASC / DESC -> ordered by ascending or descending order
-- LIMIT -> Number of records



-- Filtering the Selected Rows:


-- You can filter rows by specific conditions using the WHERE clause:

SELECT first_name, last_name FROM example_table WHERE id = 102;
-- first_name, last_name -> List of columns
-- example_table -> table name
-- WHERE -> condition


-- Logical and comparison operators can be used for better control:

SELECT first_name, last_name FROM example_table WHERE id > 1 AND id < 102;
-- first_name, last_name -> List of columns
-- example_table -> table name
-- WHERE -> condition



-- Updating Data:


--Note: If you left out the WHERE clause, all rows in the table would be updated

UPDATE example_table SET first_name = 'Alen' WHERE first_name = 'Kristian';
-- example_table -> table name
-- first_name -> column
-- WHERE -> condition


UPDATE example_table
SET email = '102@abv.bg', first_name = 'Wayne', last_name = 'Rooney'
WHERE id = 102;
-- example_table -> table name
-- email, first_name, last_name -> List of columns
-- WHERE -> condition



-- Altering Tables Using SQL:


-- Add new column:

ALTER TABLE example_table ADD COLUMN salary DECIMAL;
-- ALTER TABLE -> choose table
-- example_table -> table name
-- ADD COLUMN -> adding a new column
-- salary -> column
-- DECIMAL -> data type;


-- Delete existing column:

ALTER TABLE example_table DROP COLUMN salary;
-- ALTER TABLE -> choose table
-- example_table -> table name
-- DROP COLUMN -> deleting a column
-- salary -> column


-- Modify data type of existing column:

ALTER TABLE example_table ALTER COLUMN email TYPE VARCHAR(100);
-- ALTER TABLE -> choose table
-- example_table -> table name
-- ALTER COLUMN -> choose column
-- email -> column
-- TYPE -> type of column
-- VARCHAR(100) -> new data type



-- Dropping and Truncating:


-- To delete all the entries in a table - delete the data from table:

TRUNCATE TABLE example_table;
-- example_table -> table name


-- To drop a table - delete table:

DROP TABLE example_table;
-- example_table -> table name


-- To drop entire database - delete database:

DROP DATABASE soft_uni;
-- soft_uni -> database name


-- Delete from table - delete row from table:

DELETE FROM example_table WHERE id = 102;
-- example_table -> table name
