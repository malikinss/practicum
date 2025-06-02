/*
Write a query that will return the top 5 most expensive products, sorted in descending order.

Return the product name and price.

Name the variable max_price.
*/

SELECT
    name,
    MAX(CAST(price AS REAL)) AS max_price
FROM
    products_data_all
GROUP BY
    name
LIMIT 5;