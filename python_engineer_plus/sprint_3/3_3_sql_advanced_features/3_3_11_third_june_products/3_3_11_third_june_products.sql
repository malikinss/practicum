/*
Write a query that will calculate the number of products weighing more than 900 g (weight) for each store (name_store) on '2019-06-03'.

Save the number of products in the variable name_cnt, and the date converted to the required type in update_date.

Display the date, store name, and the number of products only for those stores in which the number of products is less than 10.
*/

SELECT
    CAST(date_upd AS DATE) AS update_date,
    name_store,
    COUNT(name) AS name_cnt
FROM
    products_data_all
WHERE
    update_date = '2019-06-03'
    AND CAST(weight AS REAL) > 900
    AND units = 'г'
GROUP BY
    update_date,
    name_store
HAVING
    name_cnt < 10;