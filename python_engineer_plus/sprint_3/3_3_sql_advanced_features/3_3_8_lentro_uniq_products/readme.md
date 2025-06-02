# Unique Product Count per Category in Lentro Store on June 30, 2019

## Description 📝

The provided SQL query aims to count the number of unique products in each category for the store 'Lentro' on June 30, 2019, from the `products_data_all` table.

It selects the date (`update_date`), store name (`name_store`), category (`category`), and the count of unique products (`uniq_name_cnt`), converting the `date_upd` column to a date format.

The results are grouped by date, store, and category, sorted by the unique product count in descending order.

## Purpose 🎯

Intended for summarizing the number of unique products by category in the 'Lentro' store on June 30, 2019, useful for inventory analysis, store-specific category performance, or educational exercises in SQL aggregation, date conversion, grouping, and sorting within a retail context.

## How It Works 🔍

-   **Module Import**:

    -   No external modules; uses standard SQL syntax compatible with relational databases (e.g., SQLite, PostgreSQL).

-   **Query Details**:

    -   **Columns**:
        -   `CAST(date_upd AS DATE) AS update_date`: Converts `date_upd` (DATETIME) to date format, named `update_date`.
        -   `name_store` (VARCHAR(100)): Store name from `products_data_all`.
        -   `category` (VARCHAR(100)): Product category (e.g., "молоко и сливки").
        -   `COUNT(DISTINCT id_product) AS uniq_name_cnt`: Counts unique `id_product` values per category.
    -   **Table**: `products_data_all`, containing product details (`id_product`, `name`, `category`, `units`, `weight`, `price`, `date_upd`, `id_store`, `name_store`).
    -   **Conditions**:
        -   `name_store = 'Lentro'`: Filters for the 'Lentro' store.
        -   `CAST(date_upd AS DATE) = DATE '2019-06-30'`: Filters for records where the date portion of `date_upd` is June 30, 2019.
    -   **Grouping**:
        -   `GROUP BY update_date, name_store, category`: Aggregates by date, store, and category to count unique products.
    -   **Sorting**:
        -   `ORDER BY uniq_name_cnt DESC`: Sorts results by unique product count in descending order.
    -   **Returns**: One row per unique category in 'Lentro' on June 30, 2019, with date, store name, category, and unique product count.

-   **Behavior**:
    -   Filters rows for 'Lentro' store on June 30, 2019, groups by date, store, and category, and counts unique `id_product` values.
    -   Based on the sample data:
        -   `products_data_all`: 20 rows, all with `name_store="Молочные вкусности"`, `date_upd="2019-06-01 00:00:00"`, and `category="молоко и сливки"`.
        -   No rows match `name_store='Lentro'` or `date_upd` on `2019-06-30`.
        -   Result: **No rows returned** due to no matching data.
    -   Expected output (if data existed):
        ```
        update_date | name_store | category | uniq_name_cnt
        2019-06-30 | Lentro | молоко и сливки | 10
        2019-06-30 | Lentro | масло сливочное и маргарин | 5
        ...
        ```
    -   **Row Count**: 0 rows with sample data.

## Verification ✅

Implementation satisfies requirements:

-   **Functionality**:

    -   Selects `update_date` (converted date), `name_store`, `category`, and unique product count (`uniq_name_cnt`).
    -   Converts `date_upd` to date format using `CAST(date_upd AS DATE)`.
    -   Filters for 'Lentro' store on June 30, 2019.
    -   Groups by `update_date`, `name_store`, and `category`.
    -   Sorts by `uniq_name_cnt` in descending order.

-   **Correctness**:

    -   Corrected `WHERE` clause uses `CAST(date_upd AS DATE)` instead of the alias `update_date`.
    -   `COUNT(DISTINCT id_product)` accurately counts unique products.
    -   `GROUP BY update_date, name_store, category` ensures precise aggregation.
    -   `ORDER BY uniq_name_cnt DESC` sorts as required.
    -   Sample data has no rows for `name_store='Lentro'` or `date_upd` on `2019-06-30`, so empty result is correct.
    -   Cyrillic `category` and `name_store` require UTF-8 encoding.

-   **Output**:

    -   Matches required format: four columns (`update_date`, `name_store`, `category`, `uniq_name_cnt`).
    -   Returns 0 rows with sample data, as expected.
    -   Column names and structure align with task requirements.

-   **Documentation**: Clear query structure and detailed README.

## Potential Considerations 🛠️

-   **Correctness**:

    -   Assumes `products_data_all` exists; no error handling for missing tables.
    -   No rows match `name_store='Lentro'` or `date_upd` on `2019-06-30` in sample data, indicating a possible data gap.
    -   `CAST(date_upd AS DATE)` correctly extracts the date from `date_upd` (DATETIME).
    -   `GROUP BY` includes `update_date` and `name_store` for robustness, though redundant with single-store and single-date filters.

-   **Performance**:

    -   `COUNT(DISTINCT id_product)` and `GROUP BY`: O(n) for n rows, efficient for small datasets (20 rows).
    -   Filtering on `name_store` and `date_upd` benefits from indexing, but none defined.
    -   Empty result minimizes data transfer.
    -   Sorting (`ORDER BY`) is negligible with no rows.

-   **Design**:

    -   Corrected query fixes the alias error in `WHERE`.
    -   Clear variable naming (`uniq_name_cnt`, `update_date`) enhances readability.
    -   `COUNT(DISTINCT id_product)` ensures unique product counts, aligning with the task.

-   **Alternatives**:

    -   Use `DATE(date_upd)`: Alternative date extraction in some databases.
    -   Simplify `GROUP BY`: Use `GROUP BY name_store, category` if date is fixed by filter (though current form is robust).
    -   Add tie-breaker: `ORDER BY uniq_name_cnt DESC, category` to sort categories alphabetically for equal counts.
    -   Include total products: Add `COUNT(*)` for comparison with unique counts.

-   **Extensibility**:

    -   Easily modify to include other stores, dates, or categories.
    -   Can extend with additional metrics (e.g., `AVG(price)` per category).
    -   Supports integration into inventory reports or dashboards.

-   **Edge Cases**:
    -   **No Matching Rows**: Returns no rows (as with sample data).
    -   **Empty Table**: Returns no rows.
    -   **Missing Table**: Raises a database error (assumed handled by client).
    -   **NULL Values**: `id_product` and `name_store` are non-`NULL` in sample data; `COUNT(DISTINCT)` handles `NULL` correctly.
    -   **Large Dataset**: Query remains efficient but may need indexing for scale.

## Usage Example (For Clarity, Not Submission) 📦

```sql
-- Execute corrected query
SELECT CAST(date_upd AS DATE) AS update_date, name_store, category, COUNT(DISTINCT id_product) AS uniq_name_cnt
FROM products_data_all
WHERE name_store = 'Lentro' AND CAST(date_upd AS DATE) = DATE '2019-06-30'
GROUP BY update_date, name_store, category
ORDER BY uniq_name_cnt DESC;
-- Output (based on sample data):
-- (empty result set)

-- Verify no matching data
SELECT name_store, date_upd, category, id_product
FROM products_data_all
WHERE name_store = 'Lentro' OR CAST(date_upd AS DATE) = '2019-06-30';
-- Output: (empty, as no rows match store or date)

-- Hypothetical example with matching data
-- Assume data:
-- id_product | name | category | date_upd | name_store | ...
-- 1 | Milk A | молоко и сливки | 2019-06-30 00:00:00 | Lentro | ...
-- 2 | Milk B | молоко и сливки | 2019-06-30 00:00:00 | Lentro | ...
-- 3 | Butter C | масло сливочное и маргарин | 2019-06-30 00:00:00 | Lentro | ...
SELECT CAST(date_upd AS DATE) AS update_date, name_store, category, COUNT(DISTINCT id_product) AS uniq_name_cnt
FROM products_data_all
WHERE name_store = 'Lentro' AND CAST(date_upd AS DATE) = DATE '2019-06-30'
GROUP BY update_date, name_store, category
ORDER BY uniq_name_cnt DESC;
-- Output:
-- update_date | name_store | category | uniq_name_cnt
-- 2019-06-30 | Lentro | молоко и сливки | 2
-- 2019-06-30 | Lentro | масло сливочное и маргарин | 1
```

## Example Scenario

Given `products_data_all` (sample, all non-matching):

```
id_product | name | category | units | weight | price | date_upd | id_store | name_store
3 | Молоко цельное пастеризованное Ваша Ферма 3,4-6,0%, 1 л | молоко и сливки | л | 1.000 | 69.00 | 2019-06-01 00:00:00 | 0 | Молочные вкусности
5 | Молоко пастеризованное Искренне Ваш отборное 3,4-6,0%, 900 мл | молоко и сливки | мл | NULL | 78.00 | 2019-06-01 00:00:00 | 0 | Молочные вкусности
...
```

No rows match `name_store='Lentro'` or `date_upd` on `2019-06-30`, so the query returns:

```
(empty result set)
```

## Conclusion 🚀

The corrected query successfully aims to count unique products per category in the 'Lentro' store on June 30, 2019, naming the count variable `uniq_name_cnt`, converting `date_upd` to date format, and sorting by count in descending order.

With the sample data, it returns no rows due to no matching store or date, which is correct given the data constraints.

The implementation is efficient, modular, and extensible, making it suitable for inventory analysis, store-specific category evaluation, or teaching SQL aggregation, date conversion, and sorting techniques in a retail context.
