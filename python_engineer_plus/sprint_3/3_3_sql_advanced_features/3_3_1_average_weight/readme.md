# Average Weight Calculation for Products in Grams

## Description 📝

The provided SQL query calculates the average weight of products from the `products_data_all` table, specifically for products with units in grams (`units='г'`).
It converts the `weight` column to a floating-point number using `CAST(weight AS real)`, computes the average with `AVG`, and names the result `average`.
This query enables analysis of product weights in a retail database, focusing on gram-based measurements.

## Purpose 🎯

Intended for determining the average weight of gram-based products, useful for inventory analysis, product standardization, or educational exercises in SQL aggregation, type casting, and filtering within a retail context.

## How It Works 🔍

-   **Module Import**:

    -   No external modules; uses standard SQL syntax compatible with relational databases (e.g., SQLite, PostgreSQL).

-   **Query**:

    -   **`SELECT AVG(CAST(weight AS real)) AS average FROM products_data_all WHERE units = 'г';`**
        -   **Function**:
            -   `CAST(weight AS real)`: Converts the `weight` column (DECIMAL(10,3)) to a floating-point number (`real` in SQLite, equivalent to `FLOAT` or `DOUBLE` in other databases).
            -   `AVG(...)`: Computes the arithmetic mean of the converted weights.
            -   `AS average`: Names the output column `average`.
        -   **Table**: `products_data_all`, containing product details (`id_product`, `name`, `category`, `units`, `weight`, `price`, `date_upd`, `id_store`, `name_store`).
        -   **Condition**:
            -   `WHERE units = 'г'`: Filters for products with weights measured in grams (Cyrillic 'г').
        -   **Returns**: A single row with one column (`average`) containing the average weight in grams.

-   **Behavior**:
    -   Identifies rows in `products_data_all` where `units='г'`.
    -   Converts their `weight` values to floating-point numbers and calculates the average.
    -   Based on the sample data:
        -   `products_data_all`: 20 rows.
        -   Rows with `units='г'`: `id_product` 11 (`weight=950.000`), 12 (`weight=200.000`), 16 (`weight=200.000`), 31 (`weight=500.000`)—4 rows.
        -   Weights: 950.000, 200.000, 200.000, 500.000.
        -   Calculation: `(950.000 + 200.000 + 200.000 + 500.000) / 4 = 1850.000 / 4 = 462.500`.
    -   Output:
        ```
        average
        462.5
        ```
    -   **Row Count**: Always returns one row with the average.

## Verification ✅

Implementation satisfies requirements:

-   **Functionality**:

    -   Calculates the average of `weight` for products with `units='г'`.
    -   Converts `weight` to a floating-point number using `CAST(weight AS real)`.
    -   Names the output column `average`.

-   **Correctness**:

    -   `weight` is `DECIMAL(10,3)` in `products_data_all`, and `CAST(weight AS real)` ensures floating-point arithmetic.
    -   `WHERE units = 'г'` correctly filters for gram-based products (Cyrillic 'г').
    -   Sample data has 4 rows with `units='г'`, yielding an average of 462.5 grams.
    -   Handles `NULL` weights (none in gram-based rows) by excluding them from `AVG`.

-   **Output**:

    -   Single column (`average`) with the value 462.5 for sample data.
    -   Matches required format: one row, one column named `average`.

-   **Documentation**: Clear query structure and detailed README.

## Potential Considerations 🛠️

-   **Correctness**:

    -   Assumes `products_data_all` exists; no error handling for missing tables.
    -   `units='г'` uses Cyrillic, requiring proper database encoding (e.g., UTF-8).
    -   `weight` is `DECIMAL(10,3)`, so `CAST(weight AS real)` preserves precision.
    -   No `NULL` weights in gram-based rows in sample data; `AVG` ignores `NULL` if present.

-   **Performance**:

    -   `AVG` and `WHERE`: O(n) for n rows, efficient for small datasets (20 rows, 4 matching).
    -   Filtering on `units` benefits from indexing, but none defined.
    -   Minimal data transfer due to single scalar output.

-   **Design**:

    -   Simple, focused query meets task requirements.
    -   `CAST(weight AS real)` ensures floating-point output, though `DECIMAL` input is already precise.
    -   Clear column naming with `AS average`.

-   **Alternatives**:

    -   Omit `CAST`: `AVG(weight)` works, as `DECIMAL` supports averaging, but may not guarantee floating-point output.
    -   Use `CAST(weight AS FLOAT)`: Equivalent to `real` in most databases.
    -   Add `ROUND(AVG(CAST(weight AS real)), 2)`: Control decimal places in output.
    -   Filter other units: Extend to compare averages across units (e.g., 'л', 'мл').

-   **Extensibility**:

    -   Easily modify to calculate averages for other units or columns (e.g., `price`).
    -   Can extend with `GROUP BY category` to compare averages by category.
    -   Supports integration into inventory reports.

-   **Edge Cases**:
    -   **No Matching Rows**: Returns `NULL` for `average` (not applicable with sample data).
    -   **Empty Table**: Returns `NULL` for `average`.
    -   **Missing Table**: Raises a database error (assumed handled by client).
    -   **NULL Weights**: Excluded from `AVG`, reducing the count of averaged rows.
    -   **Large Dataset**: Query remains efficient but may need indexing for scale.

## Usage Example (For Clarity, Not Submission) 📦

```sql
-- Execute query in a SQL client
SELECT AVG(CAST(weight AS real)) AS average
FROM products_data_all
WHERE units = 'г';
-- Output (based on sample data):
-- average
-- 462.5

-- Verify matching rows
SELECT id_product, name, weight, units
FROM products_data_all
WHERE units = 'г';
-- Output:
-- id_product | name | weight | units
-- 11 | Молоко ультрапастеризованное Домик в деревне 0,5%, 950 г | 950.000 | г
-- 12 | Молоко ультрапастеризованное Вкуснотеево 2,5%, 200 г | 200.000 | г
-- 16 | Молоко ультрапастеризованное Parmalat 1,8%, 200 г | 200.000 | г
-- 31 | Молоко топленое Рузское 2,5%, 500 г | 500.000 | г

-- With rounding (optional)
SELECT ROUND(AVG(CAST(weight AS real)), 2) AS average
FROM products_data_all
WHERE units = 'г';
-- Output:
-- average
-- 462.50
```

## Example Scenario

Given `products_data_all` (partial):

```
id_product | name | category | units | weight | price | date_upd | id_store | name_store
11 | Молоко ультрапастеризованное Домик в деревне 0,5%, 950 г | молоко и сливки | г | 950.000 | 99.00 | 2019-06-01 00:00:00 | 0 | Молочные вкусности
12 | Молоко ультрапастеризованное Вкуснотеево 2,5%, 200 г | молоко и сливки | г | 200.000 | 23.00 | 2019-06-01 00:00:00 | 0 | Молочные вкусности
16 | Молоко ультрапастеризованное Parmalat 1,8%, 200 г | молоко и сливки | г | 200.000 | 24.00 | 2019-06-01 00:00:00 | 0 | Молочные вкусности
31 | Молоко топленое Рузское 2,5%, 500 г | молоко и сливки | г | 500.000 | 72.00 | 2019-06-01 00:00:00 | 0 | Молочные вкусности
...
```

The query calculates: `(950.000 + 200.000 + 200.000 + 500.000) / 4 = 462.5` and returns:

```
average
462.5
```

## Conclusion 🚀

The query successfully calculates the average weight of gram-based products in `products_data_all`, converting `weight` to a floating-point number and naming the result `average`. With the sample data, it returns 462.5 grams, meeting the task’s requirements.
The implementation is efficient, modular, and extensible, making it ideal for inventory analysis, product weight standardization, or teaching SQL aggregation and type casting techniques in a retail context.
