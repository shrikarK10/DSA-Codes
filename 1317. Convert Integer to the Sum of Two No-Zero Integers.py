# 1317. Convert Integer to the Sum of Two No-Zero Integers
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# No-Zero integer is a positive integer that does not contain any 0 in its decimal representation.

# Given an integer n, return a list of two integers [a, b] where:

# a and b are No-Zero integers.
# a + b = n
# The test cases are generated so that there is at least one valid solution. If there are many valid solutions, you can return any of them.


class Solution:
    def getNoZeroIntegers(self, n: int):

        for i in range(1,n):
            b = n-i
            if( '0' in str(b) or '0' in str(i) ):
                continue
            else:
                return [i,b]
"""
Approach:
- So we just loop till n and update b as n-i such that b will be our second number and i will the first number.
- But to acutally check if the both number contain 0 or not we convert them to string and check presence of zero.
- If any of them contain zero we continue the loop else we return the list [i,b] as our answer.
"""