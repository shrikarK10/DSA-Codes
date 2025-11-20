# 570. Managers with at Least 5 Direct Reports
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# SQL Schema
# Pandas Schema
# Table: Employee

# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | name        | varchar |
# | department  | varchar |
# | managerId   | int     |
# +-------------+---------+
# id is the primary key (column with unique values) for this table.
# Each row of this table indicates the name of an employee, their department, and the id of their manager.
# If managerId is null, then the employee does not have a manager.
# No employee will be the manager of themself.
 

# Write a solution to find managers with at least five direct reports.

# Return the result table in any order.

# The result format is in the following example.



"""# Write your MySQL query statement below
    SELECT e.name 
    FROM 
    (
        SELECT COUNT(*) as emp_count , name , managerId
        FROM Employee
        GROUP BY managerId

    ) as q
    JOIN
    Employee as e 
    ON(e.id = q.managerId)
    WHERE q.emp_count >= 5;"""


"""
Approach:
- First thought was lets just group by annd count WRT managerId to get the count of direct reports for each manager.
- But then i realized it will not give the manager name instead it was retrieving the name of one of the employees reporting to that manager.
- So i changed the subquery to return managerId so that we can join it back to Employee table to get the manager name.

"""