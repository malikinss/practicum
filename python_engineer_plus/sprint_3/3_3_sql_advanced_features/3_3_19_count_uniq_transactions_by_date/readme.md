# Count of Unique Transactions per Day from Transactions Table

## Description 📝

The provided SQL query aims to count the number of unique transactions (`id_transaction`) from the `transactions` table, grouped by day, with the `date` column truncated to the day. The transaction count is named `transaction_per_day`, and the truncated date is named `trunc_date`. The results are output with `transaction_per_day` first, followed by `trunc_date`. The query is intended to analyze daily transaction volumes.

## Purpose 🎯

Intended to count unique transactions per day, useful for analyzing daily transaction volumes, identifying peak days, or supporting operational planning. Suitable for retail analytics or educational exercises in SQL date truncation, aggregation, and sorting.

## How It Works 🔍

-   **Module Import**:

    -   No external modules; uses PostgreSQL SQL syntax (`DATE_TRUNC`). Alternatives exist for other databases.

-   **Query Details**:

    -   **Columns**:
        -   `COUNT(DISTINCT id_transaction) AS transaction_per_day`: Counts unique `id_transaction` values per day.
        -   `DATE_TRUNC('day', date) AS trunc_date`: Truncates `date` (assumed TIMESTAMP) to the day (e.g., `2025-06-01 14:30:00` → `2025-06-01 00:00:00`).
    -   **Table**: `transactions`, assumed to contain `id_transaction` (INTEGER) and `date` (TIMESTAMP).
    -   **Grouping**:
        -   `GROUP BY DATE_TRUNC('day', date)`: Aggregates by truncated date to count transactions per day.
    -   **Sorting**:
        -   `ORDER BY trunc_date ASC`: Sorts results chronologically by truncated date.
    -   **Returns**: One row per unique date, with the count of unique transactions and the truncated date.

-   **Behavior**:
    -   Truncates `date` to day, groups by day, counts unique `id_transaction` values, and sorts by date.
    -   Without sample data, hypothetical example:
        -   Transactions on `2025-06-01 09:15:00` (ID 1), `2025-06-01 14:30:00` (ID 2), `2025-06-02 10:00:00` (ID 3) yield:
            ```
            transaction_per_day | trunc_date
            2                  | 2025-06-01 00:00:00
            1                  | 2025-06-02 00:00:00
            ```
    -   **Row Count**: Equals the number of unique dates with transactions.

## Verification ✅

Implementation satisfies requirements:

-   **Functionality**:

    -   Counts unique `id_transaction` values, named `transaction_per_day`.
    -   Truncates `date` to day, named `trunc_date`.
    -   Groups by truncated date.
    -   Outputs `transaction_per_day`, then `trunc_date`.

-   **Correctness**:

    -   `COUNT(DISTINCT id_transaction)` ensures unique transaction counts.
    -   `DATE_TRUNC('day', date)` correctly truncates to day in PostgreSQL.
    -   `GROUP BY DATE_TRUNC('day', date)` aligns with truncation.
    -   `ORDER BY trunc_date ASC` ensures chronological order.
    -   Assumes `date` is TIMESTAMP; if not, `CAST(date AS TIMESTAMP)` may be needed.
    -   No sample data, but aligns with standard SQL practices.
    -   PostgreSQL-compatible; alternatives:
        -   **SQLite**: `DATE(date) AS trunc_date`.
        -   **MySQL**: `DATE(date) AS trunc_date`.
        -   **SQL Server**: `CAST(date AS DATE) AS trunc_date`.

-   **Output**:

    -   Matches required format: `transaction_per_day`, `trunc_date`.
    -   One row per unique date.
    -   Column order and names align with task.

-   **Documentation**: Clear query structure and detailed README.

## Potential Considerations 🛠️

-   **Correctness**:

    -   Assumes `transactions` exists with `id_transaction` and `date`; no error handling for missing tables/columns.
    -   Assumes `id_transaction` is unique per transaction; `DISTINCT` ensures robustness.
    -   `NULL` dates are excluded by `DATE_TRUNC`; `NULL` `id_transaction` excluded by `COUNT(DISTINCT)`.
    -   Table name `transactions` vs. `transactions_data` needs confirmation.

-   **Performance**:

    -   `COUNT(DISTINCT)`, `DATE_TRUNC`, `GROUP BY`: O(n) for n rows, efficient for moderate datasets.
    -   Sorting: O(n log n), minimal impact with limited dates.
    -   Indexing on `date` optimizes grouping/sorting; `id_transaction` index aids `DISTINCT`.

-   **Design**:

    -   Added `ORDER BY` for usability.
    -   Clear naming (`transaction_per_day`, `trunc_date`).
    -   Minimalist query meets requirements.

-   **Alternatives**:

    -   Use `CAST(date AS DATE)`: Simpler than `DATE_TRUNC` for day truncation.
    -   Database-specific functions: `DATE(date)` (MySQL/SQLite), `CAST(date AS DATE)` (SQL Server).
    -   Filter dates: `WHERE date >= '2025-01-01'` for specific periods.
    -   Add details: Include `id_product` counts or customer IDs.

-   **Extensibility**:

    -   Modify to group by week/month (`DATE_TRUNC('week', date)`).
    -   Add filters (e.g., specific products).
    -   Integrate into analytics dashboards.

-   **Edge Cases**:
    -   **Empty Table**: Returns no rows.
    -   **Missing Table**: Raises error.
    -   **NULL Dates**: Excluded.
    -   **NULL id_transaction**: Excluded from count.
    -   **No Transactions on a Day**: Date omitted.
    -   **Large Dataset**: Efficient with indexing.

## Usage Example (Hypothetical, Not Submission) 📦

```sql
-- Hypothetical transactions table
-- id_transaction | date                | id_product | amount
-- 1 | 2025-06-01 09:15:00 | 3 | 50.00
-- 2 | 2025-06-01 14:30:00 | 5 | 75.00
-- 3 | 2025-06-02 10:00:00 | 8 | 30.00
-- Execute corrected query
SELECT COUNT(DISTINCT id_transaction) AS transaction_per_day, DATE_TRUNC('day', date) AS trunc_date
FROM transactions
GROUP BY DATE_TRUNC('day', date)
ORDER BY trunc_date ASC;
-- Output:
-- transaction_per_day | trunc_date
-- 2                  | 2025-06-01 00:00:00
-- 1                  | 2025-06-02 00:00:00

-- Verify with details
SELECT id_transaction, DATE_TRUNC('day', date) AS transaction_date
FROM transactions
ORDER BY transaction_date;
-- Output:
-- id_transaction | transaction_date
-- 1 | 2025-06-01 00:00:00
-- 2 | 2025-06-01 00:00:00
-- 3 | 2025-06-02 00:00:00

-- Alternative for SQLite
SELECT COUNT(DISTINCT id_transaction) AS transaction_per_day, DATE(date) AS trunc_date
FROM transactions
GROUP BY DATE(date)
ORDER BY trunc_date ASC;
-- Output: Same (adjusted format)
```

## Example Scenario

Assume a `transactions` table:

```
id_transaction | date                | id_product | amount
1 | 2025-06-01 09:15:00 | 3 | 50.00
2 | 2025-06-01 14:30:00 | 5 | 75.00
3 | 2025-06-02 10:00:00 | 8 | 30.00
```

The query returns:

```
transaction_per_day | trunc_date
2                  | 2025-06-01 00:00:00
1                  | 2025-06-02 00:00:00
```

## Conclusion 🚀

The corrected query successfully counts unique transactions per day, names the count `transaction_per_day` and the truncated date `trunc_date`, groups by day, and sorts chronologically. Without sample data, behavior is verified with hypothetical scenarios and PostgreSQL practices.

The implementation is efficient, modular, and extensible, suitable for transaction volume analysis or teaching SQL date truncation, aggregation, and sorting.

For non-PostgreSQL databases, alternative date functions are needed.
