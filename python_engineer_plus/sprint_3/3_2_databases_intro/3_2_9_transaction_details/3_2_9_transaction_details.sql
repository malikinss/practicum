/*
For a period later than `June 5, 2019`, output the transaction ID; the name of the store where it occurred; the category and name of the product purchased.

Select:
    - `id_transaction` from the `transactions` table
    - `name_store` from the `stores` table
    - `category` from the `products` table
    - `name` from the `products` table
*/

SELECT
    t.id_transaction,
    s.name_store,
    p.category,
    p.name
FROM
    transactions AS t
JOIN
    products AS p ON
    t.id_product = p.id_product,
    stores AS s ON
    t.id_store = s.id_store
WHERE
    t.date > '2019-06-05'
;