/*
Write a query to count the number of unique transactions id_transaction from the transactions table.

Group the transaction count by day: truncate the date column to the day.

Name the generated column with transactions transaction_per_day, and the truncated date trunc_date.

Output the columns in this order: first transaction_per_day, then trunc_date.
*/

SELECT
    EXTRACT(WEEK FROM trunc_date) AS week_number,
    AVG(transaction_per_day) AS avg_week_transaction
FROM
    (
    SELECT
        COUNT(DISTINCT id_transaction) AS transaction_per_day,
        DATE_TRUNC('day', date) AS trunc_date
    FROM
        transactions
    GROUP BY
        trunc_date
    ) AS SUBQ
GROUP BY
    week_number;
