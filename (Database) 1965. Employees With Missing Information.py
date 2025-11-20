# 1965. Employees With Missing Information
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
# +-------------+---------+
# employee_id is the column with unique values for this table.
# Each row of this table indicates the name of the employee whose ID is employee_id.
 

# Table: Salaries

# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | employee_id | int     |
# | salary      | int     |
# +-------------+---------+
# employee_id is the column with unique values for this table.
# Each row of this table indicates the salary of the employee whose ID is employee_id.
 

# Write a solution to report the IDs of all the employees with missing information. The information of an employee is missing if:

# The employee's name is missing, or
# The employee's salary is missing.
# Return the result table ordered by employee_id in ascending order.


"""# Write your MySQL query statement below

SELECT uni.employee_id  
FROM (
    (
    SELECT e.employee_id , e.name , s.salary
    FROM Employees as e LEFT JOIN Salaries as s ON (e.employee_id=s.employee_id)
    ) 
    UNION
    (
    SELECT s.employee_id , e.name , s.salary
    FROM Employees as e RIGHT JOIN Salaries as s ON (e.employee_id=s.employee_id)
    ) 
) as uni
WHERE uni.name IS NULL or uni.salary IS NULL
ORDER BY uni.employee_id ASC"""


"""
Approach:
- We wanted to use a FULL OUTER JOIN to combine the Employees and Salaries tables on employee_id to get all employees along with their names and salaries.
- However, since MySQL does not support FULL OUTER JOIN directly, we simulated it using a UNION of a LEFT JOIN and a RIGHT JOIN.
- In the LEFT JOIN, we selected all employees from the Employees table and matched their salaries from the Salaries table, resulting in NULL salaries for employees without salary records.
- In the RIGHT JOIN, we selected all employees from the Salaries table and matched their names from the Employees table, resulting in NULL names for employees without name records.
- We combined the results of both joins using UNION to get a complete list of employees with their names and salaries.
- Finally, we filtered the combined results to include only those employees with NULL names or NULL salaries,"""