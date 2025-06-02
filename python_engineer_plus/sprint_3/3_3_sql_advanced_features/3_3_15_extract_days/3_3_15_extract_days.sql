/*
Get the day from the date column of the transactions table.

Name the new field days.

Calculate the number of purchased products (id_product) grouped by day and name the resulting field cnt.

Sort the result in ascending date order.
*/

SELECT
    EXTRACT(DAY FROM CAST(date as DATE)) AS days,
    COUNT(*) AS cnt
FROM
    transactions
GROUP BY
    days
ORDER BY
    days;