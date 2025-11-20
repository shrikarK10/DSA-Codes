# 177. Nth Highest Salary
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# SQL Schema
# Pandas Schema
# Table: Employee

# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | id          | int  |
# | salary      | int  |
# +-------------+------+
# id is the primary key (column with unique values) for this table.
# Each row of this table contains information about the salary of an employee.
 

# Write a solution to find the nth highest distinct salary from the Employee table. If there are less than n distinct salaries, return null.

# The result format is in the following example.


"""
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
SET N=N-1;
RETURN (
# Write your MySQL query statement below.
SELECT DISTINCT Salary FROM Employee ORDER BY Salary DESC LIMIT N, 1
);
END
"""

"""
Approach:
- We create a stored function named getNthHighestSalary that takes an integer parameter N.
- Inside the function, we decrement N by 1 to adjust for zero-based indexing.
- We then execute a SQL query to select distinct salaries from the Employee table, ordering them in
    descending order.
- We use the LIMIT clause to skip the first N-1 salaries and retrieve the Nth highest salary.
- Finally, we return the result of the query. If there are less than N distinct salaries, the query will return null.
- The function is defined to return an integer value.
"""