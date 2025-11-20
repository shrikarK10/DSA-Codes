# 1527. Patients With a Condition
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# SQL Schema
# Pandas Schema
# Table: Patients

# +--------------+---------+
# | Column Name  | Type    |
# +--------------+---------+
# | patient_id   | int     |
# | patient_name | varchar |
# | conditions   | varchar |
# +--------------+---------+
# patient_id is the primary key (column with unique values) for this table.
# 'conditions' contains 0 or more code separated by spaces. 
# This table contains information of the patients in the hospital.
 

# Write a solution to find the patient_id, patient_name, and conditions of the patients who have Type I Diabetes. Type I Diabetes always starts with DIAB1 prefix.

# Return the result table in any order.

# The result format is in the following example.


"""
# Write your MySQL query statement below

SELECT patient_id , patient_name , conditions
FROM Patients
WHERE conditions LIKE 'DIAB1%' OR conditions LIKE '% DIAB1%'

"""

"""
Approach:
- We need to filter patients based on whether their conditions include Type I Diabetes, which is indicated by the prefix 'DIAB1'.
- We use the LIKE operator to check for two scenarios:
  - The conditions string starts with 'DIAB1' (using 'DIAB1%').
  - The conditions string contains ' DIAB1' preceded by a space (using '% DIAB1%').
  - This ensures that we capture cases where 'DIAB1' is either at the beginning of the conditions string or appears later in the string as a separate code.
  - We select the patient_id, patient_name, and conditions columns from the Patients table for those who meet the criteria.
  - Finally, we return the filtered results.
"""