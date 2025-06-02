# Maximum Weight Calculation per Product Category

## Description 📝

The provided SQL query calculates the maximum weight of products in each category from the `products_data_all` table.

It selects the category (`category`) and the maximum weight (`max_weight`), converting the `weight` column to a floating-point number using `CAST(weight AS real)`.

The results are grouped by category and sorted alphabetically by category.

This query enables analysis of the heaviest products within each product category in a retail database context.

## Purpose 🎯

Intended for identifying the heaviest product in each category, useful for inventory analysis, product packaging assessment, or educational exercises in SQL aggregation, type casting, grouping, and sorting within a retail environment.

## How It Works 🔍

-   **Module Import**:

    -   No external modules; uses standard SQL syntax compatible with relational databases (e.g., SQLite, PostgreSQL).

-   **Query**:

    -   **`SELECT category, MAX(CAST(weight AS real)) AS max_weight FROM products_data_all GROUP BY category ORDER BY category;`**
        -   **Columns**:
            -   `category` (VARCHAR(100)): Product category (e.g., "молоко и сливки").
            -   `MAX(CAST(weight AS real)) AS max_weight`: Maximum weight per category, with `weight` (DECIMAL(10,3)) converted to a floating-point number (`real` in SQLite, equivalent to `FLOAT` or `DOUBLE`).
        -   **Table**: `products_data_all`, containing product details (`id_product`, `name`, `category`, `units`, `weight`, `price`, `date_upd`, `id_store`, `name_store`).
        -   **Grouping**:
            -   `GROUP BY category`: Aggregates results by category, computing the maximum weight for each unique category.
        -   **Sorting**:
            -   `ORDER BY category`: Sorts results alphabetically by category (ascending).
        -   **Returns**: One row per unique category, with the category name and its maximum weight.

-   **Behavior**:
    -   Groups all rows in `products_data_all` by `category`, calculating the maximum `weight` for each group.
    -   Based on the sample data:
        -   `products_data_all`: 20 rows, all with `category="молоко и сливки"`.
        -   Non-`NULL` `weight` values: 1.000, 450.000, 950.000, 200.000, 1.400, 1.760, 1.000, 0.950, 200.000, 1.000, 0.450, 925.000, 500.000, 930.000, 0.500, 930.000 (16 rows; 4 rows have `NULL` weight).
        -   Units vary (`л`, `мл`, `г`), but `weight` is treated numerically post-casting.
        -   Maximum weight for "молоко и сливки": 950.000 (from `id_product=11`, units='г').
    -   Output:
        ```
        category | max_weight
        молоко и сливки | 950.0
        ```
    -   **Row Count**: 1 row (only one category in sample data).

## Verification ✅

Implementation satisfies requirements:

-   **Functionality**:

    -   Selects `category` and maximum `weight` (named `max_weight`).
    -   Converts `weight` to a floating-point number using `CAST(weight AS real)`.
    -   Groups results by `category`.
    -   Sorts by `category` in ascending order.

-   **Correctness**:

    -   `weight` is `DECIMAL(10,3)`; `CAST(weight AS real)` ensures floating-point output.
    -   `GROUP BY category` correctly aggregates by category.
    -   `MAX` ignores `NULL` weights (4 rows), ensuring accurate maximum.
    -   Sample data has one category ("молоко и сливки") with a maximum weight of 950.0.
    -   `ORDER BY category` ensures alphabetical sorting.

-   **Output**:

    -   Matches required format: two columns (`category`, `max_weight`).
    -   Returns 1 row for sample data, reflecting the single category.
    -   Value (950.0) and column names align with task requirements.

-   **Documentation**: Clear query structure and detailed README.

## Potential Considerations 🛠️

-   **Correctness**:

    -   Assumes `products_data_all` exists; no error handling for missing tables.
    -   `category` uses Cyrillic ("молоко и сливки"), requiring UTF-8 encoding.
    -   `weight` units vary (`л`, `мл`, `г`), but numerical comparison assumes consistent measurement (e.g., all treated as grams or liters).
    -   `NULL` weights (4 rows) are excluded by `MAX`, as intended.

-   **Performance**:

    -   `MAX` and `GROUP BY`: O(n) for n rows, efficient for small datasets (20 rows).
    -   Sorting (`ORDER BY`): O(n log n), negligible for 1 row.
    -   Indexing on `category` could optimize grouping for large datasets.

-   **Design**:

    -   Focused query meets task requirements.
    -   `CAST(weight AS real)` ensures floating-point output, though `DECIMAL` is precise.
    -   Clear variable naming (`max_weight`) and alphabetical sorting enhance usability.

-   **Alternatives**:

    -   Omit `CAST`: `MAX(weight)` works for `DECIMAL`, but may not guarantee floating-point output.
    -   Use `CAST(weight AS FLOAT)`: Equivalent to `real`.
    -   Filter by `units`: Add `WHERE units = 'г'` to standardize units.
    -   Include product details: Join with `name` to show the heaviest product per category.

-   **Extensibility**:

    -   Easily modify to include other columns (e.g., `units`) or filters (e.g., `WHERE date_upd = '2019-06-01'`).
    -   Can extend with subqueries to find products matching the maximum weight.
    -   Supports integration into inventory reports or dashboards.

-   **Edge Cases**:
    -   **No Matching Rows**: Returns no rows (not applicable with sample data).
    -   **Empty Table**: Returns no rows.
    -   **Missing Table**: Raises a database error (assumed handled by client).
    -   **All `NULL` Weights**: Returns `NULL` for `max_weight` per category (not applicable).
    -   **Multiple Categories**: Query scales to handle additional categories (none in sample data).

## Usage Example (For Clarity, Not Submission) 📦

```sql
-- Execute query in a SQL client
SELECT category, MAX(CAST(weight AS real)) AS max_weight
FROM products_data_all
GROUP BY category
ORDER BY category;
-- Output (based on sample data):
-- category | max_weight
-- молоко и сливки | 950.0

-- Verify maximum weight
SELECT category, id_product, name, weight, units
FROM products_data_all
WHERE category = 'молоко и сливки' AND weight IS NOT NULL
ORDER BY weight DESC
LIMIT 1;
-- Output:
-- category | id_product | name | weight | units
-- молоко и сливки | 11 | Молоко ультрапастеризованное Домик в деревне 0,5%, 950 г | 950.000 | г

-- With product details (optional)
SELECT p.category, p.name, MAX(CAST(p.weight AS real)) AS max_weight
FROM products_data_all AS p
GROUP BY p.category
ORDER BY p.category;
-- Output:
-- category | name | max_weight
-- молоко и сливки | Молоко ультрапастеризованное Домик в деревне 0,5%, 950 г | 950.0
```

## Example Scenario

Given `products_data_all` (partial):

```
id_product | name | category | units | weight | price | date_upd | id_store | name_store
3 | Молоко цельное пастеризованное Ваша Ферма 3,4-6,0%, 1 л | молоко и сливки | л | 1.000 | 69.00 | 2019-06-01 00:00:00 | 0 | Молочные вкусности
11 | Молоко ультрапастеризованное Домик в деревне 0,5%, 950 г | молоко и сливки | г | 950.000 | 99.00 | 2019-06-01 00:00:00 | 0 | Молочные вкусности
17 | Молоко пастеризованное Домик в деревне отборное 3,5-4,5%, 1,4 л | молоко и сливки | л | 1.400 | 139.00 | 2019-06-01 00:00:00 | 0 | Молочные вкусности
18 | Молоко пастеризованное Домик в деревне 2,5%, 1,4 л | молоко и сливки | л | 1.760 | 129.00 | 2019-06-01 00:00:00 | 0 | Молочные вкусности
...
```

The query groups by `category`, finds the maximum weight (950.000 for "молоко и сливки"), and returns:

```
category | max_weight
молоко и сливки | 950.0
```

## Conclusion 🚀

The query successfully calculates the maximum weight per category in `products_data_all`, converting `weight` to a floating-point number and naming the result `max_weight`.

With the sample data, it returns one row for "молоко и сливки" with a maximum weight of 950.0, meeting the task’s requirements.

The implementation is efficient, modular, and extensible, making it ideal for inventory analysis, product weight assessment, or teaching SQL aggregation, grouping, and type casting techniques in a retail context.
