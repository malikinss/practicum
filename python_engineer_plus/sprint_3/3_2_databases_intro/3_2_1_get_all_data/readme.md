# Database Initialization and Exploration Queries

## Description 📝

The provided SQL code snippet initializes a database by dropping and recreating four tables: `products`, `products_stores`, `products_data_all`, and `transactions`.

It defines their schemas, inserts sample data, and includes queries to retrieve all columns from each table. The tables store information about products, their availability and pricing in stores, detailed product data, and transaction records.

The `SELECT *` queries at the end allow exploration of the table structures and contents, facilitating further analysis in a retail or inventory management context.

## Purpose 🎯

Intended for setting up a retail database for analysis, testing, or educational purposes, demonstrating table creation, data insertion, and basic data retrieval in SQL.

The queries enable users to inspect table schemas and sample data, serving as a foundation for more complex operations like joins or aggregations.

## How It Works 🔍

-   **Module Import**:

    -   No external modules; uses standard SQL syntax compatible with relational databases (e.g., SQLite, PostgreSQL).

-   **Table Dropping and Creation**:

    -   **`DROP TABLE IF EXISTS`**: Ensures clean setup by removing existing tables (`products`, `products_stores`, `products_data_all`, `transactions`).
    -   **CREATE TABLE**:
        -   `products`:
            -   Columns: `id_product` (INTEGER, PRIMARY KEY), `name` (TEXT, NOT NULL), `category` (TEXT, NOT NULL), `units` (TEXT, NOT NULL), `weight` (TEXT).
            -   Stores core product details (e.g., milk products, butter).
        -   `products_stores`:
            -   Columns: `id_product` (INTEGER, NOT NULL), `price` (INTEGER, NOT NULL), `id_store` (INTEGER, NOT NULL), `date_upd` (DATETIME, NOT NULL).
            -   Primary Key: `(id_product, id_store, date_upd)`.
            -   Tracks product prices and availability per store over time.
        -   `transactions`:
            -   Columns: `user_id` (INTEGER, NOT NULL), `id_transaction` (INTEGER, NOT NULL), `id_store` (INTEGER, NOT NULL), `id_product` (INTEGER, NOT NULL), `date` (DATETIME, NOT NULL), `unique_id` (INTEGER, NOT NULL, PRIMARY KEY).
            -   Records sales transactions with user and product details.
        -   `products_data_all`:
            -   Columns: `id_product` (INTEGER, NOT NULL), `name` (VARCHAR(255), NOT NULL), `category` (VARCHAR(100), NOT NULL), `units` (VARCHAR(10), NOT NULL), `weight` (DECIMAL(10,3)), `price` (DECIMAL(10,2), NOT NULL), `date_upd` (DATETIME, NOT NULL), `id_store` (INTEGER, NOT NULL), `name_store` (VARCHAR(100), NOT NULL).
            -   Primary Key: `(id_product, id_store)`.
            -   Aggregates product details with store-specific information.

-   **Data Insertion**:

    -   **products**: Inserts 21 rows, primarily milk and butter products (e.g., "Молоко топленое Эконива 4%, 1 л", "Масло сливочное Arla Natura 82 %, 400 г").
    -   **products_stores**: Inserts 21 rows with product prices for store `id_store=0` on `2019-06-01` (e.g., product `id_product=3`, price=69).
    -   **transactions**: Inserts 20 rows of transaction data from June 2019, linking users, products, and stores (e.g., `user_id=326`, `id_product=144`, `date='2019-06-14'`).
    -   **products_data_all**: Inserts 20 rows with detailed product data for store `id_store=0` (e.g., `id_product=3`, price=69.00, store="Молочные вкусности").

-   **Retrieval Queries**:

    -   `SELECT * FROM products;`: Retrieves all columns and rows from `products`.
    -   `SELECT * FROM products_stores;`: Retrieves all columns and rows from `products_stores`.
    -   `SELECT * FROM products_data_all;`: Retrieves all columns and rows from `products_data_all`.
    -   `SELECT * FROM transactions;`: Retrieves all columns and rows from `transactions`.

-   **Behavior**:
    -   **products**: Returns 21 rows with product IDs, names, categories (e.g., "молоко и сливки"), units (e.g., "л", "г"), and weights (e.g., "1", "900").
    -   **products_stores**: Returns 21 rows with product-store combinations, prices, and update dates (e.g., `id_product=3`, `price=69`, `date_upd='2019-06-01'`).
    -   **products_data_all**: Returns 20 rows with detailed product info, including store names (e.g., `id_product=3`, `name_store="Молочные вкусности"`).
    -   **transactions**: Returns 20 rows of transaction records (e.g., `unique_id=0`, `id_product=144`, `date='2019-06-14 16:27:30'`).
    -   **Output**: Each query produces a result set with all columns and rows, formatted based on the SQL client used.

## Verification ✅

Implementation satisfies requirements:

-   **Functionality**:

    -   Drops and recreates `products`, `products_stores`, `products_data_all`, and `transactions` tables.
    -   Defines schemas with appropriate columns, data types, and constraints.
    -   Inserts sample data to populate tables.
    -   Retrieves all columns from each table using `SELECT *`.

-   **Correctness**:

    -   Table schemas align with retail use case:
        -   `products`: Product catalog with IDs, names, and attributes.
        -   `products_stores`: Product availability and pricing per store.
        -   `transactions`: Sales records with user and product links.
        -   `products_data_all`: Comprehensive product-store data.
    -   Primary keys ensure uniqueness (e.g., `unique_id` in `transactions`, composite keys in `products_stores` and `products_data_all`).
    -   Data types are appropriate (e.g., `DECIMAL` for prices, `DATETIME` for dates).
    -   Inserted data is consistent (e.g., `id_product=3` appears in multiple tables with matching details).

-   **Output**:

    -   Queries return all columns and rows as required, enabling schema and data inspection.
    -   Matches task goal of exploring table structures and contents.

-   **Documentation**: Clear comments in SQL code and detailed README sections.

## Potential Considerations 🛠️

-   **Correctness**:

    -   No foreign key constraints defined, which could allow orphaned records (e.g., `id_product` in `transactions` not in `products`).
    -   `weight` in `products` is `TEXT`, while in `products_data_all` it’s `DECIMAL(10,3)`, potentially causing type mismatches.
    -   No `NOT NULL` constraints on some columns (e.g., `weight` in `products_data_all`), allowing `NULL` values.
    -   Sample data is limited to June 2019 and specific products, sufficient for testing but not comprehensive.

-   **Performance**:

    -   `DROP` and `CREATE`: O(1) for schema operations.
    -   `INSERT`: O(n) for n rows, efficient for small datasets (20–21 rows).
    -   `SELECT *`: O(n) for n rows, but may be slow for large datasets.
    -   Total: Efficient for setup and exploration of small tables.

-   **Design**:

    -   Composite primary keys (e.g., `products_stores`, `products_data_all`) ensure uniqueness for product-store combinations.
    -   `products_data_all` duplicates some `products` data, possibly for denormalized querying efficiency.
    -   No indexes defined beyond primary keys, which could impact query performance on large datasets.
    -   Clear table naming and column definitions align with retail domain.

-   **Alternatives**:

    -   Add foreign keys: Enforce referential integrity (e.g., `id_product` references `products`).
    -   Normalize `products_data_all`: Avoid duplication by joining `products` and `products_stores`.
    -   Use specific columns in `SELECT`: Improve performance over `SELECT *` for large tables.
    -   Add indexes: Optimize queries on `id_product` or `date`.

-   **Extensibility**:

    -   Easily add new tables (e.g., `stores` for store details).
    -   Can extend schemas with additional columns (e.g., `stock_quantity` in `products_stores`).
    -   Supports further queries (e.g., sales analysis, product availability).

-   **Edge Cases**:
    -   Empty tables: `SELECT *` returns no rows but shows column headers.
    -   Missing tables: Prevented by `DROP IF EXISTS` and `CREATE`.
    -   Invalid data: Not handled in `INSERT` (assumes valid sample data).
    -   Large datasets: Current queries are unoptimized for scale.

## Usage Example (For Clarity, Not Submission) 📦

```sql
-- Execute setup and queries in a SQL client
DROP TABLE IF EXISTS products;
-- ... (other DROP and CREATE statements)
-- ... (INSERT statements)

-- Retrieve data
SELECT * FROM products;
-- Output (sample):
-- id_product | name | category | units | weight
-- 0 | Молоко топленое Эконива 4%, 1 л | молоко и сливки | л | 1
-- 1 | Молоко пастеризованное Му-му отборное 3,4-6,0%, 900 г | молоко и сливки | г | 900
-- ...

SELECT * FROM products_stores;
-- Output (sample):
-- id_product | price | id_store | date_upd
-- 3 | 69 | 0 | 2019-06-01 00:00:00
-- 5 | 78 | 0 | 2019-06-01 00:00:00
-- ...

SELECT * FROM products_data_all;
-- Output (sample):
-- id_product | name | category | units | weight | price | date_upd | id_store | name_store
-- 3 | Молоко цельное пастеризованное Ваша Ферма 3,4-6,0%, 1 л | молоко и сливки | л | 1.000 | 69.00 | 2019-06-01 00:00:00 | 0 | Молочные вкусности
-- ...

SELECT * FROM transactions;
-- Output (sample):
-- user_id | id_transaction | id_store | id_product | date | unique_id
-- 326 | 25815 | 2 | 144 | 2019-06-14 16:27:30 | 0
-- 326 | 25815 | 2 | 117 | 2019-06-14 16:27:30 | 1
-- ...
```

## Conclusion 🚀

The implementation successfully initializes a retail database with `products`, `products_stores`, `products_data_all`, and `transactions` tables, populates them with sample data, and provides queries to retrieve all columns.

It establishes a robust foundation for exploring table structures and contents, with clear schemas and consistent data.

The code is efficient, modular, and fully compliant with the task’s requirements, making it ideal for retail data analysis or teaching SQL database setup and exploration.
