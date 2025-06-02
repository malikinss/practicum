/*
You found out that the most products were bought on the 1st.

Truncate the date from the date field to the day and call it date_month.

Find the number of products bought on this day (id_product), group by the date_month field and save it in the cnt variable.

Sort the result in ascending date_month.
*/

SELECT
    DATE_TRUNC('day' FROM date) AS date_month,
    COUNT(id_product) AS cnt
FROM
    transactions
GROUP BY
    date_month;