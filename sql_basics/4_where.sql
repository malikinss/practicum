-- Unload all values from the 'buyer' table, filtering the client's age: it must be less than or equal to 30. 
-- The age is stored in the 'age' field.
SELECT 
    *
FROM 
    buyer
WHERE 
    age <= 30;

-- From the 'buyer' table, download several fields: 
-- 'first_name' with the name of the buyer, 
-- 'connection_area' with the zone of the first connection, 
-- and 'company_marker', which contains the value 1 if the client is an employee of the company, and 0 if not. 
-- Leave entries only for those customers who connected for the first time in the “Robotic Maze” zone.
SELECT 
    first_name,
    connection_area,
    company_marker
FROM 
    buyer
WHERE 
    connection_area = 'Robotic Maze';

-- Unload all fields from the 'buyer' table, but only for those buyers whose discount is not equal to 3.
SELECT 
    *
FROM 
    buyer
WHERE 
    percent_of_discount != 3;