/*
Display products of the category 'milk and cream' and prices in stores for a certain day.

Write a query to the table and select the following fields:

- Product name (`name`)
- Price (`price`)
- Store name (`name*store`)
- Date (`date_upd`)

Make a selection by category (`category`) and date (`date_upd`). You need the category 'milk and cream' and World Milk Day: `'2019-06-01'`.
*/

SELECT 
    name, price, name_store, date_upd
FROM
    products_data_all
WHERE
    category = 'молоко и сливки' AND date_upd = '2019-06-01';
