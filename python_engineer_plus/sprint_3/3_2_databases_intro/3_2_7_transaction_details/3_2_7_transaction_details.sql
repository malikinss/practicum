/*
Write a query that will output:

- transaction number — `id_transaction` from the `transactions` table
- category name — `category` from the `products` table
- product name — `name` from the `products` table

Joining condition — equality of values ​​in the `products.id_product` and `transactions.id_product` fields.
Result table field names: `id_transaction`, `category`, `name`.

Output `10` rows. Sort the data in ascending order of transaction number.
*/

SELECT
    id_transaction, category, name
FROM
    transactions
INNER JOIN
    products ON
    transactions.id_product = products.id_product
ORDER BY
    id_transaction
LIMIT 10;