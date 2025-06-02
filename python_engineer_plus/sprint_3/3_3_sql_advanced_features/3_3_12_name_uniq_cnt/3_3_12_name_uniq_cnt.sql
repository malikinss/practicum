/*
Write a query that will count the number of unique products for each store (name_store).

Name the variable name_uniq_cnt.

Find three stores that have the smallest number of unique products, but more than thirty.

Print the name of each store and the number of unique products in it.
*/

SELECT
    name_store,
    COUNT(DISTINCT name) AS name_uniq_cnt
FROM
    products_data_all
GROUP BY
    name
HAVING
    name_uniq_cnt > 30
ORDER BY
    name_uniq_cnt
LIMIT 3;