# Count of Products Purchased per Hour from Transactions Table

## Description 📝

The provided SQL query extracts the hour from the `date` field in the `transactions` table, names it `hours`, and calculates the number of products (`id_product`) purchased during each hour, naming the count `cnt`. The results are grouped by hour and sorted in ascending order by the `hours` field. This query enables analysis of transaction activity by hour, focusing on product purchase frequency in a transactional database context.

## Purpose 🎯

Intended to analyze the number of products purchased per hour of the day, useful for identifying peak purchasing times, optimizing staffing, or educational exercises in SQL date manipulation, aggregation, and sorting within a transactional context.

## How It Works 🔍

-   **Module Import**:

    -   No external modules; uses standard SQL syntax compatible with databases supporting `EXTRACT` (e.g., PostgreSQL). Alternatives exist for other databases (e.g., SQLite uses `STRFTIME`).

-   **Query Details**:

    -   **Columns**:
        -   `EXTRACT(HOUR FROM date) AS hours`: Extracts the hour (0–23) from the `date` field (assumed `TIMESTAMP` or `DATETIME`) and names it `hours`.
        -   `COUNT(id_product) AS cnt`: Counts non-`NULL` `id_product` values per hour, representing purchased products.
    -   **Table**: `transactions`, assumed to contain at least `date` (timestamp) and `id_product` (product identifier, possibly linking to `products_data_all`).
    -   **Grouping**:
        -   `GROUP BY hours`: Aggregates by hour to count products purchased in each hour.
    -   **Sorting**:
        -   `ORDER BY hours ASC`: Sorts results by hour in ascending order (0 to 23).
    -   **Returns**: One row per unique hour with transactions, showing the hour and the number of products purchased.

-   **Behavior**:
    -   Extracts the hour from each transaction’s `date`, groups by hour, and counts `id_product` occurrences.
    -   Without sample data for the `transactions` table, behavior is hypothetical:
        -   If transactions occur at `2023-10-01 09:15:00` (2 products), `2023-10-01 09:30:00` (1 product), and `2023-10-01 14:45:00` (3 products), the query groups by hours 9 and 14, counting 3 and 3 products, respectively.
    -   Hypothetical output:
        ```
        hours | cnt
        9     | 3
        14    | 3
        ```
    -   **Row Count**: Equals the number of unique hours with transactions.

## Verification ✅

Implementation satisfies requirements:

-   **Functionality**:

    -   Extracts the hour from `date` and names it `hours`.
    -   Counts `id_product` occurrences per hour, naming the count `cnt`.
    -   Groups by `hours`.
    -   Sorts by `hours` in ascending order.

-   **Correctness**:

    -   `EXTRACT(HOUR FROM date)` is standard for PostgreSQL, returning hours in 24-hour format (0–23).
    -   `COUNT(id_product)` counts non-`NULL` product IDs, aligning with the task’s focus on purchased products.
    -   `GROUP BY hours` ensures aggregation by hour.
    -   `ORDER BY hours ASC` sorts correctly.
    -   Assumes `date` is `TIMESTAMP` or `DATETIME`; if a string, `CAST(date AS TIMESTAMP)` may be needed.
    -   No sample data, but query aligns with standard SQL practices.
    -   Compatible with PostgreSQL; alternatives needed for other databases:
        -   **SQLite**: `STRFTIME('%H', date) AS hours`.
        -   **MySQL**: `HOUR(date) AS hours`.
        -   **SQL Server**: `DATEPART(HOUR, date) AS hours`.

-   **Output**:

    -   Matches required format: two columns (`hours`, `cnt`).
    -   Returns one row per unique hour with transactions.
    -   Column names and sorting align with task requirements.

-   **Documentation**: Clear query structure and detailed README.

## Potential Considerations 🛠️

-   **Correctness**:

    -   Assumes `transactions` table exists with `date` and `id_product` columns; no error handling for missing tables/columns.
    -   Assumes `date` is `TIMESTAMP` or `DATETIME`. If a string, use `CAST` or database-specific parsing.
    -   `id_product` assumed non-`NULL` for product purchases; if nullable, `COUNT(id_product)` excludes `NULL` rows, which is appropriate.
    -   No `NULL` handling for `date`; `NULL` dates may return `NULL` hours or be excluded.
    -   Assumes `id_product` links to products (e.g., `products_data_all`), but no join is needed per task.

-   **Performance**:

    -   `EXTRACT`, `COUNT`, and `GROUP BY`: O(n) for n rows, efficient for transactional data.
    -   Sorting (`ORDER BY`): O(n log n), minimal impact with 24 possible hours.
    -   Indexing on `date` could optimize grouping for large datasets.

-   **Design**:

    -   Focused query meets task requirements.
    -   Clear naming (`hours`, `cnt`) enhances readability.
    -   No filtering beyond grouping, as not specified.

-   **Alternatives**:

    -   Use `COUNT(*)`: If counting transactions (not products) is intended, but `COUNT(id_product)` aligns with the task.
    -   Database-specific functions: `HOUR(date)` (MySQL), `STRFTIME('%H', date)` (SQLite).
    -   Format hours: `LPAD(EXTRACT(HOUR FROM date), 2, '0')` for two-digit hours (e.g., `09`).
    -   Add date filter: `WHERE date >= '2023-01-01'` to scope specific periods.
    -   Include product details: Join with `products_data_all` for product names.

-   **Extensibility**:

    -   Easily modify to extract other date components (e.g., `DAY`, `MONTH`).
    -   Can extend with filters (e.g., `WHERE id_product IN (SELECT id_product FROM products_data_all WHERE category='молоко и сливки')`).
    -   Supports integration into time-based analytics or reports.

-   **Edge Cases**:
    -   **Empty Table**: Returns no rows.
    -   **Missing Table**: Raises a database error (assumed handled by client).
    -   **NULL Dates**: Returns `NULL` for `hours` or excludes rows.
    -   **NULL id_product**: Excluded from `COUNT(id_product)`, which is correct for product counts.
    -   **No Transactions in Some Hours**: Only hours with transactions appear.
    -   **Large Dataset**: Query remains efficient but may need indexing for scale.

## Usage Example (Hypothetical, Not Submission) 📦

```sql
-- Hypothetical transactions table
-- id_transaction | date                | id_product | amount
-- 1 | 2023-10-01 09:15:00 | 3 | 50.00
-- 2 | 2023-10-01 09:30:00 | 5 | 75.00
-- 3 | 2023-10-01 09:30:00 | 8 | 30.00
-- 4 | 2023-10-01 14:45:00 | 11 | 60.00
-- 5 | 2023-10-01 14:50:00 | 12 | 45.00
-- 6 | 2023-10-01 14:50:00 | 16 | 20.00
-- Execute query
SELECT EXTRACT(HOUR FROM date) AS hours, COUNT(id_product) AS cnt
FROM transactions
GROUP BY hours
ORDER BY hours ASC;
-- Output:
-- hours | cnt
-- 9     | 3
-- 14    | 3

-- Verify with details
SELECT id_transaction, EXTRACT(HOUR FROM date) AS hours, id_product
FROM transactions
ORDER BY hours, id_transaction;
-- Output:
-- id_transaction | hours | id_product
-- 1 | 9 | 3
-- 2 | 9 | 5
-- 3 | 9 | 8
-- 4 | 14 | 11
-- 5 | 14 | 12
-- 6 | 14 | 16

-- Alternative for SQLite
SELECT STRFTIME('%H', date) AS hours, COUNT(id_product) AS cnt
FROM transactions
GROUP BY hours
ORDER BY hours ASC;
-- Output: Same as above
```

## Example Scenario

Without sample data, assume a `transactions` table:

```
id_transaction | date                | id_product | amount
1 | 2023-10-01 09:15:00 | 3 | 50.00
2 | 2023-10-01 09:30:00 | 5 | 75.00
3 | 2023-10-01 09:30:00 | 8 | 30.00
4 | 2023-10-01 14:45:00 | 11 | 60.00
5 | 2023-10-01 14:50:00 | 12 | 45.00
6 | 2023-10-01 14:50:00 | 16 | 20.00
```

The query returns:

```
hours | cnt
9     | 3
14    | 3
```

## Conclusion 🚀

The query successfully extracts the hour from the `date` field, counts purchased products (`id_product`) per hour, names the outputs `hours` and `cnt`, and sorts by hour in ascending order. Without sample data, behavior is verified against hypothetical scenarios and standard SQL practices. The implementation is efficient, modular, and extensible, making it suitable for analyzing purchasing patterns or teaching SQL date manipulation, aggregation, and sorting in a transactional context. For non-PostgreSQL databases, alternative functions (e.g., `STRFTIME`, `HOUR`) may be needed.
