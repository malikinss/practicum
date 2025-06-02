/*
Write a query that will calculate the maximum weight value in each category.

Name the variable max_weight.

Print the category and the maximum weight.
*/

SELECT
    category,
    MAX(CAST(weight AS real)) AS max_weight
FROM
    products_data_all
GROUP BY
    category
ORDER BY
    category;