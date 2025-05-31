# Milk and Cream Product Query for Non-Holiday Saturdays in June 2019

## Description 📝

The provided SQL query retrieves product details for items in the 'milk and cream' category (`молоко и сливки`) from the `products_data_all` table, specifically for four non-holiday Saturdays in June 2019: June 8, 15, 22, and 29.

It selects the product name (`name`), price (`price`), store name (`name_store`), and update date (`date_upd`), filtering by the specified category and dates.

This query enables analysis of milk and cream product pricing and availability on these specific dates, likely for retail reporting or inventory management purposes.

## Purpose 🎯

Intended for extracting product data for the 'milk and cream' category on four designated Saturdays in June 2019, useful for tracking price trends, store-specific offerings, or educational exercises in SQL filtering and date-based queries within a retail database context.

## How It Works 🔍

-   **Module Import**:

    -   No external modules; uses standard SQL syntax compatible with relational databases (e.g., SQLite, PostgreSQL).

-   **Query**:

    -   **`SELECT name, price, name_store, date_upd FROM products_data_all WHERE category = 'молоко и сливки' AND date_upd IN ('2019-06-08', '2019-06-15', '2019-06-22', '2019-06-29');`**
        -   **Columns**:
            -   `name` (VARCHAR(255)): Product name (e.g., "Молоко цельное пастеризованное Ваша Ферма 3,4-6,0%, 1 л").
            -   `price` (DECIMAL(10,2)): Product price (e.g., 69.00).
            -   `name_store` (VARCHAR(100)): Store name (e.g., "Молочные вкусности").
            -   `date_upd` (DATETIME): Date of price update (e.g., `2019-06-08 00:00:00`).
        -   **Table**: `products_data_all`, which aggregates product and store information.
        -   **Conditions**:
            -   `category = 'молоко и сливки'`: Filters for 'milk and cream' products (Cyrillic text).
            -   `date_upd IN ('2019-06-08', '2019-06-15', '2019-06-22', '2019-06-29')`: Matches records for the specified Saturdays.
        -   **Returns**: Rows matching the category and any of the four dates, with the specified columns.

-   **Behavior**:
    -   Retrieves milk and cream products for the specified dates from `products_data_all`.
    -   Based on the sample data provided previously, `products_data_all` contains entries only for `2019-06-01`. Therefore, this query is expected to return **no rows** unless additional data for June 8, 15, 22, or 29 exists in the actual database.
    -   Example output (if data existed):
        ```
        name | price | name_store | date_upd
        Молоко цельное пастеризованное Ваша Ферма 3,4-6,0%, 1 л | 69.00 | Молочные вкусности | 2019-06-08 00:00:00
        ...
        ```
    -   **Row Count**: Likely 0 with the provided sample data, as no records match the specified dates.

## Verification ✅

Implementation satisfies requirements:

-   **Functionality**:

    -   Selects requested columns: `name`, `price`, `name_store`, `date_upd`.
    -   Filters by `category = 'молоко и сливки'` and `date_upd` in `['2019-06-08', '2019-06-15', '2019-06-22', '2019-06-29']`.
    -   Retrieves data from `products_data_all`.

-   **Correctness**:

    -   Column names match `products_data_all` schema.
    -   `category` uses Cyrillic (`молоко и сливки`), consistent with sample data.
    -   `date_upd IN (...)` assumes exact `DATETIME` matches (e.g., `2019-06-08 00:00:00`); sample data suggests no matches.
    -   All selected columns are `NOT NULL` in the schema, ensuring complete results if rows exist.

-   **Output**:

    -   Expected to return no rows with provided sample data (all entries are for `2019-06-01`).
    -   If data exists for the specified dates, output matches the format: a result set with four columns.
    -   Column headers are displayed even if no rows are returned.

-   **Documentation**: Clear query structure and detailed README.

## Potential Considerations 🛠️

-   **Correctness**:

    -   Assumes `products_data_all` exists; no error handling for missing tables.
    -   `date_upd IN (...)` expects exact `DATETIME` values (e.g., `2019-06-08 00:00:00`). Partial date matches require `DATE(date_upd) IN (...)`.
    -   Cyrillic `category` requires UTF-8 encoding support in the database.
    -   Sample data indicates no records for June 8–29, suggesting either a data gap or a need for additional data.

-   **Performance**:

    -   `SELECT`: O(n) for n rows, efficient for small datasets.
    -   `IN` clause with four dates is fast; benefits from indexing on `date_upd`, but none defined beyond `PRIMARY KEY` (`id_product`, `id_store`).
    -   Explicit column selection minimizes data transfer.

-   **Design**:

    -   Focused query retrieves only required data, following SQL best practices.
    -   Uses exact schema column names for clarity.
    -   No sorting or grouping, as not requested.

-   **Alternatives**:

    -   Use `DATE(date_upd) IN (...)`: Match any time on the specified dates.
    -   Add `ORDER BY date_upd, name`: Sort results by date and product name.
    -   Join with `products`: Cross-check `category` consistency.
    -   Use a date range: `date_upd BETWEEN '2019-06-08' AND '2019-06-29'` with a day-of-week filter (e.g., `DAYOFWEEK`).

-   **Extensibility**:

    -   Easily add more columns (e.g., `units`, `weight`) or dates.
    -   Can extend to analyze price changes across Saturdays.
    -   Supports integration into reports (e.g., weekly product trends).

-   **Edge Cases**:
    -   **Empty Results**: Returns no rows if no matches (likely with sample data).
    -   **Missing Table**: Raises a database error (assumed handled by client).
    -   **Case Sensitivity**: `category` match is exact; sample data is consistent.
    -   **Date Format**: Assumes `YYYY-MM-DD`; other formats may fail.
    -   **No Data for Dates**: Sample data lacks entries for June 8–29, resulting in empty output.

## Usage Example (For Clarity, Not Submission) 📦

```sql
-- Execute query in a SQL client
SELECT name, price, name_store, date_upd
FROM products_data_all
WHERE category = 'молоко и сливки'
AND date_upd IN ('2019-06-08', '2019-06-15', '2019-06-22', '2019-06-29');
-- Expected output (with sample data):
-- (empty result set, as no rows match the dates)

-- Hypothetical output (if data existed):
-- name | price | name_store | date_upd
-- Молоко цельное пастеризованное Ваша Ферма 3,4-6,0%, 1 л | 69.00 | Молочные вкусности | 2019-06-08 00:00:00
-- Молоко пастеризованное Искренне Ваш отборное 3,4-6,0%, 900 мл | 78.00 | Молочные вкусности | 2019-06-08 00:00:00
-- ...

-- With sorting (optional)
SELECT name, price, name_store, date_upd
FROM products_data_all
WHERE category = 'молоко и сливки'
AND date_upd IN ('2019-06-08', '2019-06-15', '2019-06-22', '2019-06-29')
ORDER BY date_upd, name;
-- Output: Same data (if any), sorted by date and name
```

## Example Scenario

Given `products_data_all` from sample data:

```
id_product | name | category | units | weight | price | date_upd | id_store | name_store
3 | Молоко цельное пастеризованное Ваша Ферма 3,4-6,0%, 1 л | молоко и сливки | л | 1.000 | 69.00 | 2019-06-01 00:00:00 | 0 | Молочные вкусности
...
```

The query returns no rows, as all entries are for `2019-06-01`. If data for `2019-06-08` existed, e.g.:

```
3 | Молоко цельное пастеризованное Ваша Ферма 3,4-6,0%, 1 л | молоко и сливки | л | 1.000 | 69.00 | 2019-06-08 00:00:00 | 0 | Молочные вкусности
```

The output would be:

```
name | price | name_store | date_upd
Молоко цельное пастеризованное Ваша Ферма 3,4-6,0%, 1 л | 69.00 | Молочные вкусности | 2019-06-08 00:00:00
...
```

## Conclusion 🚀

The query successfully targets `name`, `price`, `name_store`, and `date_upd` for 'milk and cream' products on four non-holiday Saturdays in June 2019 from `products_data_all`.

While the sample data results in an empty output due to missing records for the specified dates, the query is correctly structured, efficient, and meets the task’s requirements.

It is modular and extensible, making it suitable for retail analysis, price tracking, or teaching SQL date-based filtering techniques.
