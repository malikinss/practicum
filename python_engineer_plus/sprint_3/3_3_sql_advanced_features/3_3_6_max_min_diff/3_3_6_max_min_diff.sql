/*
Write a query that will calculate the difference between the maximum and minimum price of each product in the category 'butter and margarine' on June 10, 2019.

Name the variable max_min_diff.

Convert string date values ​​to date format.

Display the product name, the difference between the maximum and minimum prices.
*/

SELECT
    name,
    (MAX(CAST(price AS REAL)) - MIN(CAST(price AS REAL))) AS max_min_diff
FROM
    products_data_all
WHERE
    category = 'масло сливочное и маргарин' AND
    CAST(date_upd AS DATE) = '2019-06-10'
GROUP BY
    name;