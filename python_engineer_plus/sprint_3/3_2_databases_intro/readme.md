# Lesson 3.2: Databases Intro 🗄️

## Description 📝

This lesson introduces **databases**, focusing on **relational databases**, their structure, and **SQL** for data management.
It covers table creation, CRUD operations, joins, and querying techniques, with practical exercises in a retail database context.
This lesson includes a detailed theoretical explanation, 9 practical SQL tasks, and no theoretical questions, emphasizing hands-on database operations.

## Purpose 🎯

By the end of this lesson, I will:  
✅ Understand relational databases and their components (tables, keys, relationships)  
✅ Write SQL queries for CRUD operations and data analysis  
✅ Use joins to combine data from multiple tables  
✅ Apply database concepts to practical retail scenarios

## Concepts & Theory 🔍

### 🔹 Databases

-   **Purpose**: Systems for storing and processing data (e.g., user info, transactions).
-   **Types**: Relational (focus of the course), textual, graph, in-memory.
-   **DBMS**: Software for managing databases (e.g., PostgreSQL, MySQL).

### 🔹 Relational Databases

-   **Structure**: Data stored in tables with rows (records) and columns (fields).
-   **Keys**:
    -   **Primary Key**: Unique identifier for records.
    -   **Foreign Key**: Links to a primary key in another table.
-   **Data Types**: INTEGER, FLOAT, TEXT, DATE, MONEY, JSON, etc.

### 🔹 SQL

-   **Purpose**: Language for querying relational databases.
-   **Operations**:
    -   **CRUD**: Create (`INSERT`), Read (`SELECT`), Update (`UPDATE`), Delete (`DELETE`).
    -   **Other**: Table creation, configuration.
-   **Features**: Conditions (`WHERE`), aggregations (`COUNT`, `SUM`), joins.

### 🔹 Joins

-   **Purpose**: Combine data from multiple tables.
-   **Types**:
    -   `INNER JOIN`: Matching records only.
    -   `LEFT JOIN`: All records from left table, matching from right.
    -   `RIGHT JOIN`: All records from right table, matching from left.
    -   `FULL OUTER JOIN`: All records from both tables.

## Practical Task 🧪

### 1️⃣ **SQL Query Development**

The lesson includes 9 practical tasks applying SQL in a retail database:

1. **Database Initialization (3_2_1_get_all_data)**: Creates tables (`products`, `products_stores`, `products_data_all`, `transactions`) and retrieves all data.
2. **Product Data Selection (3_2_2_product_data_selection)**: Selects product ID, name, category, and store from `products_data_all`.
3. **Milk Day Query (3_2_3_milk_day)**: Retrieves milk/cream products for June 1, 2019.
4. **Saturday Milk Query (3_2_4_saturdays)**: Fetches milk/cream products for four Saturdays in June 2019.
5. **Milk Day Transactions (3_2_5_milkday_transactions)**: Gets transaction data for milk/cream on June 1, 2019.
6. **Record Count (3_2_6_count_records)**: Counts rows in `products_data_all`.
7. **Transaction Details (3_2_7_transaction_details)**: Joins `transactions` and `products` for product category/name, limited to 10 rows.
8. **Product Availability (3_2_8_product_availability)**: Uses `LEFT JOIN` to check product availability in stores.
9. **Post-June Transactions (3_2_9_transaction_details)**: Joins `transactions`, `products`, and `stores` for details after June 5, 2019.

💡 These tasks build SQL skills for retail data analysis and database management.

## Benefits ✅

-   Relational databases enable efficient data storage and retrieval.
-   SQL queries support complex data analysis and reporting.
-   Joins facilitate multi-table data integration.
-   Practical tasks prepare for real-world database applications.

## Recommendations 📌

-   Use uppercase for SQL keywords for readability.
-   Test queries with small datasets to verify logic.
-   Include `WHERE` in `UPDATE`/`DELETE` to avoid unintended changes.
-   Practice joins to master multi-table queries.

## Output 📜

After completing this lesson, I now:  
✅ Understand relational database concepts and structures  
✅ Write SQL queries for CRUD and multi-table operations  
✅ Apply joins to analyze retail data effectively  
✅ Solve practical database tasks with confidence

## Conclusion 🚀

Mastering relational databases and SQL equips me to manage and analyze data efficiently.  
Through practical retail scenarios, I’ve developed skills to handle real-world database challenges, preparing me for backend development with Django. 🧑‍💻✨
