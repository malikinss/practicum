# Top 5 Most Expensive Products

## Description 📝

The provided SQL query aims to retrieve the top 5 most expensive products from the `products_data_all` table, selecting the product name (`name`) and its price, named `max_price`.
The results are intended to be sorted in descending order by price.

## Purpose 🎯

Intended to identify the 5 most expensive products by price, displaying their names and prices, useful for retail pricing analysis, product positioning, or educational exercises in SQL sorting and limiting within a retail context.

## How It Works 🔍

-   **Module Import**:

    -   No external modules; uses standard SQL syntax compatible with relational databases (e.g., SQLite, PostgreSQL).

-   **Query Details**:

    -   **Columns**:
        -   `name` (VARCHAR(255)): Product name from `products_data_all`.
        -   `CAST(price AS REAL) AS max_price`: Product price (DECIMAL(10,2)) converted to a floating-point number, named `max_price`.
    -   **Table**: `products_data_all`, containing product details (`id_product`, `name`, `category`, `units`, `weight`, `price`, `date_upd`, `id_store`, `name_store`).
    -   **Sorting**:
        -   `ORDER BY max_price DESC`: Sorts products by price in descending order (highest first).
    -   **Limit**:
        -   `LIMIT 5`: Restricts output to the top 5 rows.
    -   **Returns**: Up to 5 rows with product names and their prices, sorted from most to least expensive.

-   **Behavior**:
    -   Selects all products, sorts by price in descending order, and returns the top 5.
    -   Based on the sample data:
        -   `products_data_all`: 20 rows with unique `id_product` and `name`.
        -   `price` values: 69.00, 78.00, 76.01, 49.00, 99.00, 23.00, 139.00, 129.00, 84.00, 24.00, 84.00, 45.00, 72.00, 89.00, 79.00, 149.00, 75.00, 149.00, 72.99, 99.00.
        -   Top 5 prices: 149.00 (twice), 139.00, 129.00, 99.00 (twice, but we select top 5 rows).
        -   Corresponding products:
            -   `id_product=25`, `name="Молоко ультрапастеризованное Простоквашино 3,2%, 950 мл"`, `price=149.00`.
            -   `id_product=35`, `name="Молоко ультрапастеризованное Parmalat Comfort 3,5%, 1 л"`, `price=149.00`.
            -   `id_product=17`, `name="Молоко пастеризованное Домик в деревне отборное 3,5-4,5%, 1,4 л"`, `price=139.00`.
            -   `id_product=18`, `name="Молоко пастеризованное Домик в деревне 2,5%, 1,4 л"`, `price=129.00`.
            -   `id_product=11`, `name="Молоко ультрапастеризованное Домик в деревне 0,5%, 551 г"`, `price=99.00`.
    -   Output:
        ```
        name | max_price
        Молоко ультрапастеризованное Простоквашино 3,2%, 950 мл | 149.0
        Молоко ультрапастеризованное Parmalat Comfort 3,5%, 1 л | 149.0
        Молоко пастеризованное Домик в деревне отборное 3,5-4,5%, 1,4 л | 139.0
        Молоко пастеризованное Домик в деревне 2,5%, 1,4 л | 129.0
        Молоко ультрапастеризованное Домик в деревне 0,5%, 551 г | 99.0
        ```
    -   **Row Count**: 5 rows.

## Verification ✅

Implementation satisfies requirements:

-   **Functionality**:

    -   Selects `name` and `price` (as `max_price`).
    -   Returns the top 5 most expensive products.
    -   Sorts by `max_price` in descending order.

-   **Correctness**:

    -   `CAST(price AS REAL)` ensures floating-point output for `price` (DECIMAL(10,2)).
    -   `ORDER BY max_price DESC` correctly sorts by price.
    -   `LIMIT 5` restricts to the top 5 rows.
    -   Sample data yields 5 products with prices 149.0, 149.0, 139.0, 129.0, 99.0, matching the highest prices.
    -   Cyrillic `name` requires UTF-8 encoding.

-   **Output**:

    -   Matches required format: two columns (`name`, `max_price`).
    -   Returns 5 rows, sorted by price in descending order.
    -   Column names and values align with task requirements.

-   **Documentation**: Clear query structure and detailed README.

## Potential Considerations 🛠️

-   **Correctness**:

    -   Assumes `products_data_all` exists; no error handling for missing tables.
    -   `price` is non-`NULL` in sample data, ensuring valid sorting.
    -   Assumes `name` is unique per product; if not, `DISTINCT ON (name, id_product)` or filtering may be needed.
    -   Ties in prices (e.g., two at 149.0) are resolved arbitrarily by row order; additional sorting (e.g., `ORDER BY max_price DESC, name`) could standardize.

-   **Performance**:

    -   `ORDER BY` and `LIMIT`: O(n log n) for sorting n rows, efficient for small datasets (20 rows).
    -   `LIMIT 5` minimizes data transfer.
    -   Indexing on `price` could optimize sorting for large datasets.

-   **Design**:

    -   Corrected query removes unnecessary `MAX` and `GROUP BY`.
    -   `CAST(price AS REAL)` aligns with sample data precision.
    -   Clear variable naming (`max_price`) enhances readability.

-   **Alternatives**:

    -   Omit `CAST`: `price AS max_price` works for `DECIMAL`, but floating-point output is ensured by `CAST`.
    -   Use `DISTINCT`: `SELECT DISTINCT name, price` to avoid duplicates if multiple entries exist (not needed with sample data).
    -   Add tie-breaker: `ORDER BY max_price DESC, name` for consistent ordering of equal prices.
    -   Filter by date: Add `WHERE date_upd = '2019-06-01'` to scope specific dates.

-   **Extensibility**:

    -   Easily modify to include additional columns (e.g., `category`, `id_product`).
    -   Can extend with filters (e.g., `WHERE category='молоко и сливки'`).
    -   Supports integration into pricing reports or dashboards.

-   **Edge Cases**:
    -   **Fewer Than 5 Products**: Returns all available rows (not applicable with 20 rows).
    -   **Empty Table**: Returns no rows.
    -   **Missing Table**: Raises a database error (assumed handled by client).
    -   **NULL Prices**: Excluded from top results (none in sample data).
    -   **Large Dataset**: Query remains efficient but may need indexing for scale.

## Usage Example (For Clarity, Not Submission) 📦

```sql
-- Execute corrected query
SELECT name, CAST(price AS REAL) AS max_price
FROM products_data_all
ORDER BY max_price DESC
LIMIT 5;
-- Output (based on sample data):
-- name | max_price
-- Молоко ультрапастеризованное Простоквашино 3,2%, 950 мл | 149.0
-- Молоко ультрапастеризованное Parmalat Comfort 3,5%, 1 л | 149.0
-- Молоко пастеризованное Домик в деревне отборное 3,5-4,5%, 1,4 л | 139.0
-- Молоко пастеризованное Домик в деревне 2,5%, 1,4 л | 129.0
-- Молоко ультрапастеризованное Домик в деревне 0,5%, 551 г | 99.0

-- Verify data
SELECT name, price
FROM products_data_all
ORDER BY price DESC
LIMIT 10;
-- Output: Confirms top 5 prices and products

-- With tie-breaker (optional)
SELECT name, CAST(price AS REAL) AS max_price
FROM products_data_all
ORDER BY max_price DESC, name ASC
LIMIT 5;
-- Output: Same data, with alphabetical ordering for ties (e.g., 149.0)
```

## Example Scenario

Given `products_data_all` (partial):

```
id_product | name | category | units | weight | price | date_upd | id_store | name_store
25 | Молоко ультрапастеризованное Простоквашино 3,2%, 950 мл | молоко и сливки | мл | 925.000 | 149.00 | 2019-06-01 00:00:00 | 0 | Молочные вкусности
35 | Молоко ультрапастеризованное Parmalat Comfort 3,5%, 1 л | молоко и сливки | л | 1.000 | 149.00 | 2019-06-01 00:00:00 | 0 | Молочные вкусности
17 | Молоко пастеризованное Домик в деревне отборное 3,5-4,5%, 1,4 л | молоко и сливки | л | 1.400 | 139.00 | 2019-06-01 00:00:00 | 200 | Молочные вкусности
18 | Молоко пастеризованное Домик в деревне 2,5%, 1,4 л | молоко и сливки | л | 1.760 | 129.00 | 2019-06-01 00:00:00 | 200 | Молочные вкусности
11 | Молоко ультрапастеризованное Домик в деревне 0,5%, 551 г | молоко и сливки | г | 551.000 | 99.00 | 2019-06-01 00:00:00 | 0 | Молочные вкусности
...
```

The query returns:

```
name | max_price
Молоко ультрапастеризованное Простоквашино 3,2%, 950 мл | 149.0
Молоко ультрапастеризованное Parmalat Comfort 3,5%, 1 л | 149.0
Молоко пастеризованное Домик в деревне отборное 3,5-4,5%, 1,4 л | 139.0
Молоко пастеризованное Домик в деревне 2,5%, 1,4 л | 129.0
Молоко ультрапастеризованное Домик в деревне 0,5%, 551 г | 99.0
```

## Conclusion 🚀

The corrected query successfully retrieves the top 5 most expensive products from `products_data_all`, naming the price variable `max_price` and sorting in descending order.

With the sample data, it returns 5 products with prices 149.0, 149.0, 139.0, 129.0, and 99.0, meeting the task’s requirements.

The implementation is efficient, modular, and extensible, making it ideal for pricing analysis, product positioning, or teaching SQL sorting and limiting techniques in a retail context.
