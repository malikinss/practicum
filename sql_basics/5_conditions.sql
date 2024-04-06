-- Unload all values from the 'buyer' table, filtering customers:
-- by age - less than or equal to 30,
-- gender - male.
-- Age is stored in the 'age' field, and gender is stored in the 'gender' field.
SELECT 
    *
FROM 
    buyer
WHERE 
    (age <= 30) 
    AND (gender = 'male');

-- Unload all values from the 'buyer' table, filtering customers by the following conditions:
-- or the name 'Olga' is specified in the 'first_name' field,
-- or the 'percent_of_discount' field value is 20.
SELECT 
    *
FROM 
    buyer
WHERE 
    first_name = 'Olga'
    OR percent_of_discount = 20;

-- Unload the 'last_name', 'percent_of_discount' and 'company_marker' fields from the 'buyer' table. 
-- Set the following conditions:
-- or the discount percentage is 20,
-- or the client is an employee of the company.
-- If the client is an employee of the park, then 'company_marker' will be equal to 1.
SELECT 
    last_name,
    percent_of_discount,
    company_marker
FROM 
    buyer
WHERE 
    percent_of_discount = 20
    OR company_marker = 1;

-- Unload the 'last_name' and 'age' fields from the 'buyer' table. 
-- Keep the table for clients who are 25 years old, 32 years old or 38 years old. 
-- In addition, users between 40 and 45 years old should also be included in the sample.
SELECT 
    last_name,
    age
FROM 
    buyer
WHERE 
    age IN (25, 32, 38)
    OR (age >= 40 
        AND age <= 45 );

-- Unload the 'bracelet_id', 'last_name' and 'first_name' fields from the 'buyer' table. 
-- The following clients should be included in the sample:
-- from 30 to 48 years inclusive,
-- who connected for the first time not in the “Robotic Racing” and “Robo-City” zones,
-- which do not have a discount.
-- The age is indicated in the 'age' field, the area of the first connection is in the 'connection_area' field, and the discount is in the 'percent_of_discount' field.
SELECT 
    bracelet_id,
    last_name,
    first_name
FROM 
    buyer
WHERE 
    (age >= 30 AND age <= 48)
    AND (connection_area NOT IN ('Robotic Racing', 'Robo-City'))
    AND percent_of_discount = 0;

-- Unload the 'connection_area' and 'gender' fields from the 'buyer' table. 
-- Name them 'area' and 'gender_of_client' respectively. 
--Set the conditions - the sample should include:
-- all Andrei and Nikolai
-- under 38 years old,
-- whose surnames are not Ivanov or Kuznetsov.
-- In addition, the sample should include only those clients who connected for the first time in the “Robotic Maze” zone.
SELECT 
    connection_area AS area,
    gender AS gender_of_client
FROM 
    buyer
WHERE 
    (first_name IN ('Andrei', 'Nikolai')
    AND age < 38
    AND NOT last_name IN ('Ivanov', 'Kuznetsov'))
    AND connection_area = 'Robotic Maze';