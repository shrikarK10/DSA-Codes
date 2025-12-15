# 175. Combine Two Tables
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# SQL Schema
# Pandas Schema
# Table: Person

# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | personId    | int     |
# | lastName    | varchar |
# | firstName   | varchar |
# +-------------+---------+
# personId is the primary key (column with unique values) for this table.
# This table contains information about the ID of some persons and their first and last names.
 

# Table: Address

# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | addressId   | int     |
# | personId    | int     |
# | city        | varchar |
# | state       | varchar |
# +-------------+---------+
# addressId is the primary key (column with unique values) for this table.
# Each row of this table contains information about the city and state of one person with ID = PersonId.
 

# Write a solution to report the first name, last name, city, and state of each person in the Person table. If the address of a personId is not present in the Address table, report null instead.

# Return the result table in any order.

# The result format is in the following example.

"""
# Write your MySQL query statement below
SELECT p.firstname as firstName , p.lastname as lastName ,  COALESCE(a.city,null) as city , COALESCE(a.state,null) as state
FROM Person as p LEFT JOIN Address as a ON (p.personId=a.personId);
"""


"""
Approach:
- We perform a LEFT JOIN between the Person and Address tables on the personId column.
- We use COALESCE to ensure that if there is no matching address for a person, the city and state fields will return null.
"""