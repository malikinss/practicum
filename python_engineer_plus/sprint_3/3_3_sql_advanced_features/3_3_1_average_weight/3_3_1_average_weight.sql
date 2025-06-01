/*
Write a query that finds the average weight (`weight`) of products from the `products_data_all` table in grams (where `units='g'`).

Name the variable average.

Change the data type of the `weight` column to a floating-point number.
*/

SELECT
    AVG(CAST(weight AS real)) AS average
FROM
    products_data_all
WHERE
    units = 'г';