-- Unload the gender and age fields from the buyer table. 
-- Set the limit to the first seven lines.
SELECT 
    gender,
    age
FROM 
    buyer
LIMIT 7;

-- Unload the last_name, gender, age, connection_area and percent_of_discount fields from the buyer table. 
-- Rename the connection_area field in the final table to area, and percent_of_discount to discount. 
-- Unload lines 10 to 16 inclusive.
SELECT 
    last_name,
    gender,
    age,
    connection_area AS area,
    percent_of_discount AS discount
FROM 
    buyer
LIMIT 7 
OFFSET 9;

-- Unload all fields from the buyer table. 
-- Display all entries starting from 170 inclusive.
SELECT 
    *
FROM 
    buyer
OFFSET 169;