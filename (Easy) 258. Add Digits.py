# 258. Add Digits
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.




class Solution:
    def addDigits(self, num: int) -> int:
        x = sum(int(i) for i in list(str(num)))
        if x >= 10:
            while(True):
                m=str(x)
                x=int(m[0])+int(m[1])
                if x < 10 : return x
        else:
            return x   
        
"""
Approach:
- Convert the integer num to a string to access each digit.
- Sum the digits of num.
- If the sum is 10 or greater, repeat the process of summing the digits of the new sum.
- Continue this until the sum is a single-digit number.
- Return the final single-digit sum.
"""
