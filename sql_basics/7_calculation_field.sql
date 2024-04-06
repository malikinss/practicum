-- The 'bracelet_id' field stores a six-digit number responsible for the bracelet code. 
-- All these numbers start with 145. 
-- To make it more convenient to work with the field, these numbers can be removed. 
-- Display the first five records with the 'bracelet_id' field and a new field with only the last three digits.
SELECT 
    bracelet_id,
    bracelet_id - 145000
FROM 
    buyer
LIMIT 5;

-- The table with orders of hot dogs stores fields with the price for one hot dog and the number of goods ordered. 
-- Print the first ten lines of the fields 'order_id', 'price', 'quantity' and the calculation field, which will display the cost of the order.
SELECT 
    order_id,
    price,
    quantity,
    price * quantity
FROM 
    hotdog
LIMIT 10;