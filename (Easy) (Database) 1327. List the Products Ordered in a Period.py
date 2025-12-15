# 1327. List the Products Ordered in a Period
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# SQL Schema
# Pandas Schema
# Table: Products

# +------------------+---------+
# | Column Name      | Type    |
# +------------------+---------+
# | product_id       | int     |
# | product_name     | varchar |
# | product_category | varchar |
# +------------------+---------+
# product_id is the primary key (column with unique values) for this table.
# This table contains data about the company's products.
 

# Table: Orders

# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | product_id    | int     |
# | order_date    | date    |
# | unit          | int     |
# +---------------+---------+
# This table may have duplicate rows.
# product_id is a foreign key (reference column) to the Products table.
# unit is the number of products ordered in order_date.
 

# Write a solution to get the names of products that have at least 100 units ordered in February 2020 and their amount.

# Return the result table in any order.

# The result format is in the following example.



# Write your MySQL query statement below
"""SELECT p.product_name , s.unit
FROM
Products AS p 
JOIN(
        SELECT product_id , SUM(unit) as unit
        FROM Orders
        WHERE order_date >='2020-02-01' AND order_date < '2020-03-01'
        GROUP BY product_id
    ) as s
    ON (p.product_id = s.product_id)
    WHERE s.unit >= 100;"""



"""
Approach:
- We need to join the Products and Orders tables to get the product names along with their ordered units.
- First, we filter the Orders table to include only those orders placed in February 2020 using a WHERE clause on the order_date.
- Next, we group the filtered orders by product_id and calculate the total units ordered for each product using the SUM function.
- We then join this aggregated result with the Products table on the product_id to get the corresponding product names.
- Finally, we filter the results to include only those products that have at least 100 units ordered using a WHERE clause.
- The final SELECT statement retrieves the product names and their total ordered units.
"""