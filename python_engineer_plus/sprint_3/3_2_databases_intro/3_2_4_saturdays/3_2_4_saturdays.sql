/*
Export the fields `name`, `price`, `name_store`, `date_upd` of the category `milk and cream' for four "non-holiday" Saturdays in June: `8`, `15`, `22` and `29`.
*/

SELECT 
    name, 
    price, 
    name_store, 
    date_upd
FROM 
    products_data_all
WHERE 
    category = 'молоко и сливки'
    AND date_upd IN (
        '2019-06-08', 
        '2019-06-15', 
        '2019-06-22', 
        '2019-06-29'
    )
