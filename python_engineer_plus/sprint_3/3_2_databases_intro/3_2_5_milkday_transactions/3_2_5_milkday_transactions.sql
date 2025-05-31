/*
Find out how much milk and cream was purchased on International Milk Day.

From the `transactions` table, download all data on milk and cream purchases for June 1, 2019.

The `date` field records the time of purchase, and stores data in the "date" format. Write a query to select only sales for June 1.

Please note: the database can compare data in date format as numbers and understands that `2019-06-14 16:27:30 > 2019-05-19 22:28:47`

The `transactions` table does not have informaation about the product category. We have prepared a list with unique identifiers (`id_product`) of products in the category 'milk and cream':
(0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 28, 29, 30, 31, 32, 34, 35, 36, 37, 38, 39, 40, 42, 43, 44, 45, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75,76, 77, 78, 80, 81, 82, 83, 84, 86, 88, 89, 90, 91, 92, 93, 95, 96, 97, 98, 99, 100, 102, 103, 104, 105,106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 118, 119, 5, 14, 27, 33, 41, 46, 62, 79, 85, 87, 94, 101, 117)

Specify the `WHERE` condition: select records with the value of the `date` field greater than `'2019-06-01'` (inclusive) and strictly less than `'2019-06-02'`.

Get those records whose value of the `id_product` field is found in the list of the `IN(here_list_id)` construction.
*/

SELECT
    *
FROM
    transactions
WHERE 
    date >= '2019-06-01'
    AND date < '2019-06-02'
    AND id_product IN (0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 28, 29, 30, 31, 32, 34, 35, 36, 37, 38, 39, 40, 42, 43, 44, 45, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75,76, 77, 78, 80, 81, 82, 83, 84, 86, 88, 89, 90, 91, 92, 93, 95, 96, 97, 98, 99, 100, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 118, 119, 5, 14, 27, 33, 41, 46, 62, 79, 85, 87, 94, 101, 117
    );
