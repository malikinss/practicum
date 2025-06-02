/*
Write a query that will calculate the total number of unique products in each store (name_store), information about which is in the products_data_all table.

Name the variables name_cnt, name_uniq_cnt respectively.

Display the store name, total number of products, number of unique products.
*/

SELECT
    name_store,
    COUNT(*) AS name_cnt,
    COUNT(DISTINCT id_product) AS name_uniq_cnt
FROM
    products_data_all
GROUP BY
    name_store
ORDER BY
    name_store;