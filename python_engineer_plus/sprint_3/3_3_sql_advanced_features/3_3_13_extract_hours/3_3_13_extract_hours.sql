/*
Get hours from the date field of the transactions table.
Name the new field hours.
*/

SELECT
    EXTRACT(HOUR FROM date) AS hours
FROM
    transactions;