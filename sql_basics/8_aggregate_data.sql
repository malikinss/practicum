-- Find the minimum and maximum values in the 'ingredients' field of the 'hotdog' table.
SELECT 
    MIN(ingredients),
    MAX(ingredients)
FROM 
    hotdog;

-- Find the average price of a hot dog (the 'price' field) in the hotdog table for those orders where a vegetarian sausage was selected (the 'vegan_sausage' field). 
-- If the value of the 'vegan_sausage' field is 1, then the sausage was vegetarian. 
-- If 0 - meat.
SELECT 
    AVG(price)
FROM 
    hotdog
WHERE 
    vegan_sausage = 1;

-- Count how many times you ordered a 'Caribbean Flood' hot dog in February. 
-- You will need a 'date' field and a field with the name of the hot dog.
SELECT 
    COUNT(date)
FROM 
    hotdog
WHERE 
    EXTRACT(MONTH FROM date) = 2
    AND name_hotdog = 'Caribbean Flood';

-- Calculate how much on average a customer with a bracelet 145863 spent on hot dogs with ketchup and mayonnaise added at the same time or on hot dogs with sausage meat. 
-- If ketchup and mayonnaise are added, the 'mayonnaise' and 'ketchup' fields contain the value 1.
SELECT 
    AVG(quantity * price)
FROM 
    hotdog
WHERE 
    bracelet_id = 145863
    AND (vegan_sausage = 0
        OR (mayonnaise = 1 
            AND ketchup = 1)
        );

-- Let's calculate a real business metric - conversion rate, or CR. 
-- This is the proportion of unique users from the total users in the 'hotdog' table. 
-- Divide the number of unique users by the number of all users. 
-- Use the 'bracelet_id' field.
SELECT 
    COUNT(DISTINCT bracelet_id)::numeric / COUNT(bracelet_id)
FROM 
    hotdog;
