-- We previously noted that conversion rates fell slightly in March. 
-- Calculate DAU for March: the number of unique buyers this month.
-- Display the date and number of unique buyers. 
-- Sort the table by date in ascending order.
SELECT
    date,
    COUNT(DISTINCT bracelet_id) AS unique_clients
FROM
    pizza
WHERE
    EXTRACT(MONTH FROM date) = 3
GROUP BY
    date
ORDER BY
    date;

-- Now let's look at the dynamics by week. 
-- Calculate WAU: number of unique buyers by week.
-- Display the week number and WAU in the table. 
-- Sort the table by week number in ascending order.
SELECT
    EXTRACT(WEEK FROM date) AS week_n,
    COUNT(DISTINCT bracelet_id) AS unique_clients
FROM
    pizza
GROUP BY
    week_n
ORDER BY
    week_n;

-- Let's see if the slight dip in conversions in March is related to the number of unique buyers. 
-- Calculate MAU: the number of unique buyers for January, February and March.
-- Display the month in the table as the first date and MAU. 
-- Sort the table by month in ascending order.
SELECT
    DATE_TRUNC('month', date) AS month_n,
    COUNT(DISTINCT bracelet_id) AS unique_clients
FROM
    pizza
GROUP BY
    month_n   
ORDER BY
    month_n;

-- Now let's calculate ARPPU for January by day. 
-- Display the day number and metric value. 
-- To calculate ARPPU, divide total revenue by the number of unique customers.
SELECT
    EXTRACT(DAY FROM date) AS day_n,
    SUM(price*quantity) / COUNT(DISTINCT bracelet_id)
FROM
    pizza
WHERE
    EXTRACT(MONTH FROM date) = 1
GROUP BY
    date   
ORDER BY
    date;