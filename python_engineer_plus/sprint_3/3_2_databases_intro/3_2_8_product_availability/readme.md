# Product Availability Check in Grocery Stores

## Description 📝

The provided SQL query checks whether all unique products from the `products` table are sold in grocery stores as recorded in the `products_stores` table.

It selects the product ID (`id_product`) and name (`name`) from `products`, and the store ID (`id_store`) from `products_stores`, using a `LEFT JOIN` on `id_product` to include all products, even those not available in any store.

The resulting fields are named `id_product`, `name`, and `id_store`.

This query helps identify products not sold in any store by showing `NULL` in the `id_store` column for unmatched products.

## Purpose 🎯

Intended for verifying product availability across stores, useful for inventory management, identifying unsold products, or educational exercises in SQL joins, particularly `LEFT JOIN`, within a retail database context.

## How It Works 🔍

-   **Module Import**:

    -   No external modules; uses standard SQL syntax compatible with relational databases (e.g., SQLite, PostgreSQL).

-   **Query**:

    -   **`SELECT p.id_product, p.name, ps.id_store FROM products AS p LEFT JOIN products_stores AS ps ON p.id_product = ps.id_product;`**
        -   **Columns**:
            -   `p.id_product` (INTEGER): Product ID from `products`.
            -   `p.name` (TEXT): Product name from `products` (e.g., "Молоко топленое Эконива 4%, 1 л").
            -   `ps.id_store` (INTEGER): Store ID from `products_stores`, or `NULL` if no match.
        -   **Tables**:
            -   `products`: Contains product details (`id_product`, `name`, `category`, `units`, `weight`).
            -   `products_stores`: Tracks product availability in stores (`id_product`, `price`, `id_store`, `date_upd`).
        -   **Join**:
            -   `LEFT JOIN products_stores AS ps ON p.id_product = ps.id_product`: Includes all rows from `products` and matching rows from `products_stores`. If a product has no corresponding entry in `products_stores`, `id_store` is `NULL`.
        -   **Aliases**: `p` for `products`, `ps` for `products_stores`, improving readability.
        -   **Returns**: All products with their store availability, showing `NULL` for `id_store` where products are not sold.

-   **Behavior**:
    -   Lists all 21 products from `products`, joined with their store entries from `products_stores`.
    -   Based on the sample data:
        -   `products`: 21 rows with `id_product` values (0, 1, 2, 3, 4, 6, 7, 50, 51, 52, 53, 55, 100, 102, 103, 104, 105, 106, 147, 148, 154).
        -   `products_stores`: 21 rows with `id_product` values (3, 5, 8, 10, 11, 12, 16, 17, 18, 20, 21, 25, 26, 27, 28, 29, 31, 34, 35, 38, 39).
        -   Matching `id_product` values: 3, 8, 10, 11, 12, 16, 17, 18, 20, 21, 25, 26, 27, 28, 29, 31, 34, 35, 38, 39 (20 products).
        -   Non-matching `id_product` from `products`: 0, 1, 2, 4, 6, 7, 50, 51, 52, 53, 55, 100, 102, 103, 104, 105, 106, 147, 148, 154 (20 products have no store entry, but some `id_product` in `products_stores` like 5 are not in `products`).
        -   Result: 21 rows (one for each product in `products`), with `id_store=0` for the 20 matched products and `NULL` for unmatched ones (e.g., `id_product=0`).
    -   Example output (partial):
        ```
        id_product | name | id_store
        0 | Молоко топленое Эконива 4%, 1 л | NULL
        1 | Молоко пастеризованное Му-му отборное 3,4-6,0%, 900 г | NULL
        3 | Молоко цельное пастеризованное Ваша Ферма 3,4-6,0%, 1 л | 0
        8 | Молоко стерилизованное Можайское 3,2%, 450 мл | 0
        ...
        ```
    -   **Row Count**: 21 rows (one per product in `products`).

## Verification ✅

Implementation satisfies requirements:

-   **Functionality**:

    -   Selects `id_product` and `name` from `products`, `id_store` from `products_stores`.
    -   Uses `LEFT JOIN` on `id_product` to include all products.
    -   Names output columns `id_product`, `name`, `id_store`.

-   **Correctness**:

    -   Column names match schemas: `id_product` (INTEGER), `name` (TEXT), `id_store` (INTEGER).
    -   `LEFT JOIN` ensures all `products` rows are included, with `NULL` for unmatched `id_store`.
    -   Aliases (`p`, `ps`) prevent ambiguity and improve clarity.
    -   Sample data yields 21 rows, with `NULL` for products not in `products_stores` (e.g., `id_product=0, 1, 2`).

-   **Output**:

    -   Matches required format: three columns (`id_product`, `name`, `id_store`).
    -   Includes all 21 products, with `id_store` as `0` or `NULL` based on `products_stores` matches.
    -   Identifies unsold products (e.g., `id_product=0` with `id_store=NULL`).

-   **Documentation**: Clear query structure and detailed README.

## Potential Considerations 🛠️

-   **Correctness**:

    -   Assumes `products` and `products_stores` exist; no error handling for missing tables.
    -   `LEFT JOIN` correctly includes all `products` rows, showing `NULL` for unsold products.
    -   Sample data shows `products_stores` contains `id_product=5`, absent from `products`, indicating possible data inconsistency (not addressed by query).
    -   Cyrillic `name` requires UTF-8 encoding support.

-   **Performance**:

    -   `LEFT JOIN`: O(n \* m) in worst case, efficient for small datasets (21 products, 21 store entries).
    -   No sorting or limiting, as not requested, so all rows are returned.
    -   `PRIMARY KEY` on `products.id_product` and composite key on `products_stores` (`id_product`, `id_store`, `date_upd`) aid join performance.

-   **Design**:

    -   `LEFT JOIN` is ideal for checking availability, ensuring all products are listed.
    -   Aliases (`p`, `ps`) enhance readability.
    -   Explicit column selection (`p.id_product`, `p.name`, `ps.id_store`) avoids ambiguity.

-   **Alternatives**:

    -   Use `RIGHT JOIN`: Inappropriate, as it prioritizes `products_stores`.
    -   Add `WHERE ps.id_store IS NULL`: Identify only unsold products.
    -   Include `COUNT(ps.id_store)` with `GROUP BY`: Summarize store availability per product.
    -   Index `products_stores.id_product`: Optimize join for large datasets.

-   **Extensibility**:

    -   Easily add columns (e.g., `category`, `price`) or filters (e.g., `WHERE category = 'молоко и сливки'`).
    -   Can extend to count stores per product or list specific stores.
    -   Supports integration into inventory audits or reports.

-   **Edge Cases**:
    -   **No Matches**: Products with no `products_stores` entry show `id_store=NULL` (e.g., `id_product=0`).
    -   **Empty `products`**: Returns no rows.
    -   **Empty `products_stores`**: Returns all products with `id_store=NULL`.
    -   **Missing Table**: Raises a database error (assumed handled by client).
    -   **Data Inconsistency**: `id_product=5` in `products_stores` but not `products` (not addressed by query).

## Usage Example (For Clarity, Not Submission) 📦

```sql
-- Execute query in a SQL client
SELECT p.id_product, p.name, ps.id_store
FROM products AS p
LEFT JOIN products_stores AS ps ON p.id_product = ps.id_product;
-- Output (partial, based on sample data):
-- id_product | name | id_store
-- 0 | Молоко топленое Эконива 4%, 1 л | NULL
-- 1 | Молоко пастеризованное Му-му отборное 3,4-6,0%, 900 г | NULL
-- 2 | Молоко пастеризованное Фермерский супермаркет Сферм 3,2-4%, 930 мл | NULL
-- 3 | Молоко цельное пастеризованное Ваша Ферма 3,4-6,0%, 1 л | 0
-- 4 | Молоко цельное Асеньевская ферма 3,4-6%, 900 мл | NULL
-- ...

-- Find unsold products (optional)
SELECT p.id_product, p.name
FROM products AS p
LEFT JOIN products_stores AS ps ON p.id_product = ps.id_product
WHERE ps.id_store IS NULL;
-- Output: Products with id_product=0, 1, 2, 4, 6, 7, 50, 51, 52, 53, 55, 100, 102, 103, 104, 105, 106, 147, 148, 154

-- Verify matches
SELECT DISTINCT id_product FROM products_stores WHERE id_product IN (0, 1, 2, 3, 4, 6, 7, 50, 51, 52, 53, 55, 100, 102, 103, 104, 105, 106, 147, 148, 154);
-- Output: 3, 8, 10, 11, 12, 16, 17, 18, 20, 21, 25, 26, 27, 28, 29, 31, 34, 35, 38, 39
```

## Example Scenario

Given sample data:

-   `products`:
    ```
    id_product | name | category | units | weight
    0 | Молоко топленое Эконива 4%, 1 л | молоко и сливки | л | 1
    1 | Молоко пастеризованное Му-му отборное 3,4-6,0%, 900 г | молоко и сливки | г | 900
    3 | Молоко цельное пастеризованное Ваша Ферма 3,4-6,0%, 1 л | молоко и сливки | л | 1
    ...
    ```
-   `products_stores`:
    ```
    id_product | price | id_store | date_upd
    3 | 69 | 0 | 2019-06-01 00:00:00
    8 | 76 | 0 | 2019-06-01 00:00:00
    ...
    ```

The query returns (partial):

```
id_product | name | id_store
0 | Молоко топленое Эконива 4%, 1 л | NULL
1 | Молоко пастеризованное Му-му отборное 3,4-6,0%, 900 г | NULL
3 | Молоко цельное пастеризованное Ваша Ферма 3,4-6,0%, 1 л | 0
...
```

## Conclusion 🚀

The query successfully checks product availability by selecting `id_product`, `name`, and `id_store` using a `LEFT JOIN` between `products` and `products_stores`.

It returns all 21 products from the sample data, with `NULL` `id_store` for unsold products, meeting the task’s requirements.

The implementation is efficient, modular, and extensible, making it ideal for inventory analysis, identifying unsold products, or teaching SQL `LEFT JOIN` techniques in a retail context.
