# 2239. Find Closest Number to Zero
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an integer array nums of size n, return the number with the value closest to 0 in nums. If there are multiple answers, return the number with the largest value.


from typing import List

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        abs_a = [abs(x) for x in nums]
    
        if min(abs_a) in nums:
            return min(abs_a)
        else:
            return -min(abs_a)


"""
Approach:
- Create a list abs_a that contains the absolute values of each element in nums.
- Find the minimum value in abs_a using the min() function.
- Check if this minimum absolute value exists in the original nums list.
- If it does, return that value as it is the closest to zero.
- If the minimum absolute value is not in nums, return its negative counterpart, which will be the closest number to zero with the largest value.
"""
