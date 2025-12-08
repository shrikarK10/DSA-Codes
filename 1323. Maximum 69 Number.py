# 1323. Maximum 69 Number
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given a positive integer num consisting only of digits 6 and 9.

# Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).



class Solution:
    def maximum69Number (self, num: int) -> int:
        s = str(num)
        if '6' not in s : return num
        else:s = s[:s.index('6')]+'9'+s[s.index('6')+1:]
        return int(s)


"""
Approach:
- I converted the number to a string and checked if it contains the digit '6'.
- If it doesn't contain '6', I returned the number as it is the maximum possible number.
- If it contains '6', I replaced the first occurrence of '6' with '9' and returned the new number.
"""
