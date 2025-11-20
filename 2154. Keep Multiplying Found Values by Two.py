# 2154. Keep Multiplying Found Values by Two
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given an array of integers nums. You are also given an integer original which is the first number that needs to be searched for in nums.

# You then do the following steps:

# If original is found in nums, multiply it by two (i.e., set original = 2 * original).
# Otherwise, stop the process.
# Repeat this process with the new number as long as you keep finding the number.
# Return the final value of original.

from typing import List
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        
        while(True):
            if original not in nums:
                return original
            else:
                original *= 2


"""
Approach:
- The problem is pretty simple.
- We need to keep multiplying the original value by 2 until we find it in the nums list.
- So I used a while loop to keep checking if the original value is in the nums list.
- If it is not found, we return the original value.
- If it is found, we multiply the original value by 2 and continue the loop.
- The loop will continue until the original value is not found in the nums list.
"""
