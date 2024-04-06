-- Unload the last_name and percent_of_discount fields from the buyer table.
SELECT 
    last_name,
    percent_of_discount
FROM 
    buyer;

-- Unload the bracelet_id, last_name and percent_of_discount fields from the buyer table. 
--Assign the aliases id, name_client and discount to the fields respectively.
SELECT 
    bracelet_id AS id,
    last_name AS name_client,
    percent_of_discount AS discount
FROM 
    buyer;

-- Unload the bracelet_id, first_name, gender and percent_of_discount fields from the buyer table. 
-- Assign the fields aliases id , first_name_client , gender_client and discount respectively. 
-- Arrange the fields in the final table in the following order: first_name_client, gender_client, discount and id.
SELECT 
    first_name AS first_name_client,
    gender AS gender_client,
    percent_of_discount AS discount,
    bracelet_id AS id
FROM 
    buyer;