-- Sort the 'hotdog' table by the 'bracelet_id' field in ascending order. 
-- Leave only the first five rows in the table.
SELECT 
    *
FROM 
    hotdog
ORDER BY 
    bracelet_id
LIMIT 5;

-- Find the most expensive hot dog. 
-- Display the name of the hot dog and its price. 
-- Use the 'name_hotdog' and 'price' fields.
SELECT 
    name_hotdog,
    price
FROM 
    hotdog
ORDER BY 
    price DESC
LIMIT 1;

-- Select three areas of the first connection from the buyer table, where the average discount was the highest.
SELECT 
    connection_area,
    AVG(percent_of_discount) as avg_discount
FROM 
    buyer
GROUP BY 
    connection_area
ORDER BY 
    avg_discount DESC
LIMIT 3;