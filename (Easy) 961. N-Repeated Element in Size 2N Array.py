# 961. N-Repeated Element in Size 2N Array
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# You are given an integer array nums with the following properties:

# nums.length == 2 * n.
# nums contains n + 1 unique elements.
# Exactly one element of nums is repeated n times.
# Return the element that is repeated n times.

from typing import List

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n=[]

        for i in nums:
            if i in n :
                return i
            n.append(i)


"""
Approach:
- Initialize an empty list n to keep track of the unique elements encountered.
- Iterate through each element i in the nums array.
- For each element, check if it is already in the list n.
- If it is, return that element as it is the one repeated n times.
- If it is not in the list, append it to n and continue.
"""
