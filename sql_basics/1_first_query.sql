-- Write a query that displays the phrase “Hello, world!” on the screen.
SELECT 
    'Hello, world!';

-- Using the query, calculate the difference between 27 and 19 and divide the result by 4.
SELECT 
    (27-19)/4;

-- Calculate what percentage 125 is of 25.
SELECT 
    125/25 * 100;

-- Unload all data from the pizza table
SELECT 
    * 
FROM 
    pizza;

-- Count the number of records in the pizza table
SELECT 
    COUNT(*)
FROM 
    pizza;