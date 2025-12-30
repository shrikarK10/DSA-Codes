# 1450. Number of Students Doing Homework at a Given Time
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given two integer arrays startTime and endTime and given an integer queryTime.

# The ith student started doing their homework at the time startTime[i] and finished it at time endTime[i].

# Return the number of students doing their homework at time queryTime. More formally, return the number of students where queryTime lays in the interval [startTime[i], endTime[i]] inclusive.


from typing import List
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count=0
        for i in range (0,len(startTime)):
            if startTime[i] == queryTime or endTime[i] == queryTime or (startTime[i] < queryTime and endTime[i] > queryTime):
                count+=1
        return count


"""
Approach:
- Initialize a counter to zero.
- Loop through each student's start and end times.
- For each student, check if the queryTime falls within their start and end times (inclusive).
- If it does, increment the counter.
- Finally, return the counter which represents the number of students doing homework at queryTime.
"""
