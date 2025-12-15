# 1741. Find Total Time Spent by Each Employee
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# SQL Schema
# Pandas Schema
# Table: Employees

# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | emp_id      | int  |
# | event_day   | date |
# | in_time     | int  |
# | out_time    | int  |
# +-------------+------+
# (emp_id, event_day, in_time) is the primary key (combinations of columns with unique values) of this table.
# The table shows the employees' entries and exits in an office.
# event_day is the day at which this event happened, in_time is the minute at which the employee entered the office, and out_time is the minute at which they left the office.
# in_time and out_time are between 1 and 1440.
# It is guaranteed that no two events on the same day intersect in time, and in_time < out_time.
 

# Write a solution to calculate the total time in minutes spent by each employee on each day at the office. Note that within one day, an employee can enter and leave more than once. The time spent in the office for a single entry is out_time - in_time.

# Return the result table in any order.

# The result format is in the following example.


# Write your MySQL query statement below
"""SELECT event_day as day , emp_id , SUM(out_time-in_time) as total_time
FROM Employees
GROUP BY day , emp_id;"""


"""
Approach:
- We need to calculate the total time spent by each employee on each day at the office.
- The time spent for a single entry can be calculated as out_time - in_time.
- We can use the SUM function to aggregate the total time spent by each employee on each day.
- We will group the results by event_day and emp_id to get the total time for each employee on each day.
- The final query selects the event_day as day, emp_id, and the sum of (out_time - in_time) as total_time.
- This approach ensures that we account for multiple entries and exits by the same employee on the same day.
- The time complexity of this query is O(n), where n is the number of records in the Employees table, as we need to scan through all the records to compute the sums.
"""