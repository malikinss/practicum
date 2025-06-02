/*
Get hours from the date field of the transactions table.

Name the new field hours.

Calculate, grouped by the hours field, how many products (id_product) were purchased.

Name the resulting variable cnt.

Sort the result in ascending order of the hours field.
*/

SELECT
    EXTRACT(HOUR FROM date) AS hours
    COUNT(id_product) AS cnt
FROM
    transactions
GROUP BY
    hours
ORDER BY
    hours;