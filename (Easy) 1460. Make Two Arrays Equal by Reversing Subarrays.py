# 1460. Make Two Arrays Equal by Reversing Subarrays
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given two integer arrays of equal length target and arr. In one step, you can select any non-empty subarray of arr and reverse it. You are allowed to make any number of steps.

# Return true if you can make arr equal to target or false otherwise.

from typing import List

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return sorted(target) == sorted(arr)
    
"""
Approach:
- The problem can be solved by checking if both arrays contain the same elements with the same frequency.
- Since we can reverse any subarray any number of times, the order of elements does not matter.
- We can sort both arrays and compare them. If they are equal after sorting, it means we can make arr equal to target by reversing subarrays.
"""