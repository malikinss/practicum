# Top 3 Stores with Smallest Number of Unique Products (>30)

## Description 📝

The provided SQL query aims to count the number of unique products for each store (`name_store`) in the `products_data_all` table, naming the count `name_uniq_cnt`. It seeks to identify the three stores with the smallest number of unique products, where the count exceeds 30, and display the store name and the number of unique products.

## Purpose 🎯

Intended to identify the three stores with the smallest number of unique products (more than 30) in `products_data_all`, displaying store names and unique product counts, useful for inventory analysis, store performance evaluation, or educational exercises in SQL aggregation, grouping, and limiting in a retail context.

## How It Works 🔍

-   **Module Import**:

    -   No external modules; uses standard SQL syntax compatible with relational databases (e.g., SQLite, PostgreSQL).

-   **Query Details**:

    -   **Columns**:
        -   `name_store` (VARCHAR(100)): Store name from `products_data_all`.
        -   `COUNT(DISTINCT id_product) AS name_uniq_cnt`: Counts unique `id_product` values per store, representing unique products.
    -   **Table**: `products_data_all`, containing product details (`id_product`, `name`, `category`, `units`, `weight`, `price`, `date_upd`, `id_store`, `name_store`).
    -   **Grouping**:
        -   `GROUP BY name_store`: Aggregates by store to count unique products per store.
    -   **Condition**:
        -   `HAVING name_uniq_cnt > 30`: Filters for stores with more than 30 unique products.
    -   **Sorting**:
        -   `ORDER BY name_uniq_cnt ASC`: Sorts stores by unique product count in ascending order to get the smallest counts first.
    -   **Limit**:
        -   `LIMIT 3`: Restricts output to the three stores with the smallest qualifying counts.
    -   **Returns**: Up to three rows with store names and their unique product counts, for stores with more than 30 unique products.

-   **Behavior**:
    -   Groups rows by `name_store`, counts unique `id_product` values, filters for counts above 30, and returns the three stores with the smallest counts.
    -   Based on the sample data:
        -   `products_data_all`: 20 rows, all with `name_store="Молочные вкусности"`.
        -   Unique `id_product` values: 20 distinct values (3, 5, 8, 10, 11, 12, 16, 17, 18, 20, 21, 25, 26, 27, 28, 29, 31, 34, 35, 38).
        -   For `Молочные вкусности`: `name_uniq_cnt = 20`.
        -   No stores have `name_uniq_cnt > 30`, as only one store exists with 20 unique products.
    -   Output:
        ```
        (empty result set)
        ```
    -   **Row Count**: 0 rows, as no stores meet the `name_uniq_cnt > 30` condition.

## Verification ✅

Implementation satisfies requirements:

-   **Functionality**:

    -   Selects `name_store` and unique product count (`name_uniq_cnt`).
    -   Groups by `name_store` to count unique products per store.
    -   Filters for stores with `name_uniq_cnt > 30`.
    -   Returns the three stores with the smallest qualifying counts.

-   **Correctness**:

    -   `COUNT(DISTINCT id_product)` accurately counts unique products.
    -   `GROUP BY name_store` correctly aggregates by store.
    -   `HAVING name_uniq_cnt > 30` filters post-aggregation.
    -   `ORDER BY name_uniq_cnt ASC` ensures the smallest counts are first.
    -   `LIMIT 3` restricts to three results.
    -   Sample data has one store (`Молочные вкусности`) with 20 unique products, below the 30 threshold, so empty result is correct.
    -   Cyrillic `name_store` requires UTF-8 encoding.

-   **Output**:

    -   Matches required format: two columns (`name_store`, `name_uniq_cnt`).
    -   Returns 0 rows, as expected with sample data.
    -   Column names and structure align with task requirements.

-   **Documentation**: Clear query structure and detailed README.

## Potential Considerations 🛠️

-   **Correctness**:

    -   Assumes `products_data_all` exists; no error handling for missing tables.
    -   Only one store (`Молочные вкусности`) in sample data, with 20 unique products, failing the `> 30` condition.
    -   `id_product` is assumed to uniquely identify products; `name` could be used if `id_product` isn’t unique, but sample data suggests `id_product` is appropriate.
    -   No `NULL` values in `id_product` or `name_store` in sample data, ensuring accurate counts.

-   **Performance**:

    -   `COUNT(DISTINCT id_product)` and `GROUP BY`: O(n) for n rows, efficient for small datasets (20 rows).
    -   `HAVING` and `ORDER BY`: Minimal impact with one store.
    -   Indexing on `name_store` or `id_product` could optimize for large datasets.
    -   `LIMIT 3` minimizes data transfer.

-   **Design**:

    -   Corrected query uses `COUNT(DISTINCT id_product)` and `GROUP BY name_store`.
    -   Clear variable naming (`name_uniq_cnt`) enhances readability.
    -   `ORDER BY name_uniq_cnt ASC` ensures smallest counts are prioritized.

-   **Alternatives**:

    -   Use `COUNT(DISTINCT name)`: If product names are guaranteed unique (true in sample data), but `id_product` is safer.
    -   Lower threshold: Adjust `HAVING name_uniq_cnt > 10` to return results with sample data.
    -   Add tie-breaker: `ORDER BY name_uniq_cnt ASC, name_store` for consistent ordering of equal counts.
    -   Include additional metrics: Add `COUNT(*)` to compare total vs. unique products.

-   **Extensibility**:

    -   Easily modify to include other filters (e.g., `WHERE date_upd = '2019-06-01'`).
    -   Can extend with additional columns (e.g., `category`) or metrics (e.g., `AVG(price)`).
    -   Supports integration into inventory reports or dashboards.

-   **Edge Cases**:
    -   **No Matching Rows**: Returns no rows (as with sample data).
    -   **Empty Table**: Returns no rows.
    -   **Missing Table**: Raises a database error (assumed handled by client).
    -   **Fewer Than 3 Stores**: Returns all qualifying stores (none here).
    -   **NULL Values**: `id_product` and `name_store` are non-`NULL` in sample data; `COUNT(DISTINCT)` handles `NULL` correctly.
    -   **Large Dataset**: Query remains efficient but may need indexing for scale.

## Usage Example (For Clarity, Not Submission) 📦

```sql
-- Execute corrected query
SELECT name_store, COUNT(DISTINCT id_product) AS name_uniq_cnt
FROM products_data_all
GROUP BY name_store
HAVING name_uniq_cnt > 30
ORDER BY name_uniq_cnt ASC
LIMIT 3;
-- Output (based on sample data):
-- (empty result set)

-- Verify data
SELECT name_store, COUNT(DISTINCT id_product) AS unique_products
FROM products_data_all
GROUP BY name_store;
-- Output:
-- name_store | unique_products
-- Молочные вкусности | 20

-- Hypothetical example with matching data
-- Assume data:
-- id_product | name | name_store | ...
-- 1 | Milk A | Store A | ... (and 40 unique products)
-- 2 | Milk B | Store B | ... (and 35 unique products)
-- 3 | Milk C | Store C | ... (and 32 unique products)
-- 4 | Milk D | Store D | ... (and 50 unique products)
SELECT name_store, COUNT(DISTINCT id_product) AS name_uniq_cnt
FROM products_data_all
GROUP BY name_store
HAVING name_uniq_cnt > 30
ORDER BY name_uniq_cnt ASC
LIMIT 3;
-- Output:
-- name_store | name_uniq_cnt
-- Store C | 32
-- Store B | 35
-- Store A | 40
```

## Example Scenario

Given `products_data_all` (partial):

```
id_product | name | category | units | weight | price | date_upd | id_store | name_store
3 | Молоко цельное пастеризованное Ваша Ферма 3,4-6,0%, 1 л | молоко и сливки | л | 1.000 | 69.00 | 2019-06-01 00:00:00 | 0 | Молочные вкусности
5 | Молоко пастеризованное Искренне Ваш отборное 3,4-6,0%, 900 мл | молоко и сливки | мл | NULL | 78.00 | 2019-06-01 00:00:00 | 0 | Молочные вкусности
...
```

Only one store (`Молочные вкусности`) exists with 20 unique products, below the 30 threshold, so the query returns:

```
(empty result set)
```

## Conclusion 🚀

The corrected query successfully aims to count unique products per store, naming the count `name_uniq_cnt`, and identify the three stores with the smallest counts above 30. With the sample data, it returns an empty result set, as the only store has 20 unique products, which is correct given the data constraints. The implementation is efficient, modular, and extensible, making it suitable for inventory analysis, store performance evaluation, or teaching SQL aggregation, grouping, and limiting techniques in a retail context.
