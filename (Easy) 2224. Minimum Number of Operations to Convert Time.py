# 2224. Minimum Number of Operations to Convert Time
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given two strings current and correct representing two 24-hour times.

# 24-hour times are formatted as "HH:MM", where HH is between 00 and 23, and MM is between 00 and 59. The earliest 24-hour time is 00:00, and the latest is 23:59.

# In one operation you can increase the time current by 1, 5, 15, or 60 minutes. You can perform this operation any number of times.

# Return the minimum number of operations needed to convert current to correct.



class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        current_time = int(current[0:2])*60 + int(current[3:])
        correct_time = int(correct[0:2])*60 + int(correct[3:])
        diff=correct_time-current_time
        opps = 0
        if(diff>=60):
            opps+=diff//60
            diff = diff % 60
        if(diff>=15):
            opps+=diff//15
            diff = diff % 15
        if(diff >= 5 ):
            opps+= diff//5
            diff = diff % 5
        if(diff!=0):
            opps+=diff
        return opps
    

"""
Approach:
- First, we convert the given time strings "HH:MM" into total minutes from the start of the day (00:00).
- We calculate the difference in minutes between the correct time and the current time.
- We then use a greedy approach to minimize the number of operations needed to convert the current time to the correct time.
- We start by using the largest operation (60 minutes) and work our way down to the smallest (1 minute).
- For each operation, we determine how many times we can use that operation without exceeding the remaining difference in time.
- We keep track of the total number of operations used and return that as the result.
- The time complexity of this approach is O(1) since the number of operations is constant and does not depend on the input size.
"""
