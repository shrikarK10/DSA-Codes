# 1784. Check if Binary String Has at Most One Segment of Ones
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given a binary string s ​​​​​without leading zeros, return true​​​ if s contains at most one contiguous segment of ones. Otherwise, return false.

 
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return "01" not in s


"""
Approach:
- We check if the string contains the substring "01".
- If it does, it means there is more than one segment of ones hence return False.
- If it does not, it means there is at most one segment of ones hence return True.
"""