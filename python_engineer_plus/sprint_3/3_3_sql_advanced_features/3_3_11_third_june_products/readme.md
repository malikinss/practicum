# Count of Heavy Products (>900g) per Store on June 3, 2019

## Description 📝

The provided SQL query aims to count the number of products weighing more than 900 grams in each store (`name_store`) on June 3, 2019, from the `products_data_all` table. It selects the date (`update_date`), store name (`name_store`), and product count (`name_cnt`), converting `date_upd` to date format. The results are grouped by date and store, filtered to include only stores with fewer than 10 qualifying products.

## Purpose 🎯

Intended to count products weighing over 900 grams per store on June 3, 2019, displaying only stores with fewer than 10 such products, useful for inventory analysis, store-specific product weight evaluation, or educational exercises in SQL aggregation, date conversion, and filtering in a retail context.

## How It Works 🔍

-   **Module Import**:

    -   No external modules; uses standard SQL syntax compatible with relational databases (e.g., SQLite, PostgreSQL).

-   **Query Details**:

    -   **Columns**:
        -   `CAST(date_upd AS DATE) AS update_date`: Converts `date_upd` (DATETIME) to date format, named `update_date`.
        -   `name_store` (VARCHAR(100)): Store name from `products_data_all`.
        -   `COUNT(*) AS name_cnt`: Counts the number of qualifying product rows per store.
    -   **Table**: `products_data_all`, containing product details (`id_product`, `name`, `category`, `units`, `weight`, `price`, `date_upd`, `id_store`, `name_store`).
    -   **Conditions**:
        -   `CAST(date_upd AS DATE) = DATE '2019-06-03'`: Filters for records on June 3, 2019.
        -   `CAST(weight AS REAL) > 900`: Filters for products with weight greater than 900.
        -   `units = 'г'`: Ensures weights are measured in grams.
    -   **Grouping**:
        -   `GROUP BY update_date, name_store`: Aggregates by date and store to count qualifying products.
    -   **Filtering**:
        -   `HAVING name_cnt < 10`: Includes only stores with fewer than 10 qualifying products.
    -   **Sorting**:
        -   `ORDER BY name_store`: Added for consistent output (alphabetical by store name, not required but improves readability).
    -   **Returns**: Rows with date, store name, and count of products over 900 grams, for stores with fewer than 10 such products.

-   **Behavior**:
    -   Filters for products in 'г' (grams) weighing over 900 grams on June 3, 2019, groups by store and date, and counts products.
    -   Based on the sample data:
        -   `products_data_all`: 20 rows, all with `name_store="Молочные вкусности"`, `date_upd="2019-06-01 00:00:00"`, and `category="молоко и сливки"`.
        -   No rows match `date_upd` on `2019-06-03`.
        -   Rows with `units='г'`: `id_product=11` (950.000g), `id_product=12` (200.000g), `id_product=16` (200.000g), `id_product=31` (500.000g).
        -   Only `id_product=11` has `weight > 900` (950.000g), but its `date_upd` is `2019-06-01`.
        -   Result: **No rows returned** due to no matching date.
    -   Expected output (if data existed):
        ```
        update_date | name_store | name_cnt
        2019-06-03 | Lentro | 3
        2019-06-03 | Молочные вкусности | 5
        ...
        ```
    -   **Row Count**: 0 rows with sample data.

## Verification ✅

Implementation satisfies requirements:

-   **Functionality**:

    -   Selects `update_date` (converted date), `name_store`, and product count (`name_cnt`).
    -   Converts `date_upd` to date format using `CAST(date_upd AS DATE)`.
    -   Filters for products with `weight > 900` grams (`units='г'`) on June 3, 2019.
    -   Groups by `update_date` and `name_store`.
    -   Filters for stores with `name_cnt < 10` using `HAVING`.

-   **Correctness**:

    -   Corrected `WHERE` clause uses `CAST(date_upd AS DATE)` instead of the alias `update_date`.
    -   `COUNT(*)` accurately counts qualifying rows.
    -   `units = 'г'` ensures weight is in grams, aligning with the task’s intent.
    -   `HAVING name_cnt < 10` correctly filters post-aggregation.
    -   Sample data has no rows for `2019-06-03`, so empty result is correct.
    -   Cyrillic `name_store` requires UTF-8 encoding.

-   **Output**:

    -   Matches required format: three columns (`update_date`, `name_store`, `name_cnt`).
    -   Returns 0 rows with sample data, as expected.
    -   Column names and structure align with task requirements.

-   **Documentation**: Clear query structure and detailed README.

## Potential Considerations 🛠️

-   **Correctness**:

    -   Assumes `products_data_all` exists; no error handling for missing tables.
    -   No rows match `date_upd` on `2019-06-03` in sample data, indicating a possible data gap.
    -   `units = 'г'` is critical, as weights in `л` or `мл` (e.g., 1.000, 450.000) could be misinterpreted without this filter.
    -   `weight` is `DECIMAL(10,3)`; `CAST(weight AS REAL)` ensures floating-point comparison.
    -   `NULL` weights (4 rows in sample data) are excluded by `weight > 900`.

-   **Performance**:

    -   `COUNT`, `GROUP BY`, and `HAVING`: O(n) for n rows, efficient for small datasets (20 rows).
    -   Filtering on `date_upd`, `weight`, and `units` benefits from indexing, but none defined.
    -   Empty result minimizes data transfer.
    -   Sorting (`ORDER BY name_store`) is negligible with no rows.

-   **Design**:

    -   Corrected query fixes the alias error and uses `COUNT(*)` for robustness.
    -   `CAST(weight AS REAL)` ensures precise weight comparison.
    -   `HAVING` is appropriate for filtering aggregated counts.
    -   Added `ORDER BY name_store` for clarity, though not required.

-   **Alternatives**:

    -   Use `DATE(date_upd)`: Alternative date extraction in some databases.
    -   Simplify `GROUP BY`: Use `GROUP BY name_store` if date is fixed by filter (though current form is robust).
    -   Count unique products: Use `COUNT(DISTINCT id_product)` instead of `COUNT(*)` if only unique products are needed.
    -   Adjust weight threshold: Lower to `> 500` to find matches in sample data.

-   **Extensibility**:

    -   Easily modify to include other dates, stores, or weight thresholds.
    -   Can extend with additional metrics (e.g., `AVG(price)` for heavy products).
    -   Supports integration into inventory reports or dashboards.

-   **Edge Cases**:
    -   **No Matching Rows**: Returns no rows (as with sample data).
    -   **Empty Table**: Returns no rows.
    -   **Missing Table**: Raises a database error (assumed handled by client).
    -   **NULL Weights**: Excluded by `weight > 900` (4 rows in sample data).
    -   **Large Dataset**: Query remains efficient but may need indexing for scale.

## Usage Example (For Clarity, Not Submission) 📦

```sql
-- Execute corrected query
SELECT CAST(date_upd AS DATE) AS update_date, name_store, COUNT(*) AS name_cnt
FROM products_data_all
WHERE CAST(date_upd AS DATE) = DATE '2019-06-03' AND CAST(weight AS REAL) > 900 AND units = 'г'
GROUP BY update_date, name_store
HAVING name_cnt < 10
ORDER BY name_store;
-- Output (based on sample data):
-- (empty result set)

-- Verify no matching data
SELECT date_upd, name_store, name, weight, units
FROM products_data_all
WHERE CAST(date_upd AS DATE) = '2019-06-03' OR (units = 'г' AND weight > 900);
-- Output: Only id_product=11 (950g, 2019-06-01), no 2019-06-03 matches

-- Hypothetical example with matching data
-- Assume data:
-- id_product | name | weight | units | date_upd | name_store | ...
-- 1 | Milk A | 950.000 | г | 2019-06-03 00:00:00 | Молочные вкусности | ...
-- 2 | Milk B | 1000.000 | г | 2019-06-03 00:00:00 | Молочные вкусности | ...
-- 3 | Butter C | 920.000 | г | 2019-06-03 00:00:00 | Lentro | ...
SELECT CAST(date_upd AS DATE) AS update_date, name_store, COUNT(*) AS name_cnt
FROM products_data_all
WHERE CAST(date_upd AS DATE) = DATE '2019-06-03' AND CAST(weight AS REAL) > 900 AND units = 'г'
GROUP BY update_date, name_store
HAVING name_cnt < 10
ORDER BY name_store;
-- Output:
-- update_date | name_store | name_cnt
-- 2019-06-03 | Lentro | 1
-- 2019-06-03 | Молочные вкусности | 2
```

## Example Scenario

Given `products_data_all` (partial, all non-matching):

```
id_product | name | category | units | weight | price | date_upd | id_store | name_store
3 | Молоко цельное пастеризованное Ваша Ферма 3,4-6,0%, 1 л | молоко и сливки | л | 1.000 | 69.00 | 2019-06-01 00:00:00 | 0 | Молочные вкусности
11 | Молоко ультрапастеризованное Домик в деревне 0,5%, 551 г | молоко и сливки | г | 950.000 | 99.00 | 2019-06-01 00:00:00 | 0 | Молочные вкусности
12 | Молоко ультрапастеризованное Вкуснотеево 2,5%, 200 г | молоко и сливки | г | 200.000 | 23.00 | 2019-06-01 00:00:00 | 0 | Молочные вкусности
...
```

No rows match `date_upd` on `2019-06-03`, and only one product (`id_product=11`, 950g) meets `weight > 900` and `units='г'`, but its date is `2019-06-01`. The query returns:

```
(empty result set)
```

## Conclusion 🚀

The corrected query successfully aims to count products weighing over 900 grams per store on June 3, 2019, naming the count `name_cnt` and the date `update_date`, filtering for stores with fewer than 10 products. With the sample data, it returns no rows due to no matching date, which is correct given the data constraints. The implementation is efficient, modular, and extensible, making it suitable for inventory analysis, store-specific weight evaluation, or teaching SQL aggregation, date conversion, and filtering techniques in a retail context.
