/*
Write a query that will count the number of unique products in each category in the store 'Lentro' on '2019-06-30'.

Name the variable uniq_name_cnt and sort the data in descending order by this field.

Convert the date to date format and name the field update_date.

Display the date, store name, category name, and number of unique products.
*/

SELECT
    CAST(date_upd AS DATE) AS update_date,
    name_store,
    category,
    COUNT(DISTINCT id_product) AS uniq_name_cnt
FROM
    products_data_all
WHERE
    name_store = 'Lentro' AND
    update_date = '2019-06-30'
GROUP BY
    update_date,
    name_store,
    category
ORDER BY
    uniq_name_cnt DESC;