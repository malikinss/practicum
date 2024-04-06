-- Unload all information from the 'pizza' table.
SELECT 
    *
FROM 
    pizza;

-- One way to check a table for anomalies is to unload data from the middle of the table. 
-- Unload five lines from there, from 1067 to 1071.
SELECT 
    *
FROM 
    pizza
LIMIT 5 OFFSET 1066;

-- The marketing department also wants to look at the table. 
-- Unload the first ten lines. 
-- Limit yourself to the fields 'date', 'name', 'bracelet_id', 'price' and 'quantity'. 
-- In the final table, rename 'date', 'name', and 'bracelet_id' to 'order_date', 'pizza_name', and 'client_id', respectively, to make it easier for your colleagues to work with the data.
SELECT 
    date AS order_date, 
    name AS pizza_name,
    bracelet_id AS client_id,
    price,
    quantity
FROM 
    pizza
LIMIT 10;

-- You need to look at the most expensive pizzas. 
-- Select all orders where the cost of pizza is more than 40 points.
SELECT 
    *
FROM 
    pizza
WHERE 
    price > 40;

-- The sales department has a hypothesis that pizzas over 40 points were most actively ordered from February 1 to February 15, 2022. 
-- Complete the previous request and add a condition that will unload orders from February 1 to February 15. 
-- Limit yourself to the fields 'date', 'name', 'price'.
SELECT 
    date,
    name,
    price
FROM 
    pizza
WHERE 
    price > 40
    AND (date >= '2022-02-01'
    AND date <= '2022-02-15');

-- Display fields with pizza name, date, week number and pizza radius for orders of two categories. 
-- In the first category, the price of the pizza is less than 30 points, and the radius is greater than 37 cm. 
-- In the second, the radius of the pizza is greater than or equal to 35 cm, and the price is greater than 35 points.
SELECT 
    name,
    date,
    EXTRACT(WEEK FROM date),
    radius
FROM 
    pizza
WHERE 
    (price < 30 AND radius > 37)
    OR (radius >= 35 AND price > 35);

-- What about the number of pizzas in the order? 
-- Display the date, the first day of the month, the name of the pizza and the number of pizzas in the order. 
-- Select orders only for February and with the number of pizzas in the order not equal to 1.
SELECT 
    date,
    DATE_TRUNC('month', date),
    name,
    quantity
FROM 
    pizza
WHERE 
    EXTRACT(MONTH FROM date) = 2
    AND NOT quantity = 1;

-- Some clients are company employees. 
-- Their braceletes IDs are 145738, 145759, 145773, 145807, 145815, 145821, 145873, 145880. 
-- Display the names, prices, and quantities of pizzas in orders these workers made in March.
SELECT 
    name,
    price,
    quantity
FROM 
    pizza
WHERE 
    bracelet_id IN (145738, 145759, 145773, 145807, 145815, 145821, 145873, 145880)
    AND EXTRACT(MONTH FROM date) = 3;

-- Now determine which of these workers bought vegetarian pizzas throughout the entire period. 
-- Display the bracelet ID and pizza name.
SELECT 
    bracelet_id,
    name
FROM 
    pizza
WHERE 
    bracelet_id IN (145738, 145759, 145773, 145807, 145815, 145821, 145873, 145880)
    AND vegan_marker = 1;