/*
Write a query that will count the number of products in each category on the date '2019-06-05'.

Name the variable name_cnt and sort the data by increasing number of products.

Name the selected date update_date.

Output the date (update_date), category (category), number of products (name_cnt).

Note that the date must be converted from a string type to date.
*/

SELECT
    CAST(date_upd AS DATE) AS update_date,
    category,
    COUNT(*) AS name_cnt
FROM
    products_data_all
WHERE
    CAST(date_upd AS DATE) = DATE '2019-06-05'
GROUP BY
    category,
    update_date
ORDER BY
    name_cnt ASC;