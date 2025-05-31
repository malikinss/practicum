/*
Check: are all unique products from `products` sold in grocery stores `products_stores`?
Write a query that selects:

- `id_product` from the table `products`
- `name` from the table `products`
- id_store from the table `products_stores`

Join the table `products_stores` to the table `products` using the `LEFT JOIN` method on the field `id_product`.

Name the fields of the resulting selection: `id_product`, `name`, `id_store`.
*/

SELECT
    p.id_product,
    p.name,
    ps.id_store
FROM
    products AS p
LEFT JOIN
    products_stores AS ps ON
    p.id_product = ps.id_product
;