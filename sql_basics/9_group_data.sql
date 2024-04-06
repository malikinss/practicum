-- Count how many hot dogs were ordered with and without ketchup. 
-- Group the data by the 'ketchup' field of the 'hotdog' table and summarize the values in the 'quantity' field.
SELECT
    ketchup, 
    SUM(quantity)
FROM
    hotdog
GROUP BY
    ketchup;

-- Let's check how the data on hot dogs differs. 
-- Count the number of orders and the average number of ingredients for each type of hot dog. 
-- The required fields are 'name_hotdog' and 'ingredients'.
SELECT
    name_hotdog,
    COUNT(name_hotdog),
    AVG(ingredients)
FROM 
    hotdog
GROUP BY
    name_hotdog;

-- Display the average number of times mustard was poured on each type of hot dog containing five ingredients. 
-- Add a condition: select records for the second week of the year.
-- If mustard was added to the hot dog, the 'mustard' field contains the value 1.
SELECT
    name_hotdog,
    AVG(mustard)
FROM
    hotdog
WHERE   
    EXTRACT(WEEK FROM date) = 2 
    AND ingredients = 5
GROUP BY
    name_hotdog;

-- Display how many orders of vegetarian sausage were sold in the first five days of January. 
-- Display the January day number and the number of orders in the summary table.
-- If the sausage is vegetarian, the 'vegan_sausage' field takes the value 1.
SELECT
    EXTRACT(DAY FROM date) as order_day,
    COUNT(name_hotdog)
FROM 
    hotdog
WHERE 
    EXTRACT(MONTH FROM date) = 1
    AND EXTRACT(DAY FROM date) in (1,2,3,4,5)
    AND vegan_sausage = 1
GROUP BY
    order_day;

-- How much revenue did customers with bracelets 145900, 145783 and 145866 bring in by buying sausages with all three sauces added: mustard, ketchup and mayonnaise?
SELECT
    bracelet_id,
    SUM(price*quantity)
FROM
    hotdog
WHERE
    mustard = 1
    AND mayonnaise = 1
    AND ketchup = 1
    AND bracelet_id IN (145900, 145783, 145866)
GROUP BY 
    bracelet_id;