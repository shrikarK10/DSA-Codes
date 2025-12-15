# 3465. Find Products with Valid Serial Numbers
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# SQL Schema
# Pandas Schema
# Table: products

# +--------------+------------+
# | Column Name  | Type       |
# +--------------+------------+
# | product_id   | int        |
# | product_name | varchar    |
# | description  | varchar    |
# +--------------+------------+
# (product_id) is the unique key for this table.
# Each row in the table represents a product with its unique ID, name, and description.
# Write a solution to find all products whose description contains a valid serial number pattern. A valid serial number follows these rules:

# It starts with the letters SN (case-sensitive).
# Followed by exactly 4 digits.
# It must have a hyphen (-) followed by exactly 4 digits.
# The serial number must be within the description (it may not necessarily start at the beginning).
# Return the result table ordered by product_id in ascending order.

# The result format is in the following example.

"""
# Write your MySQL query statement below
SELECT product_id, product_name,description 
FROM products
WHERE REGEXP_LIKE (description ,'[A-Za-z0-9]*([[:space:]]|^)SN[0-9]{4}-[0-9]{4}([[:space:]]|$)' , 'c')
ORDER BY product_id ASC;
"""


"""
Approach:
- We need to filter products based on whether their description contains a valid serial number pattern.
- We use the REGEXP_LIKE function to check if the description matches the specified pattern.
- The pattern '[A-Za-z0-9]*([[:space:]]|^)SN[0-9]{4}-[0-9]{4}([[:space:]]|$)' is used to identify valid serial numbers:
  - [A-Za-z0-9]* allows for any alphanumeric characters before the serial number.
  - ([[:space:]]|^) ensures that the serial number starts either at the beginning of the string or is preceded by a space.
  - SN[0-9]{4}-[0-9]{4} matches the required format of the serial number.
  - ([[:space:]]|$) ensures that the serial number ends either at the end of the string or is followed by a space.
"""