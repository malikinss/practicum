-- Calculate the maximum and minimum radius of pizzas purchased on March 13, 2022.
SELECT
    MAX(radius),
    MIN(radius)
FROM
    pizza
WHERE 
    date = '2022-03-13';

-- Calculate the maximum and minimum pizza radius for each day in March. 
-- Display the date, maximum and minimum values in the table. 
-- Sort the numbers in descending order.
SELECT
    date,
    MAX(radius) as max_radius,
    MIN(radius) as min_radius
FROM 
    pizza
WHERE
    EXTRACT(MONTH FROM date) = 3
GROUP BY
    date
ORDER BY
    min_radius DESC,
    max_radius DESC;

-- Calculate the average cost of a pizza depending on whether it is vegetarian or not. 
-- Display the 'vegan_marker' field and the average price field on the screen.
SELECT
    vegan_marker,
    AVG(price)
FROM
    pizza
GROUP BY 
    vegan_marker;

-- Complete the previous request. 
-- Add grouping by month. 
-- Display in the summary table:
-- month as the first day of the month,
-- indicator whether the pizza is vegetarian or not,
-- average cost of pizza.
-- Sort the data in ascending order: by month and by whether the pizza is vegetarian.
SELECT
    DATE_TRUNC('month', date) AS month,
    vegan_marker,
    AVG(price)
FROM
    pizza
GROUP BY
    vegan_marker,
    month
ORDER BY
    month,
    vegan_marker;

-- Count how many unique customers ordered each pizza. 
-- Display the name of the pizza and the number of unique customers.
SELECT 
    name,
    COUNT(DISTINCT bracelet_id)
FROM
    pizza
GROUP BY
    name;

-- Let's look at the client's portrait.
-- Which three clients brought in the most revenue in the third week of the year? 
-- Display only the field with 'bracelet_id' on the screen. 
-- Sort clients in descending order of revenue.
SELECT 
    bracelet_id
FROM
    pizza
WHERE
    EXTRACT(WEEK FROM date) = 3
GROUP BY
    bracelet_id
ORDER BY
    SUM(price*quantity) DESC
LIMIT 3;

-- Now, in the 'buyer' table, find these clients and count how many of the most profitable clients are women and men.
-- Display the 'gender' field on the screen and the number of top revenue clients who belong to each gender.
-- The bracelet IDs of the most profitable clients are 145773, 145779, 145855.
SELECT
    gender,
    COUNT(bracelet_id)
FROM
    buyer
WHERE
    bracelet_id IN (145773, 145779, 145855)
GROUP BY 
    gender;

-- Now let’s study which first connection zones are popular among young people. 
-- Display the area of first connection, client gender and average age in the final table. 
-- Research only young people under 30 years of age. 
-- In the final table, leave only those clients whose average age is less than 23 years. 
-- Sort the table by zone of first connection in alphabetical order and by gender.
SELECT
    connection_area,
    gender,
    AVG(age) AS avg_age
FROM
    buyer
WHERE
    age < 30
GROUP BY
    connection_area,
    gender
HAVING 
    AVG(age) < 23
ORDER BY
    connection_area,
    gender;