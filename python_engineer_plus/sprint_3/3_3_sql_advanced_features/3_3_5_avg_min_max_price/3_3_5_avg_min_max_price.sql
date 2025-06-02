/*
Write a query that will calculate the average, maximum, and minimum prices (price) of products for each store (name_store) in the products_data_all table.

Name the variables average_price, max_price, min_price, respectively.

Display the store name, average, maximum, and minimum prices.
*/

SELECT
    AVG(price) AS average_price,
    MAX(price) AS max_price,
    MIN(price) AS min_price
FROM
    products_data_all
GROUP BY
    name_store;