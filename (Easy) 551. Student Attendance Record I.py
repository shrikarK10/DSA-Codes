# 551. Student Attendance Record I
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# You are given a string s representing an attendance record for a student where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:

# 'A': Absent.
# 'L': Late.
# 'P': Present.
# The student is eligible for an attendance award if they meet both of the following criteria:

# The student was absent ('A') for strictly fewer than 2 days total.
# The student was never late ('L') for 3 or more consecutive days.
# Return true if the student is eligible for an attendance award, or false otherwise.



class Solution:
    def checkRecord(self, s: str) -> bool:
        abs_count = 0
        cons_late = 0
        for i in s:
            if i == 'A':
                abs_count+=1
                cons_late=0
            elif i == 'L':
                cons_late+=1
            else: cons_late=0
            if abs_count >= 2 or cons_late == 3:
                return False
        return True


"""
Approach:
- I used a simple approach to check if the student is eligible for an attendance award.
- I initialized two variables abs_count and cons_late to 0.
- I used a for loop to iterate through the string s.
- For each character in s, I checked if it is 'A' or 'L' and updated the abs_count and cons_late variables accordingly.
- If abs_count is greater than or equal to 2 or cons_late is equal to 3, I returned False as the student is not eligible for an attendance award.
- Otherwise, I returned True as the student is eligible for an attendance award.
"""
