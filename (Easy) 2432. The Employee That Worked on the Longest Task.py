# 2432. The Employee That Worked on the Longest Task
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# There are n employees, each with a unique id from 0 to n - 1.

# You are given a 2D integer array logs where logs[i] = [idi, leaveTimei] where:

# idi is the id of the employee that worked on the ith task, and
# leaveTimei is the time at which the employee finished the ith task. All the values leaveTimei are unique.
# Note that the ith task starts the moment right after the (i - 1)th task ends, and the 0th task starts at time 0.

# Return the id of the employee that worked the task with the longest time. If there is a tie between two or more employees, return the smallest id among them.



from typing import List

class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        max_time = logs[0][1]
        ind = logs[0][0]
        for i in range (1 ,len(logs)) :
            curr_time = logs[i][1] - logs[i-1][1]
            if curr_time > max_time :
                max_time = curr_time
                ind = logs[i][0]
            elif curr_time == max_time :
                ind = min(ind , logs[i][0])
        return ind


"""
Approach:
- Initialize max_time with the time taken by the first employee (logs[0][1]) and ind with the id of the first employee (logs[0][0]).
- Iterate through the logs starting from the second task.
- Calculate the time taken for the current task by subtracting the leave time of the previous task from the current task's leave time.
- If the current task time is greater than max_time, update max_time and ind with the current task's time and employee id.
- If the current task time is equal to max_time, update ind with the smaller employee id between the current and previous max.
- Return the employee id (ind) who worked the longest task.
"""