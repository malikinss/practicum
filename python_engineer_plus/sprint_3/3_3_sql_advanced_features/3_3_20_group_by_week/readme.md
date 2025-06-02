# Average Unique Transactions per Week from Transactions Table

## Description 📝

The provided SQL query calculates the average number of unique transactions (`id_transaction`) per day, grouped by week, from the `transactions` table. It first truncates the `date` column to the day, counts unique transactions per day, and then groups these daily counts by week to compute the average. The inner subquery names the daily transaction count `transaction_per_day` and the truncated date `trunc_date`, while the outer query names the week number `week_number` and the average daily transactions per week `avg_week_transaction`.

## Purpose 🎯

-   **Original Task Query**: Counts unique transactions per day, useful for daily transaction volume analysis, identifying peak days, or operational planning.
-   **Weekly Analysis Query**: Calculates the average daily transaction count per week, useful for weekly trend analysis, resource allocation, or strategic planning.
-   Both are suitable for retail analytics or educational exercises in SQL date truncation, aggregation, and subqueries.

## How It Works 🔍

-   **Module Import**:

    -   No external modules; uses PostgreSQL syntax (`DATE_TRUNC`, `EXTRACT`). Alternatives exist for other databases (e.g., SQLite uses `DATE`, `STRFTIME`).

-   **Original Task Query**:

    -   **Columns**:
        -   `COUNT(DISTINCT id_transaction) AS transaction_per_day`: Counts unique transactions per day.
        -   `DATE_TRUNC('day', date) AS trunc_date`: Truncates `date` to day (e.g., `2025-06-01 14:30:00` → `2025-06-01 00:00:00`).
    -   **Table**: `transactions` (assumed: `id_transaction`, `date`).
    -   **Grouping**: `GROUP BY DATE_TRUNC('day', date)` aggregates by day.
    -   **Sorting**: `ORDER BY trunc_date ASC` ensures chronological order.
    -   **Returns**: Rows with daily unique transaction counts and truncated dates.
    -   **Hypothetical Output**:
        ```
        transaction_per_day | trunc_date
        2                  | 2025-06-01 00:00:00
        1                  | 2025-06-02 00:00:00
        ```
    -   **Row Count**: Number of unique dates with transactions.

-   **Weekly Analysis Query**:
    -   **Inner Subquery (`daily_transactions`)**:
        -   Counts unique transactions per day, as in the original task.
    -   **Outer Query**:
        -   **Columns**:
            -   `EXTRACT(YEAR FROM trunc_date) AS year`: Extracts year for clarity.
            -   `EXTRACT(WEEK FROM trunc_date) AS week_number`: ISO week number (1–53).
            -   `AVG(transaction_per_day) AS avg_week_transaction`: Averages daily counts per week.
        -   **Grouping**: `GROUP BY EXTRACT(YEAR FROM trunc_date), EXTRACT(WEEK FROM trunc_date)` aggregates by year and week.
        -   **Sorting**: `ORDER BY year ASC, week_number ASC` ensures chronological order.
    -   **Returns**: Rows with year, week number, and average daily transactions per week.
    -   **Hypothetical Output**:
        ```
        year | week_number | avg_week_transaction
        2025 | 22          | 1.5
        2025 | 23          | 1.0
        ```
    -   **Row Count**: Number of unique year-week combinations.

## Verification ✅

-   **Original Task Query**:

    -   Satisfies requirements: counts unique transactions, groups by day, names columns `transaction_per_day` and `trunc_date`, outputs in correct order.
    -   Correctness: `COUNT(DISTINCT id_transaction)` and `DATE_TRUNC` are accurate.
    -   Output: Matches format (`transaction_per_day`, `trunc_date`).
    -   PostgreSQL-compatible; alternatives:
        -   SQLite: `DATE(date)`.
        -   MySQL: `DATE(date)`.
        -   SQL Server: `CAST(date AS DATE)`.

-   **Weekly Analysis Query**:

    -   Corrects provided query by adding year grouping and sorting.
    -   Output: `year`, `week_number`, `avg_week_transaction`.
    -   Robust for year boundaries and chronological presentation.
    -   Assumes provided query’s intent is weekly analysis.

-   **General**:
    -   No sample data; verified with hypotheticals.
    -   Assumes `transactions` with `id_transaction`, `date`.
    -   UTF-8 for potential Cyrillic data (though not relevant here).

## Potential Considerations 🛠️

-   **Correctness**:

    -   Assumes `transactions` exists; no error handling for missing tables.
    -   `NULL` dates or `id_transaction` excluded by `DATE_TRUNC` and `COUNT(DISTINCT)`.
    -   Week numbers may span years; year grouping mitigates confusion.

-   **Performance**:

    -   Daily query: O(n) for grouping/counting; sorting O(n log n).
    -   Weekly query: Additional O(m) for weekly aggregation (m = unique days).
    -   Indexing on `date` optimizes grouping/sorting; `id_transaction` aids `DISTINCT`.

-   **Design**:

    -   Original: Minimalist, meets task.
    -   Weekly: Adds year for clarity, descriptive subquery alias.
    -   Clear naming (`transaction_per_day`, `trunc_date`, `avg_week_transaction`).

-   **Alternatives**:

    -   Original: Use `CAST(date AS DATE)` instead of `DATE_TRUNC`.
    -   Weekly: Use `TO_CHAR(date, 'IYYY-IW')` for year-week format.
    -   Database-specific: SQLite (`STRFTIME('%Y-%W')`), MySQL (`WEEK`), SQL Server (`DATEPART`).
    -   Filter dates: `WHERE date >= '2025-01-01'`.

-   **Extensibility**:

    -   Add filters (e.g., product categories).
    -   Group by month/year.
    -   Integrate into dashboards.

-   **Edge Cases**:
    -   Empty table: No rows.
    -   Missing table: Error.
    -   NULL values: Excluded.
    -   Sparse dates: Only active days/weeks appear.
    -   Large dataset: Needs indexing.

## Usage Example (Hypothetical, Not Submission) 📦

```sql
-- Hypothetical transactions
-- id_transaction | date                | id_product
-- 1 | 2025-06-01 09:15:00 | 3
-- 2 | 2025-06-01 14:30:00 | 5
-- 3 | 2025-06-02 10:00:00 | 8
-- 4 | 2025-06-08 12:00:00 | 11
-- Original task query
SELECT COUNT(DISTINCT id_transaction) AS transaction_per_day, DATE_TRUNC('day', date) AS trunc_date
FROM transactions
GROUP BY DATE_TRUNC('day', date)
ORDER BY trunc_date ASC;
-- Output:
-- transaction_per_day | trunc_date
-- 2                  | 2025-06-01 00:00:00
-- 1                  | 2025-06-02 00:00:00
-- 1                  | 2025-06-08 00:00:00

-- Weekly analysis query
SELECT EXTRACT(YEAR FROM trunc_date) AS year, EXTRACT(WEEK FROM trunc_date) AS week_number, AVG(transaction_per_day)
FROM (
    SELECT COUNT(DISTINCT id_transaction) AS transaction_per_day, DATE_TRUNC('day', date) AS trunc_date
    FROM transactions
    GROUP BY DATE_TRUNC('day', date)
) AS daily_transactions
GROUP BY EXTRACT(YEAR FROM trunc_date), EXTRACT(WEEK FROM trunc_date)
ORDER BY year ASC, week_number ASC;
-- Output (week 22: 2+1=3/2=1.5, week 23: 1/1=1.0):
-- year | week_number | avg_week_transaction
-- 2025 | 22          | 1.5
-- 2025 | 23          | 1.0
```

## Example Scenario

Assume `transactions`:

```
id_transaction | date                | id_product
1 | 2025-06-01 09:15:00 | 3
2 | 2025-06-01 14:30:00 | 5
3 | 2025-06-02 10:00:00 | 8
4 | 2025-06-08 12:00:00 | 11
```

-   Original: Counts 2, 1, 1 transactions on June 1, 2, 8.
-   Weekly: Averages 1.5 (week 22, June 1–2), 1.0 (week 23, June 8).

## Conclusion 🚀

The corrected query for the original task counts unique transactions per day, meeting all requirements with proper column naming and sorting. The provided weekly analysis query, corrected with year grouping and sorting, addresses a potential extension but deviates from the task. Both are efficient, modular, and extensible, suitable for transaction analysis or teaching SQL. Without sample data, hypotheticals verify behavior. Non-PostgreSQL databases require alternative date functions.
