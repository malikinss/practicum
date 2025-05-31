# Milk and Cream Product Query for World Milk Day

## Description 📝

The provided SQL query retrieves product details for items in the 'milk and cream' category (`молоко и сливки`) from the `products_data_all` table, specifically for World Milk Day on `2019-06-01`.

It selects the product name (`name`), price (`price`), store name (`name_store`), and update date (`date_upd`), filtering by the specified category and date.

This query enables analysis of milk and cream products available in stores on a particular day, focusing on relevant fields for a retail database context.

## Purpose 🎯

Intended for analyzing product offerings and pricing for the 'milk and cream' category on a specific date (World Milk Day, `2019-06-01`), useful for retail reporting, inventory management, or educational exercises in SQL filtering and data selection.

## How It Works 🔍

-   **Module Import**:

    -   No external modules; uses standard SQL syntax compatible with relational databases (e.g., SQLite, PostgreSQL).

-   **Query**:

    -   **`SELECT name, price, name_store, date_upd FROM products_data_all WHERE category = 'молоко и сливки' AND date_upd = '2019-06-01';`**
        -   **Columns**:
            -   `name` (VARCHAR(255)): Product name (e.g., "Молоко цельное пастеризованное Ваша Ферма 3,4-6,0%, 1 л").
            -   `price` (DECIMAL(10,2)): Product price (e.g., 69.00).
            -   `name_store` (VARCHAR(100)): Store name (e.g., "Молочные вкусности").
            -   `date_upd` (DATETIME): Date of price update (e.g., `2019-06-01 00:00:00`).
        -   **Table**: `products_data_all`, which contains detailed product and store information.
        -   **Conditions**:
            -   `category = 'молоко и сливки'`: Filters for 'milk and cream' products (Cyrillic text).
            -   `date_upd = '2019-06-01'`: Matches records for June 1, 2019.
        -   **Returns**: Rows matching the category and date, with the specified columns.

-   **Behavior**:
    -   Retrieves all milk and cream products available on `2019-06-01` from `products_data_all`.
    -   Based on sample data, returns 20 rows (all entries in `products_data_all` are for `2019-06-01` and `молоко и сливки`).
    -   Example output:
        ```
        name | price | name_store | date_upd
        Молоко цельное пастеризованное Ваша Ферма 3,4-6,0%, 1 л | 69.00 | Молочные вкусности | 2019-06-01 00:00:00
        Молоко пастеризованное Искренне Ваш отборное 3,4-6,0%, 900 мл | 78.00 | Молочные вкусности | 2019-06-01 00:00:00
        Молоко стерилизованное Можайское 3,2%, 450 мл | 76.00 | Молочные вкусности | 2019-06-01 00:00:00
        ...
        ```

## Verification ✅

Implementation satisfies requirements:

-   **Functionality**:

    -   Selects requested columns: `name`, `price`, `name_store`, `date_upd`.
    -   Filters by `category = 'молоко и сливки'` and `date_upd = '2019-06-01'`.
    -   Retrieves data from `products_data_all`.

-   **Correctness**:

    -   Column names match `products_data_all` schema.
    -   `category` uses Cyrillic (`молоко и сливки`), consistent with sample data.
    -   `date_upd = '2019-06-01'` is treated as `2019-06-01 00:00:00` in `DATETIME` format, matching sample data.
    -   All selected columns are `NOT NULL` in the schema, ensuring complete results.

-   **Output**:

    -   Matches expected format: a result set with four columns for all matching rows.
    -   Returns 20 rows based on sample data, all for `молоко и сливки` on `2019-06-01`.

-   **Documentation**: Clear query structure and detailed README.

## Potential Considerations 🛠️

-   **Correctness**:

    -   Assumes `products_data_all` exists and is populated; no error handling for missing tables.
    -   `date_upd = '2019-06-01'` assumes exact `DATETIME` match (e.g., `2019-06-01 00:00:00`); partial date matches (e.g., any time on `2019-06-01`) would require `DATE(date_upd) = '2019-06-01'`.
    -   Cyrillic `category` requires proper database encoding (e.g., UTF-8).
    -   No validation for empty results, but sample data ensures matches.

-   **Performance**:

    -   `SELECT`: O(n) for n rows, efficient for small datasets (20 rows).
    -   Filtering on `category` and `date_upd` benefits from indexes, but none are defined beyond `PRIMARY KEY` (`id_product`, `id_store`).
    -   Explicit column selection reduces data transfer compared to `SELECT *`.

-   **Design**:

    -   Simple, focused query aligns with task requirements.
    -   Uses exact column names from schema, ensuring clarity.
    -   No sorting or grouping, as not requested.

-   **Alternatives**:

    -   Use `DATE(date_upd) = '2019-06-01'`: Match any time on June 1, 2019.
    -   Add `ORDER BY name`: Sort results for readability.
    -   Join with `products`: Validate `category` against `products` table.
    -   Use aliases (e.g., `SELECT name AS product_name`): Enhance output clarity.

-   **Extensibility**:

    -   Easily add more columns (e.g., `units`, `weight`) or filters (e.g., `price < 100`).
    -   Can extend to compare prices across stores or dates.
    -   Supports integration into larger reports (e.g., World Milk Day promotions).

-   **Edge Cases**:
    -   **Empty Results**: Returns no rows if no matches (unlikely with sample data).
    -   **Missing Table**: Raises a database error (assumed handled by client).
    -   **Case Sensitivity**: `category` match is exact; sample data uses consistent Cyrillic.
    -   **Date Format**: Assumes `DATETIME` format `YYYY-MM-DD`; other formats may fail.

## Usage Example (For Clarity, Not Submission) 📦

```sql
-- Execute query in a SQL client
SELECT name, price, name_store, date_upd
FROM products_data_all
WHERE category = 'молоко и сливки' AND date_upd = '2019-06-01';
-- Example output:
-- name | price | name_store | date_upd
-- Молоко цельное пастеризованное Ваша Ферма 3,4-6,0%, 1 л | 69.00 | Молочные вкусности | 2019-06-01 00:00:00
-- Молоко пастеризованное Искренне Ваш отборное 3,4-6,0%, 900 мл | 78.00 | Молочные вкусности | 2019-06-01 00:00:00
-- Молоко стерилизованное Можайское 3,2%, 450 мл | 76.00 | Молочные вкусности | 2019-06-01 00:00:00
-- ...

-- With sorting (optional)
SELECT name, price, name_store, date_upd
FROM products_data_all
WHERE category = 'молоко и сливки' AND date_upd = '2019-06-01'
ORDER BY price;
-- Output: Same data, sorted by price
```

## Example Scenario

Given `products_data_all` with:

```
id_product | name | category | units | weight | price | date_upd | id_store | name_store
3 | Молоко цельное пастеризованное Ваша Ферма 3,4-6,0%, 1 л | молоко и сливки | л | 1.000 | 69.00 | 2019-06-01 00:00:00 | 0 | Молочные вкусности
5 | Молоко пастеризованное Искренне Ваш отборное 3,4-6,0%, 900 мл | молоко и сливки | мл | NULL | 78.00 | 2019-06-01 00:00:00 | 0 | Молочные вкусности
...
```

The query returns:

```
name | price | name_store | date_upd
Молоко цельное пастеризованное Ваша Ферма 3,4-6,0%, 1 л | 69.00 | Молочные вкусности | 2019-06-01 00:00:00
Молоко пастеризованное Искренне Ваш отборное 3,4-6,0%, 900 мл | 78.00 | Молочные вкусности | 2019-06-01 00:00:00
...
```

## Conclusion 🚀

The query successfully retrieves `name`, `price`, `name_store`, and `date_upd` for 'milk and cream' products on `2019-06-01` from `products_data_all`.

It is efficient, meets the task’s requirements, and provides a clear view of relevant product data.

The implementation is modular and extensible, making it ideal for retail analysis, World Milk Day reports, or teaching SQL filtering techniques.
