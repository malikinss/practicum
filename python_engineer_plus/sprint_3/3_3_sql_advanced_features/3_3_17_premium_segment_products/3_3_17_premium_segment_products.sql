/*
The department manager wants to get lists of customers who prefer premium products. And a summary of how many transactions users make on average per week. Let's study the target audience!

Write a query that will select from the products_data_all table product identifiers (id_product) of the category 'milk and cream' over 120 rubles or the category 'butter and margarine' over 354 rubles.
*/

SELECT
    id_product
FROM
    products_data_all
WHERE
    category = 'молоко и сливки' AND CAST(price AS REAL) > 120
    OR
    category = 'масло сливочное и маргарин' AND CAST(price AS REAL) > 354;