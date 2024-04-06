-- Compare sales of vegetarian hot dogs with different amounts of ingredients. 
-- Count the number of times you ordered hot dogs with veggie sausage and group the data by number of ingredients. 
-- In the final table, leave only those records where orders are less than or equal to 76.
SELECT 
    ingredients,
    COUNT(vegan_sausage)
FROM 
    hotdog
WHERE 
    vegan_sausage = 1
GROUP BY 
    ingredients
HAVING 
    COUNT(vegan_sausage) <= 76;

-- Complete the previous request. 
-- Leave only those orders where the sum of mustards is more than 30. 
-- You will need the 'mustard' field: if mustard was added, this field stores the value 1.
SELECT 
    ingredients,
    COUNT(ingredients)
FROM 
    hotdog
WHERE 
    vegan_sausage = 1
GROUP BY 
    ingredients 
HAVING 
    COUNT(ingredients) <=76 
    AND SUM(mustard) > 30;

-- Display a list of hot dog names that have had mayonnaise, mustard, or ketchup added to them at least once. 
-- The list should only include those hot dogs whose average sales revenue is greater than or equal to 30.5.
-- The required fields are 'name_hotdog', 'mustard', 'ketchup' and 'mayonnaise'. 
-- If sauce is added, the field value is 1.
SELECT 
    name_hotdog
FROM 
    hotdog
WHERE 
    1 IN (ketchup, mustard, mayonnaise)
GROUP BY 
    name_hotdog
HAVING 
    AVG(price * quantity) >= 30.5;