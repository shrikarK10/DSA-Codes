# 1068. Product Sales Analysis I
# Solved
# Easy
# SQL Schema
# Pandas Schema
# Table: Sales

# +-------------+-------+
# | Column Name | Type  |
# +-------------+-------+
# | sale_id     | int   |
# | product_id  | int   |
# | year        | int   |
# | quantity    | int   |
# | price       | int   |
# +-------------+-------+
# (sale_id, year) is the primary key (combination of columns with unique values) of this table.
# product_id is a foreign key (reference column) to Product table.
# Each row of this table shows a sale on the product product_id in a certain year.
# Note that the price is per unit.
 

# Table: Product

# +--------------+---------+
# | Column Name  | Type    |
# +--------------+---------+
# | product_id   | int     |
# | product_name | varchar |
# +--------------+---------+
# product_id is the primary key (column with unique values) of this table.
# Each row of this table indicates the product name of each product.
 

# Write a solution to report the product_name, year, and price for each sale_id in the Sales table.

# Return the resulting table in any order.

# The result format is in the following example.


"""
SELECT p.product_name , s.year , s.price 
FROM 
Sales AS s
JOIN
Product AS p 
ON (s.product_id = p.product_id)
"""


"""
approach:
-We need to retrieve the product names along with their corresponding sales year and price. 
-To achieve this, we will perform an inner join between the Sales table and the Product table based on the product_id field, which is common to both tables. 
-This will allow us to combine the relevant information from both tables into a single result set.
"""
