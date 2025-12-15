# 1873. Calculate Special Bonus
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# SQL Schema
# Pandas Schema
# Table: Employees

# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | employee_id | int     |
# | name        | varchar |
# | salary      | int     |
# +-------------+---------+
# employee_id is the primary key (column with unique values) for this table.
# Each row of this table indicates the employee ID, employee name, and salary.
 

# Write a solution to calculate the bonus of each employee. The bonus of an employee is 100% of their salary if the ID of the employee is an odd number and the employee's name does not start with the character 'M'. The bonus of an employee is 0 otherwise.

# Return the result table ordered by employee_id.

# The result format is in the following example.

"""
# Write your MySQL query statement below
SELECT k.employee_id , COALESCE(m.salary,0) as bonus
FROM 
(
    SELECT employee_id , salary
    FROM Employees
    WHERE (employee_id % 2 =1) AND (name NOT LIKE 'M%')
) as m 
RIGHT JOIN Employees as k 
ON (m.employee_id = k.employee_id)
ORDER BY k.employee_id ASC
"""

"""
Approach:
- So what we do is first filter out the employees who are eligible for the bonus based on the given conditions with the help of a subquery
- After that we join the result of the subquery with original Employees table using right join to get all employees
- and also coalesce is use to shoe that if an employee is not eligible for bonus then we show 0 as bonus
- Finally we order the result by employee_id in ascending order
"""