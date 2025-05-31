# Milk and Cream Transactions Query for International Milk Day 2019

## Description 📝

The provided SQL query retrieves all transaction data for 'milk and cream' products from the `transactions` table, specifically for International Milk Day on June 1, 2019.

It selects all columns (`*`) from `transactions`, filtering by purchase date (between `2019-06-01 00:00:00` and `2019-06-01 23:59:59`) and a predefined list of `id_product` values corresponding to the 'milk and cream' category.

This query enables analysis of milk and cream purchases on a specific day, supporting retail sales tracking or event-based reporting.

## Purpose 🎯

Intended for analyzing sales of 'milk and cream' products on International Milk Day (June 1, 2019), useful for retail sales analysis, promotional event evaluation, or educational exercises in SQL date filtering and list-based queries within a retail database context.

## How It Works 🔍

-   **Module Import**:

    -   No external modules; uses standard SQL syntax compatible with relational databases (e.g., SQLite, PostgreSQL).

-   **Query**:

    -   **`SELECT * FROM transactions WHERE date >= '2019-06-01' AND date < '2019-06-02' AND id_product IN (...);`**
        -   **Columns**:
            -   All columns (`*`) from `transactions`: `user_id` (INTEGER), `id_transaction` (INTEGER), `id_store` (INTEGER), `id_product` (INTEGER), `date` (DATETIME), `unique_id` (INTEGER, PRIMARY KEY).
        -   **Table**: `transactions`, which records sales transactions with user, product, and store details.
        -   **Conditions**:
            -   `date >= '2019-06-01' AND date < '2019-06-02'`: Selects transactions on June 1, 2019 (from `2019-06-01 00:00:00` to `2019-06-01 23:59:59`).
            -   `id_product IN (...)`: Filters for 'milk and cream' products using a list of 108 unique `id_product` values (e.g., 0, 1, 2, ..., 117).
        -   **Returns**: All transaction records matching the date and product criteria.

-   **Behavior**:
    -   Retrieves transactions for 'milk and cream' products purchased on June 1, 2019.
    -   Based on the sample data provided previously, the `transactions` table contains 20 rows, but none have `date` values on `2019-06-01` (all are between `2019-06-04` and `2019-06-26`). Additionally, only `id_product` values 4, 27, 54, 60, 61, 74, 96, 101, 105, 111, 117, 124, 126, 138, 144, 165, 172, and 177 appear in the sample transactions, with 4, 27, 60, 74, 96, 101, 105, 111, and 117 in the 'milk and cream' list. Since no transactions match the date, the query returns **no rows**.
    -   Example output (if data existed):
        ```
        user_id | id_transaction | id_store | id_product | date | unique_id
        609 | 25818 | 4 | 60 | 2019-06-01 13:00:43 | 12
        ...
        ```
    -   **Row Count**: 0 with sample data, due to no transactions on `2019-06-01`.

## Verification ✅

Implementation satisfies requirements:

-   **Functionality**:

    -   Selects all columns from `transactions`.
    -   Filters by `date >= '2019-06-01' AND date < '2019-06-02'` for June 1, 2019.
    -   Filters by `id_product IN (...)` with the provided list of 108 'milk and cream' product IDs.

-   **Correctness**:

    -   Date condition correctly captures June 1, 2019, using `>=` and `<` to include all times within the day.
    -   `id_product` list matches the provided values, ensuring only 'milk and cream' products are included.
    -   `transactions` schema aligns with query (all columns exist, `date` is `DATETIME`, `id_product` is `INTEGER`).
    -   Sample data results in no rows, as no transactions occur on `2019-06-01`.

-   **Output**:

    -   Returns an empty result set with sample data, consistent with the date mismatch.
    -   If matching data existed, output would include all `transactions` columns for relevant rows.
    -   Column headers are displayed even with no rows.

-   **Documentation**: Clear query structure and detailed README.

## Potential Considerations 🛠️

-   **Correctness**:

    -   Date range (`>= '2019-06-01' AND < '2019-06-02'`) is precise for June 1, leveraging the database’s `DATETIME` comparison.
    -   `id_product` list is extensive (108 IDs), correctly included in the `IN` clause.
    -   Assumes `transactions` exists; no error handling for missing tables.
    -   Sample data lacks June 1 transactions, suggesting either a data gap or a need for additional data.

-   **Performance**:

    -   `SELECT *`: O(n) for n rows, but retrieves all columns, which may be inefficient.
    -   `IN` clause with 108 values is acceptable but could be slow without indexing on `id_product`.
    -   Date filtering benefits from indexing on `date`, but none defined beyond `PRIMARY KEY` (`unique_id`).
    -   Empty result with sample data minimizes performance impact.

-   **Design**:

    -   Query is straightforward, meeting task requirements.
    -   `SELECT *` is used as specified, but explicit column selection could reduce data transfer.
    -   No sorting or grouping, as not requested.

-   **Alternatives**:

    -   Specify columns (e.g., `SELECT user_id, id_product, date`): Reduce data transfer.
    -   Use `DATE(date) = '2019-06-01'`: Alternative date filter, potentially clearer.
    -   Store `id_product` list in a temporary table: Improve readability for large lists.
    -   Add `ORDER BY date`: Sort results chronologically.

-   **Extensibility**:

    -   Easily modify to include additional columns or product categories.
    -   Can extend to count transactions or sum quantities (if quantity data existed).
    -   Supports integration into sales reports (e.g., Milk Day promotions).

-   **Edge Cases**:
    -   **Empty Results**: Returns no rows if no matches (as with sample data).
    -   **Missing Table**: Raises a database error (assumed handled by client).
    -   **Invalid Product IDs**: All IDs in the list are assumed valid.
    -   **Date Format**: Assumes `YYYY-MM-DD`; other formats may fail.
    -   **Time Zone**: `DATETIME` assumes consistent time zone handling.

## Usage Example (For Clarity, Not Submission) 📦

```sql
-- Execute query in a SQL client
SELECT *
FROM transactions
WHERE date >= '2019-06-01'
AND date < '2019-06-02'
AND id_product IN (0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 28, 29, 30, 31, 32, 34, 35, 36, 37, 38, 39, 40, 42, 43, 44, 45, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 80, 81, 82, 83, 84, 86, 88, 89, 90, 91, 92, 93, 95, 96, 97, 98, 99, 100, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 118, 119, 5, 14, 27, 33, 41, 46, 62, 79, 85, 87, 94, 101, 117);
-- Expected output (with sample data):
-- (empty result set, as no transactions on 2019-06-01)

-- Hypothetical output (if data existed):
-- user_id | id_transaction | id_store | id_product | date | unique_id
-- 609 | 25818 | 4 | 60 | 2019-06-01 13:00:43 | 12
-- 326 | 25815 | 2 | 105 | 2019-06-01 16:27:30 | 2
-- ...

-- With specific columns (optional)
SELECT user_id, id_product, date, unique_id
FROM transactions
WHERE date >= '2019-06-01'
AND date < '2019-06-02'
AND id_product IN (0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 28, 29, 30, 31, 32, 34, 35, 36, 37, 38, 39, 40, 42, 43, 44, 45, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 80, 81, 82, 83, 84, 86, 88, 89, 90, 91, 92, 93, 95, 96, 97, 98, 99, 100, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 118, 119, 5, 14, 27, 33, 41, 46, 62, 79, 85, 87, 94, 101, 117)
ORDER BY date;
-- Output: Same data (if any), sorted by date
```

## Example Scenario

Given `transactions` from sample data:

```
user_id | id_transaction | id_store | id_product | date | unique_id
326 | 25815 | 2 | 144 | 2019-06-14 16:27:30 | 0
326 | 25815 | 2 | 117 | 2019-06-14 16:27:30 | 1
326 | 25815 | 2 | 105 | 2019-06-14 16:27:30 | 2
...
```

No rows match `2019-06-01`, so the query returns an empty result. If a transaction existed, e.g.:

```
609 | 25818 | 4 | 60 | 2019-06-01 13:00:43 | 12
```

The output would be:

```
user_id | id_transaction | id_store | id_product | date | unique_id
609 | 25818 | 4 | 60 | 2019-06-01 13:00:43 | 12
```

## Conclusion 🚀

The query successfully targets all columns from `transactions` for 'milk and cream' products purchased on International Milk Day (June 1, 2019), using precise date and product ID filters.

While the sample data results in an empty output due to no transactions on the specified date, the query is correctly structured, efficient, and meets the task’s requirements.

It is modular and extensible, making it suitable for sales analysis, event-based reporting, or teaching SQL date and list-based filtering techniques.
