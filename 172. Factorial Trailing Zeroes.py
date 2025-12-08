# 172. Factorial Trailing Zeroes
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given an integer n, return the number of trailing zeroes in n!.

# Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.



class Solution:
    def trailingZeroes(self, n: int) -> int:
        return (n//5) + (n//5**2) + (n//5**3) + (n//5**4) + (n//5**5)


"""
Approach:
- While observing the facotrials of numbers in sequence I found out that the number of trailing zeroes increase by 1 every time a multiple of 5 is encountered.
- Also I found out that the number of trailing zeroes increase by 2 (1 because of multiple of 5 and 1 because of power of 5) every time when power of 5 is encountered. 
- So I just returned the sum of all the quotients of n divided by powers 5 till 10^4 as the constraint is 10^4. 
"""