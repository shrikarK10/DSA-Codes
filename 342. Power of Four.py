# 342. Power of Four
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given an integer n, return true if it is a power of four. Otherwise, return false.

# An integer n is a power of four, if there exists an integer x such that n == 4x.

 
from ast import List
import math
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<1 : return False
        return int(math.log(n)/math.log(4)) == math.log(n)/math.log(4)


"""
Approach:
- We first check if the input number n is less than 1. If it is, we return False since powers of four are positive integers.
- We then calculate the logarithm of n to the base 4 using the change of base formula: log4(n) = log(n) / log(4).
- Finally, we check if the logarithm result is an integer by comparing it to its integer cast. If they are equal, n is a power of four, and we return True; otherwise, we return False.
"""