/*
Write a query that finds the maximum weight of a product in the 'milk and cream' category.

Use the CAST AS construct to cast the values ​​to a floating-point number and name the variable max_weight.
*/

SELECT
    MAX(CAST(weight AS real)) AS max_weight
FROM
    products_data_all
WHERE
    category = 'молоко и сливки';