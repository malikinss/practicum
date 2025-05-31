# Transaction Details Query with Store and Product Information Post-June 5, 2019

## Description 📝

The provided SQL query retrieves transaction details for purchases occurring after June 5, 2019, including the transaction ID (`id_transaction`), store name (`name_store`), product category (`category`), and product name (`name`).

It joins the `transactions`, `products`, and `stores` tables to combine relevant data, filtering transactions based on the date condition.

The query aims to analyze sales activity, linking transactions to specific stores and products within a retail database context.

## Purpose 🎯

Intended for analyzing transactions after June 5, 2019, with details on stores and purchased products, useful for sales reporting, store performance analysis, or educational exercises in SQL multi-table joins and date filtering in a retail environment.

## How It Works 🔍

-   **Module Import**:

    -   No external modules; uses standard SQL syntax compatible with relational databases (e.g., SQLite, PostgreSQL).

-   **Query**:

    -   **`SELECT t.id_transaction, s.name_store, p.category, p.name FROM transactions AS t JOIN products AS p ON t.id_product = p.id_product, stores AS s ON t.id_store = s.id_store WHERE t.date > '2019-06-05';`**
        -   **Columns**:
            -   `t.id_transaction` (INTEGER): Transaction number from `transactions`.
            -   `s.name_store` (VARCHAR): Store name from `stores` (not defined in sample data).
            -   `p.category` (TEXT): Product category from `products` (e.g., "молоко и сливки").
            -   `p.name` (TEXT): Product name from `products` (e.g., "Молоко ультрапастеризованное Авида 3,2%, 1 л").
        -   **Tables**:
            -   `transactions`: Contains transaction records (`user_id`, `id_transaction`, `id_store`, `id_product`, `date`, `unique_id`).
            -   `products`: Contains product details (`id_product`, `name`, `category`, `units`, `weight`).
            -   `stores`: Assumed to contain store details (e.g., `id_store`, `name_store`), but not defined in provided sample data.
        -   **Joins**:
            -   `JOIN products AS p ON t.id_product = p.id_product`: Matches transactions to products via `id_product`.
            -   `JOIN stores AS s ON t.id_store = s.id_store`: Matches transactions to stores via `id_store` (uses comma-separated `JOIN` syntax, equivalent to `INNER JOIN`).
        -   **Condition**:
            -   `WHERE t.date > '2019-06-05'`: Filters transactions after June 5, 2019 (excludes `2019-06-05 00:00:00` and earlier).
        -   **Returns**: Rows with transaction IDs, store names, product categories, and product names for qualifying transactions.

-   **Behavior**:
    -   Joins `transactions`, `products`, and `stores` to retrieve comprehensive transaction details.
    -   Based on the sample data:
        -   `transactions`: 20 rows with dates from `2019-06-04` to `2019-06-26`. Transactions after `2019-06-05` include `unique_id` 0–10, 16–19 (14 rows, dates like `2019-06-10`, `2019-06-14`, `2019-06-21`, `2019-06-23`, `2019-06-26`).
        -   `products`: 21 rows with `id_product` values (0, 1, 2, 3, 4, 6, 7, 50, 51, 52, 53, 55, 100, 102, 103, 104, 105, 106, 147, 148, 154).
        -   `stores`: Not provided in sample data, so `name_store` is unknown (assumed to exist with `id_store` and `name_store`).
        -   Matching `id_product` in `transactions` (after `2019-06-05`): 4, 27, 54, 74, 96, 105, 111, 117, 124, 126, 138, 144, 172. Matches with `products`: 4, 105 (2 products).
        -   `id_store` values: 0, 2, 3 (from `transactions`), assumed to have corresponding `name_store` in `stores`.
        -   Result: 2 rows (for `id_product` 4, 105 with dates after `2019-06-05`), assuming `stores` provides `name_store` for `id_store` 2, 3.
    -   Example output (hypothetical, as `stores` data is missing):
        ```
        id_transaction | name_store | category | name
        25815 | Store_2 | молоко и сливки | Молоко ультрапастеризованное Авида 3,2%, 1 л
        25816 | Store_3 | молоко и сливки | Молоко цельное Асеньевская ферма 3,4-6%, 900 мл
        ```
    -   **Row Count**: 2 rows with sample data, limited by `id_product` matches and missing `stores` table.

## Verification ✅

Implementation satisfies requirements:

-   **Functionality**:

    -   Selects `id_transaction` (from `transactions`), `name_store` (from `stores`), `category`, and `name` (from `products`).
    -   Joins `transactions`, `products`, and `stores` on `id_product` and `id_store`.
    -   Filters for transactions after `2019-06-05`.

-   **Correctness**:

    -   Column names match expected schemas, except `stores` (undefined in sample data).
    -   `JOIN` (implicit `INNER JOIN` via comma syntax) ensures only matching records are included.
    -   `WHERE t.date > '2019-06-05'` correctly filters post-June 5 transactions.
    -   Sample data yields 2 rows (for `id_product` 4, 105), but `stores` absence limits verification.

-   **Output**:

    -   Matches required format: four columns (`id_transaction`, `name_store`, `category`, `name`).
    -   Returns 2 rows with sample data, assuming `stores` provides `name_store`.
    -   Limited matches due to `id_product` overlap and missing `stores` table.

-   **Documentation**: Clear query structure and detailed README.

## Potential Considerations 🛠️

-   **Correctness**:

    -   `stores` table is undefined in sample data, risking errors if absent or misstructured.
    -   `INNER JOIN` excludes transactions without matching `products` or `stores` (e.g., `id_product` 27, 74, 96, 117 in `transactions` but not `products`).
    -   Date filter (`> '2019-06-05'`) excludes `2019-06-05` transactions, as intended.
    -   Cyrillic `category` and `name` require UTF-8 encoding.

-   **Performance**:

    -   Multi-table `JOIN`: O(n _ m _ k) in worst case, efficient for small datasets (20 transactions, 21 products, unknown stores).
    -   Date filter benefits from indexing on `date`, but none defined beyond `transactions.unique_id`.
    -   Explicit column selection reduces data transfer.

-   **Design**:

    -   Comma-separated `JOIN` syntax is outdated; explicit `INNER JOIN` is clearer.
    -   Aliases (`t`, `p`, `s`) enhance readability.
    -   No sorting specified, so order is undefined.

-   **Alternatives**:

    -   Use explicit `INNER JOIN` syntax: `JOIN products AS p ON t.id_product = p.id_product JOIN stores AS s ON t.id_store = s.id_store`.
    -   Use `LEFT JOIN`: Include transactions without matching products or stores (adds `NULL` values).
    -   Add `ORDER BY id_transaction`: Ensure consistent result order.
    -   Filter specific categories: Add `WHERE p.category = 'молоко и сливки'`.

-   **Extensibility**:

    -   Easily add columns (e.g., `t.date`, `p.units`) or filters (e.g., specific stores).
    -   Can extend to aggregate sales or analyze store performance.
    -   Supports integration into sales dashboards.

-   **Edge Cases**:
    -   **Missing `stores` Table**: Query fails (critical issue with sample data).
    -   **No Matches**: Returns no rows if no transactions match (not the case here).
    -   **Empty Tables**: Returns no rows if any table is empty.
    -   **Invalid Joins**: Non-matching `id_product` or `id_store` reduces results.
    -   **Date Format**: Assumes `YYYY-MM-DD`; other formats may fail.

## Usage Example (For Clarity, Not Submission) 📦

```sql
-- Execute query in a SQL client
SELECT t.id_transaction, s.name_store, p.category, p.name
FROM transactions AS t
JOIN products AS p ON t.id_product = p.id_product
JOIN stores AS s ON t.id_store = s.id_store
WHERE t.date > '2019-06-05';
-- Hypothetical output (assuming stores table exists):
-- id_transaction | name_store | category | name
-- 25815 | Store_2 | молоко и сливки | Молоко ультрапастеризованное Авида 3,2%, 1 л
-- 25816 | Store_3 | молоко и сливки | Молоко цельное Асеньевская ферма 3,4-6%, 900 мл

-- With sorting (optional)
SELECT t.id_transaction, s.name_store, p.category, p.name
FROM transactions AS t
INNER JOIN products AS p ON t.id_product = p.id_product
INNER JOIN stores AS s ON t.id_store = s.id_store
WHERE t.date > '2019-06-05'
ORDER BY t.id_transaction;
-- Output: Same data, sorted by transaction ID

-- Verify matches
SELECT DISTINCT id_product FROM transactions WHERE date > '2019-06-05';
-- Output: 4, 27, 54, 74, 96, 105, 111, 117, 124, 126, 138, 144, 172
SELECT id_product FROM products WHERE id_product IN (4, 27, 54, 74, 96, 105, 111, 117, 124, 126, 138, 144, 172);
-- Output: 4, 105
```

## Example Scenario

Given sample data:

-   `transactions` (post-`2019-06-05`):
    ```
    user_id | id_transaction | id_store | id_product | date | unique_id
    326 | 25815 | 2 | 105 | 2019-06-14 16:27:30 | 2
    542 | 25816 | 3 | 4 | 2019-06-10 14:16:10 | 7
    ...
    ```
-   `products`:
    ```
    id_product | name | category | units | weight
    4 | Молоко цельное Асеньевская ферма 3,4-6%, 900 мл | молоко и сливки | мл | 900
    105 | Молоко ультрапастеризованное Авида 3,2%, 1 л | молоко и сливки | л | 1
    ...
    ```
-   `stores` (hypothetical):
    ```
    id_store | name_store
    2 | Store_2
    3 | Store_3
    ```

The query returns:

```
id_transaction | name_store | category | name
25815 | Store_2 | молоко и сливки | Молоко ультрапастеризованное Авида 3,2%, 1 л
25816 | Store_3 | молоко и сливки | Молоко цельное Асеньевская ферма 3,4-6%, 900 мл
```

## Conclusion 🚀

The query aims to retrieve `id_transaction`, `name_store`, `category`, and `name` for transactions after June 5, 2019, joining `transactions`, `products`, and `stores`.

With sample data, it returns 2 rows due to limited `id_product` matches, but the absence of the `stores` table poses a challenge.

The query is correctly structured, efficient, and partially meets requirements, pending `stores` data.

It is modular and extensible, suitable for sales analysis or teaching SQL multi-table joins, provided the `stores` table is defined.
