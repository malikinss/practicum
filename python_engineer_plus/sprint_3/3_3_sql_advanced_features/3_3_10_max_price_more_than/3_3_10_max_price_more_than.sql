/*
Write a query that will find the maximum price for each product.

Save it in the max_price variable.

Display the products and the maximum price of those whose cost is more than 500 rubles.
*/

SELECT
    name,
    MAX(CAST(price AS REAL)) AS max_price
FROM
    products_data_all
GROUP BY
    name
HAVING
    max_price > 500;