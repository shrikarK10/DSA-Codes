# 1407. Top Travellers
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# SQL Schema
# Pandas Schema
# Table: Users

# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | id            | int     |
# | name          | varchar |
# +---------------+---------+
# id is the column with unique values for this table.
# name is the name of the user.
 

# Table: Rides

# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | id            | int     |
# | user_id       | int     |
# | distance      | int     |
# +---------------+---------+
# id is the column with unique values for this table.
# user_id is the id of the user who traveled the distance "distance".
 

# Write a solution to report the distance traveled by each user.

# Return the result table ordered by travelled_distance in descending order, if two or more users traveled the same distance, order them by their name in ascending order.

"""# Write your MySQL query statement below
SELECT u.name ,  COALESCE (SUM(r.distance),0) as travelled_distance
FROM Users as u LEFT JOIN Rides as r
ON (u.id=r.user_id)
GROUP BY u.id
ORDER BY travelled_distance DESC , u.name ASC"""


"""Approach:
- We perform a LEFT JOIN between the Users and Rides tables on the user ID.
- We use COALESCE to handle users with no rides, ensuring their travelled distance is reported as 0.
- We group the results by user ID to aggregate the distances traveled by each user.
- Finally, we order the results by travelled distance in descending order and by name in ascending order for users with the same distance.
"""