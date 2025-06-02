# Maximum Price for Expensive Products (>500 Rubles)

## Description 📝

The provided SQL query calculates the maximum price for each product in the `products_data_all` table, names the result `max_price`, and filters for products with a maximum price exceeding 500 rubles. It selects the product name (`name`) and the maximum price, grouping by product name to ensure unique products are considered. This query enables analysis of high-value products in a retail database context.

## Purpose 🎯

Intended for identifying products with maximum prices above 500 rubles, useful for premium product analysis, pricing strategy, or educational exercises in SQL aggregation, grouping, and filtering within a retail environment.

## How It Works 🔍

-   **Module Import**:

    -   No external modules; uses standard SQL syntax compatible with relational databases (e.g., SQLite, PostgreSQL).

-   **Query**:

    -   **`SELECT name, MAX(CAST(price AS REAL)) AS max_price FROM products_data_all GROUP BY name HAVING max_price > 500;`**
        -   **Columns**:
            -   `name` (VARCHAR(255)): Product name from `products_data_all`.
            -   `MAX(CAST(price AS REAL)) AS max_price`: Maximum price per product, with `price` (DECIMAL(10,2)) converted to a floating-point number (`REAL`).
        -   **Table**: `products_data_all`, containing product details (`id_product`, `name`, `category`, `units`, `weight`, `price`, `date_upd`, `id_store`, `name_store`).
        -   **Grouping**:
            -   `GROUP BY name`: Aggregates by product name to compute the maximum price for each unique product.
        -   **Condition**:
            -   `HAVING max_price > 500`: Filters groups (products) where the maximum price exceeds 500 rubles.
        -   **Returns**: Rows with product names and their maximum prices, only for products with `max_price > 500`.

-   **Behavior**:
    -   Groups rows by `name`, calculates the maximum `price` for each product, and filters for those above 500 rubles.
    -   Based on the sample data:
        -   `products_data_all`: 20 rows with unique `id_product` and `name`.
        -   `price` values: 69.00, 78.00, 76.01, 49.00, 99.00, 23.00, 139.00, 129.00, 84.00, 24.00, 84.00, 45.00, 72.00, 89.00, 79.00, 149.00, 75.00, 149.00, 72.99, 99.00.
        -   Maximum price per product: Since each product appears once (unique `name` and `id_product`), the `MAX(price)` equals the listed price.
        -   Highest prices: 149.00 (two products), 139.00, 129.00, 99.00 (two products).
        -   No prices exceed 500 rubles.
    -   Output:
        ```
        (empty result set)
        ```
    -   **Row Count**: 0 rows, as no products have a maximum price > 500 rubles.

## Verification ✅

Implementation satisfies requirements:

-   **Functionality**:

    -   Selects `name` and maximum `price` (as `max_price`).
    -   Groups by `name` to compute maximum price per product.
    -   Filters for `max_price > 500` using `HAVING`.

-   **Correctness**:

    -   `CAST(price AS REAL)` ensures floating-point output for `price` (DECIMAL(10,2)).
    -   `GROUP BY name` correctly aggregates by product, though each `name` is unique in sample data.
    -   `HAVING max_price > 500` filters post-aggregation, correctly excluding all products (none exceed 500).
    -   Sample data confirms no prices above 149.00, so empty result is accurate.
    -   Cyrillic `name` requires UTF-8 encoding.

-   **Output**:

    -   Matches required format: two columns (`name`, `max_price`).
    -   Returns 0 rows, as expected with sample data.
    -   Column names and structure align with task requirements.

-   **Documentation**: Clear query structure and detailed README.

## Potential Considerations 🛠️

-   **Correctness**:

    -   Assumes `products_data_all` exists; no error handling for missing tables.
    -   `price` is non-`NULL` in sample data, ensuring valid `MAX` calculations.
    -   Each product has a unique `name` in sample data, making `GROUP BY name` equivalent to grouping by `id_product`.
    -   If multiple entries exist per product (e.g., across stores or dates), `MAX(price)` correctly selects the highest price.
    -   No prices exceed 500 rubles in sample data, possibly indicating a data limitation or currency misunderstanding (e.g., rubles vs. another unit).

-   **Performance**:

    -   `MAX` and `GROUP BY`: O(n) for n rows, efficient for small datasets (20 rows).
    -   `HAVING` filter is applied post-grouping, minimizing result size.
    -   Indexing on `name` or `price` could optimize for large datasets.

-   **Design**:

    -   `CAST(price AS REAL)` ensures floating-point output, though `DECIMAL` is precise.
    -   `HAVING` is appropriate for filtering aggregated results.
    -   Query is focused and meets task requirements.

-   **Alternatives**:

    -   Omit `CAST`: `MAX(price)` works for `DECIMAL`, but floating-point output is ensured by `CAST`.
    -   Use `id_product` in `GROUP BY`: If `name` isn’t guaranteed unique, `GROUP BY id_product, name` ensures accuracy.
    -   Add `ORDER BY max_price DESC`: Not required but could clarify ranking (though empty result makes it moot).
    -   Lower threshold: Adjust `HAVING max_price > 100` to return results with sample data.

-   **Extensibility**:

    -   Easily modify to include other columns (e.g., `category`, `id_product`).
    -   Can extend with filters (e.g., `WHERE date_upd = '2019-06-01'`).
    -   Supports integration into pricing reports or dashboards.

-   **Edge Cases**:
    -   **No Matching Rows**: Returns no rows (as with sample data).
    -   **Empty Table**: Returns no rows.
    -   **Missing Table**: Raises a database error (assumed handled by client).
    -   **NULL Prices**: `MAX` ignores `NULL` (none in sample data).
    -   **Large Dataset**: Query remains efficient but may need indexing for scale.

## Usage Example (For Clarity, Not Submission) 📦

```sql
-- Execute query
SELECT name, MAX(CAST(price AS REAL)) AS max_price
FROM products_data_all
GROUP BY name
HAVING max_price > 500;
-- Output (based on sample data):
-- (empty result set)

-- Verify data
SELECT name, price
FROM products_data_all
ORDER BY price DESC;
-- Output: Shows highest prices (149.00, 139.00, etc.), none above 500

-- Hypothetical example with matching data
-- Assume data:
-- id_product | name | price | ...
-- 101 | Premium Milk A | 600.00 | ...
-- 102 | Premium Milk A | 550.00 | ...
-- 103 | Luxury Butter B | 700.00 | ...
SELECT name, MAX(CAST(price AS REAL)) AS max_price
FROM products_data_all
GROUP BY name
HAVING max_price > 500;
-- Output:
-- name | max_price
-- Premium Milk A | 600.0
-- Luxury Butter B | 700.0
```

## Example Scenario

Given `products_data_all` (partial):

```
id_product | name | category | units | weight | price | date_upd | id_store | name_store
25 | Молоко ультрапастеризованное Простоквашино 3,2%, 950 мл | молоко и сливки | мл | 925.000 | 149.00 | 2019-06-01 00:00:00 | 0 | Молочные вкусности
35 | Молоко ультрапастеризованное Parmalat Comfort 3,5%, 1 л | молоко и сливки | л | 1.000 | 149.00 | 2019-06-01 00:00:00 | 0 | Молочные вкусности
17 | Молоко пастеризованное Домик в деревне отборное 3,5-4,5%, 1,4 л | молоко и сливки | л | 1.400 | 139.00 | 2019-06-01 00:00:00 | 200 | Молочные вкусности
...
```

No products have a price above 500 rubles, so the query returns:

```
(empty result set)
```

## Conclusion 🚀

The query successfully calculates the maximum price for each product, naming the variable `max_price`, and filters for products costing more than 500 rubles. With the sample data, it returns an empty result set, as no products exceed 500 rubles, which is correct given the data. The implementation is efficient, modular, and extensible, making it suitable for premium product analysis, pricing strategy, or teaching SQL aggregation and filtering techniques in a retail context.
