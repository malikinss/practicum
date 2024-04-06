-- Calculate the average bill according to the 'pizza' table. 
-- In the final table, display the minimum, maximum and average revenue values. 
-- This will help you see how the average check differs from the maximum and minimum.
SELECT
    MIN(price*quantity),
    MAX(price*quantity),
    AVG(price*quantity)
FROM
    pizza;

-- Calculate the average bill for each type of pizza. 
-- Display the name of the pizza and the average bill. 
-- Sort the table by average bill in descending order.
SELECT
    name,
    AVG(price*quantity) AS avg_bill
FROM
    pizza
GROUP BY
    name
ORDER BY
    avg_bill DESC;

-- Calculate the average bill for vegetarian and non-vegetarian pizzas. 
-- Display an indicator on the screen whether the pizza is vegetarian and the average bill. 
-- Add a condition: managers asked not to take into account pizzas with a cheese side.
SELECT
    vegan_marker,
    AVG(price*quantity) AS avg_bill
FROM
    pizza    
WHERE
    cheese_side = 0
GROUP BY
    vegan_marker
ORDER BY
    avg_bill DESC;

-- Display the name of the pizza, the presence of a cheese side and the average bill. 
-- Sort the table first by name in alphabetical order, and then by the presence of cheese rim in ascending order.
SELECT
    name,
    cheese_side,
    AVG(price*quantity) AS avg_bill
FROM
    pizza    
GROUP BY
    name,
    cheese_side
ORDER BY
    name,
    cheese_side;

-- Now let’s calculate the conversion of park visitors to pizza orders. 
-- Let's remember that conversion is the ratio of the number of unique visitors who ordered pizza to the total number of unique visitors. 
-- The marketing department reports that the park received 1,000 visitors in three months.
SELECT
    COUNT(DISTINCT bracelet_id)::numeric / 1000 AS cr
FROM
    pizza;

-- Calculate conversion by month. 
-- Display the first day of the month and the conversion in the summary table. 
-- Sort the table by month in ascending order. 
-- Don't count park employees: their wristband numbers are 145738, 145759, 145773, 145807, 145815, 145821, 145873, 145880.
SELECT
    DATE_TRUNC('month', date) AS month_n,
    COUNT(DISTINCT bracelet_id)::numeric / 1000 AS cr
FROM
    pizza
WHERE 
    bracelet_id NOT IN (145738, 145759, 145773, 145807, 145815, 145821, 145873, 145880)
GROUP BY
    month_n
ORDER BY
    month_n;

-- Or maybe the conversion is related to the size of the pizza? Let's check!
-- Display the name and radius of the pizza. 
-- Calculate conversion. 
-- Don't count company employees. 
-- Leave only those lines where the conversion is above 3% - this is the target indicator for park managers.
SELECT
   name,
   radius,
   COUNT(DISTINCT bracelet_id)::numeric / 1000
FROM
    pizza
WHERE 
    bracelet_id NOT IN (145738, 145759, 145773, 145807, 145815, 145821, 145873, 145880)
GROUP BY
    name,
    radius
HAVING 
    COUNT(DISTINCT bracelet_id)::numeric / 1000 > 0.03;
