# Total and Unique Product Count per Store

## Description 📝

The provided SQL query calculates the total number of product entries and the number of unique products for each store (`name_store`) in the `products_data_all` table.

It selects the store name, counts all rows per store (`name_cnt`), and counts distinct `id_product` values per store (`name_uniq_cnt`).

The results are grouped by store and sorted alphabetically by store name.

This query enables analysis of product inventory distribution across stores in a retail database context.

## Purpose 🎯

Intended for summarizing product inventory by store, showing both total and unique product counts, useful for retail inventory management, store performance analysis, or educational exercises in SQL aggregation, grouping, and sorting.

## How It Works 🔍

-   **Module Import**:

    -   No external modules; uses standard SQL syntax compatible with relational databases (e.g., SQLite, PostgreSQL).

-   **Query**:

    -   **`SELECT name_store, COUNT(*) AS name_cnt, COUNT(DISTINCT id_product) AS name_uniq_cnt FROM products_data_all GROUP BY name_store ORDER BY name_store;`**
        -   **Columns**:
            -   `name_store` (VARCHAR(100)): Store name from `products_data_all`.
            -   `COUNT(*) AS name_cnt`: Total number of product entries per store.
            -   `COUNT(DISTINCT id_product) AS name_uniq_cnt`: Number of unique products (distinct `id_product`) per store.
        -   **Table**: `products_data_all`, containing product and store details (`id_product`, `name`, `category`, `units`, `weight`, `price`, `date_upd`, `id_store`, `name_store`).
        -   **Grouping**:
            -   `GROUP BY name_store`: Aggregates results by store, computing counts for each unique `name_store`.
        -   **Sorting**:
            -   `ORDER BY name_store`: Sorts results alphabetically by store name (ascending).
        -   **Returns**: One row per unique store, with store name, total product count, and unique product count.

-   **Behavior**:
    -   Groups all rows in `products_data_all` by `name_store`, counting total entries and unique `id_product` values.
    -   Based on the sample data:
        -   `products_data_all`: 20 rows, all with `name_store="Молочные вкусности"`.
        -   `id_product` values: 3, 5, 8, 10, 11, 12, 16, 17, 18, 20, 21, 25, 26, 27, 28, 29, 31, 34, 35, 38 (20 unique values).
        -   Total rows: 20 (`name_cnt=20`).
        -   Unique `id_product`: 20 (`name_uniq_cnt=20`).
    -   Output:
        ```
        name_store | name_cnt | name_uniq_cnt
        Молочные вкусности | 20 | 20
        ```
    -   **Row Count**: 1 row (only one store in sample data).

## Verification ✅

Implementation satisfies requirements:

-   **Functionality**:

    -   Selects `name_store`, total product count (`name_cnt`), and unique product count (`name_uniq_cnt`).
    -   Groups results by `name_store`.
    -   Sorts by `name_store` in ascending order.

-   **Correctness**:

    -   `COUNT(*)` accurately counts all rows per store.
    -   `COUNT(DISTINCT id_product)` correctly counts unique `id_product` values.
    -   `GROUP BY name_store` ensures aggregation by store.
    -   `ORDER BY name_store` sorts alphabetically.
    -   Sample data yields one row for "Молочные вкусности" with `name_cnt=20`, `name_uniq_cnt=20`.

-   **Output**:

    -   Matches required format: three columns (`name_store`, `name_cnt`, `name_uniq_cnt`).
    -   Returns 1 row for sample data, reflecting the single store.
    -   Column names and values align with task requirements.

-   **Documentation**: Clear query structure and detailed README.

## Potential Considerations 🛠️

-   **Correctness**:

    -   Assumes `products_data_all` exists; no error handling for missing tables.
    -   `name_store` uses Cyrillic ("Молочные вкусности"), requiring UTF-8 encoding.
    -   All rows in sample data have the same `name_store`, limiting output to one row.
    -   No `NULL` values in `id_product` or `name_store` in sample data, ensuring accurate counts.

-   **Performance**:

    -   `GROUP BY` and `COUNT`: O(n) for n rows, efficient for small datasets (20 rows).
    -   `COUNT(DISTINCT id_product)` may be slower for large datasets but is negligible here.
    -   Sorting (`ORDER BY`): O(n log n), minimal impact with 1 row.
    -   Indexing on `name_store` or `id_product` could optimize large-scale queries.

-   **Design**:

    -   Focused query meets task requirements.
    -   Clear variable names (`name_cnt`, `name_uniq_cnt`) enhance readability.
    -   Alphabetical sorting ensures consistent output.

-   **Alternatives**:

    -   Add `HAVING name_cnt > 0`: Filter stores with products (unnecessary here).
    -   Use `id_store` instead of `name_store`: If store IDs are preferred.
    -   Include additional metrics: Add `AVG(price)` or `SUM(weight)` per store.
    -   Sort by `name_cnt` or `name_uniq_cnt`: Highlight stores with most products.

-   **Extensibility**:

    -   Easily modify to include other columns (e.g., `category`, `units`) or filters (e.g., `WHERE date_upd = '2019-06-01'`).
    -   Can extend with subqueries to compare unique products across dates.
    -   Supports integration into inventory dashboards or reports.

-   **Edge Cases**:
    -   **Empty Table**: Returns no rows.
    -   **No Matching Rows**: Returns no rows (not applicable with sample data).
    -   **Missing Table**: Raises a database error (assumed handled by client).
    -   **NULL `name_store`**: Would create a separate group (none in sample data).
    -   **Large Dataset**: Query remains efficient but may need indexing for scale.

## Usage Example (For Clarity, Not Submission) 📦

```sql
-- Execute query in a SQL client
SELECT name_store, COUNT(*) AS name_cnt, COUNT(DISTINCT id_product) AS name_uniq_cnt
FROM products_data_all
GROUP BY name_store
ORDER BY name_store;
-- Output (based on sample data):
-- name_store | name_cnt | name_uniq_cnt
-- Молочные вкусности | 20 | 20

-- Verify data
SELECT name_store, id_product
FROM products_data_all
ORDER BY name_store, id_product;
-- Output: 20 rows, all with name_store="Молочные вкусности", 20 distinct id_product

-- With additional sorting (optional)
SELECT name_store, COUNT(*) AS name_cnt, COUNT(DISTINCT id_product) AS name_uniq_cnt
FROM products_data_all
GROUP BY name_store
ORDER BY name_cnt DESC;
-- Output: Same data, sorted by total count
```

## Example Scenario

Given `products_data_all` (partial):

```
id_product | name | category | units | weight | price | date_upd | id_store | name_store
3 | Молоко цельное пастеризованное Ваша Ферма 3,4-6,0%, 1 л | молоко и сливки | л | 1.000 | 69.00 | 2019-06-01 00:00:00 | 0 | Молочные вкусности
5 | Молоко пастеризованное Искренне Ваш отборное 3,4-6,0%, 900 мл | молоко и сливки | мл | NULL | 78.00 | 2019-06-01 00:00:00 | 0 | Молочные вкусности
8 | Молоко стерилизованное Можайское 3,2%, 450 мл | молоко и сливки | мл | 450.000 | 76.00 | 2019-06-01 00:00:00 | 0 | Молочные вкусности
...
```

The query groups by `name_store`, counting 20 rows and 20 unique `id_product` values, returning:

```
name_store | name_cnt | name_uniq_cnt
Молочные вкусности | 20 | 20
```

## Conclusion 🚀

The query successfully calculates the total and unique product counts per store in `products_data_all`, naming the variables `name_cnt` and `name_uniq_cnt`.

With the sample data, it returns one row for "Молочные вкусности" with 20 total and 20 unique products, meeting the task’s requirements.

The implementation is efficient, modular, and extensible, making it ideal for inventory analysis, store performance evaluation, or teaching SQL aggregation and grouping techniques in a retail context.
