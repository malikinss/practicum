# Lesson 3.3: SQL Advanced Features 📊

## Description 📝

This lesson delves into advanced **SQL** features, including grouping (`GROUP BY`), filtering aggregated data (`HAVING`), sorting (`ORDER BY`), date manipulation (`EXTRACT`, `DATE_TRUNC`), and subqueries. It applies these concepts to a retail database for complex data analysis.

This lesson includes a detailed theoretical explanation, 20 practical SQL tasks, and no theoretical questions, emphasizing advanced query techniques.

## Purpose 🎯

By the end of this lesson, I will:  
✅ Group and filter data using `GROUP BY` and `HAVING`  
✅ Manipulate dates with `EXTRACT` and `DATE_TRUNC`  
✅ Sort and limit query results effectively  
✅ Write subqueries for complex data retrieval

## Concepts & Theory 🔍

### 🔹 Advanced SQL Features

-   **Type Casting**: Convert data types using `CAST` or `::` (e.g., `CAST(weight AS real)`).
-   **Grouping (`GROUP BY`)**: Divide data into groups for aggregation (`COUNT`, `AVG`, `SUM`).
-   **Filtering Groups (`HAVING`)**: Filter aggregated results post-`GROUP BY`.
-   **Sorting (`ORDER BY`)**: Order results with `ASC`/`DESC`, limit with `LIMIT`.
-   **Date Functions**:
    -   `EXTRACT`: Retrieve date/time components (e.g., month, hour).
    -   `DATE_TRUNC`: Truncate date/time to specific units (e.g., day, hour).
-   **Subqueries**: Nested queries in `FROM` or `WHERE` for complex logic.

## Practical Task 🧪

### 1️⃣ **Advanced SQL Queries**

The lesson includes 20 practical tasks applying advanced SQL in a retail database:

1. **Average Weight (3_3_1_average_weight)**: Computes average weight for gram-based products.
2. **Max Weight (3_3_2_max_weight)**: Finds max weight for milk/cream products.
3. **Unique Product Count (3_3_3_count_uniq_products)**: Counts total and unique products per store.
4. **Category Max Weight (3_3_4_category_max_weight)**: Calculates max weight per product category.
5. **Price Stats (3_3_5_avg_min_max_price)**: Summarizes average, max, min prices per store.
6. **Price Difference (3_3_6_max_min_diff)**: Calculates max-min price gap for butter/margarine on June 10, 2019.
7. **Category Product Count (3_3_7_count_products_for_category_by_date)**: Counts products per category on June 5, 2019.
8. **Lentro Unique Products (3_3_8_lentro_uniq_products)**: Counts unique products per category in Lentro store on June 30, 2019.
9. **Top 5 Expensive Products (3_3_9_top_five_expenciest)**: Retrieves top 5 priciest products.
10. **Expensive Products (3_3_10_max_price_more_than)**: Finds products with max price >500 rubles.
11. **Heavy Products Count (3_3_11_third_june_products)**: Counts products >500g per store on June 3, 2019, with <10 items.
12. **Smallest Unique Counts (3_3_12_name_uniq_cnt)**: Identifies top 3 stores with smallest unique product counts (>30).
13. **Hour Extraction (3_3_13_extract_hours)**: Extracts transaction hours.
14. **Products per Hour (3_3_14_extract_and_group_by_hours)**: Counts products purchased per hour.
15. **Products per Day (3_3_15_extract_days)**: Counts products purchased per day.
16. **July 1 Analysis (3_3_16_date_month)**: Counts products purchased on July 1, 2019, grouped by day.
17. **Premium Products (3_3_17_premium_segment_products)**: Identifies premium milk/cream (>120 rubles) and butter/margarine (>300 rubles) products.
18. **Premium Buyers (3_3_18_premium_buyers)**: Finds customers buying premium products and their weekly transaction averages.
19. **Daily Transactions (3_3_19_count_products)**: Counts unique transactions per day.
20. **Weekly Transactions (3_3_20_group_by_week)**: Computes average daily transactions per week.

💡 Tasks enhance skills in grouping, date handling, and subqueries for retail analytics.

## Benefits ✅

-   Advanced SQL enables complex data analysis for business insights.
-   Date functions and subqueries simplify temporal and hierarchical queries.
-   Grouping and filtering support precise reporting.
-   Practical tasks prepare for real-world database challenges.

## Recommendations 📌

-   Use `CAST` or `::` to ensure correct data type handling.
-   Test subqueries separately to verify logic.
-   Combine `GROUP BY`, `HAVING`, and `ORDER BY` for structured analysis.
-   Use descriptive aliases for query readability.

## Output 📜

After completing this lesson, I now:  
✅ Group and filter data with `GROUP BY` and `HAVING`  
✅ Manipulate dates using `EXTRACT` and `DATE_TRUNC`  
✅ Write sorted, limited queries with `ORDER BY`  
✅ Use subqueries for advanced data retrieval

## Conclusion 🚀

Mastering advanced SQL features empowers me to perform sophisticated data analysis.  
Through practical retail database tasks, I’ve honed skills in grouping, date manipulation, and subqueries, preparing me for complex backend development with Django. 🧑‍💻✨
