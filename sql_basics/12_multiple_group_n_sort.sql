-- Calculate the amount of revenue received from the sales of each hot dog for each month. 
-- Display the month number, the name of the hot dog, and the amount of revenue in the summary table.
SELECT 
    EXTRACT(MONTH fROM date) AS month,
    name_hotdog,
    SUM(price*quantity) AS total
FROM 
    hotdog
GROUP BY 
    month, 
    name_hotdog;

-- Complete the previous request. 
-- Sort the table by hot dog name in reverse alphabetical order, and then by month in ascending order.
SELECT 
    EXTRACT(MONTH fROM date) AS month,
    name_hotdog,
    SUM(price*quantity) AS total
FROM 
    hotdog
GROUP BY 
    month, 
    name_hotdog
ORDER BY 
    name_hotdog DESC,
    month ASC;