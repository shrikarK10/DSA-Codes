# 231. Power of Two
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given an integer n, return true if it is a power of two. Otherwise, return false.

# An integer n is a power of two, if there exists an integer x such that n == 2x.

#Approach matches that of 342. Power of Four (But has issues with floating point precision)
import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        return abs(math.log2(n)- round(math.log2(n))) < 1e-10
 
#Best Approach
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        return (n & (n - 1)) == 0

"""
Approach:
- My initial approach was like directly calculating the logarithm of n to the base 2 and checking if it was equal to integer value of itself.
- However, this approach can suffer from floating-point precision issues for large values of n.
- So because of that i had to use a small threshold to compare the difference between the logarithm and its rounded value.
- And it can still fail for some edge cases.
- The best approach uses a bit manipulation technique. A number n is a power of two if it has exactly one bit set in its binary representation.
- The expression (n & (n - 1)) removes the lowest set bit from n. If n is a power of two, this operation will result in 0.
- Thus, if (n & (n - 1)) == 0, we can conclude that n is a power of two.
"""