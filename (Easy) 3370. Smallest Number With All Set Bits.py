# 3370. Smallest Number With All Set Bits
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given a positive number n.

# Return the smallest number x greater than or equal to n, such that the binary representation of x contains only set bits


class Solution(object):
    def smallestNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        for i in range (1,11):
            if(n<=(2**i)-1):
                return (2**i)-1
            

"""
Approach:
- So by reading the problem it seems little bit complicated but if we carefully observe the constraints given we can see a approach to solve this problem
- w.r.t constraints n can be at max 1000 which means n can't be greater than 2**11 -1 ( which is 2047)
- So question arises that why are we considering powers of 2 here ?
- Because all powers of 2 are in their binary representation start with 1 followed by all 0's and when we subtract 1 from them we get all bits set to 1 in binary representation.
- So we can iterate from 1 to 11 ( as 2**11 -1 = 2047 which is just greater than 1000) and check for the smallest power of 2 -1 which is greater than or equal to n and return that value.
"""