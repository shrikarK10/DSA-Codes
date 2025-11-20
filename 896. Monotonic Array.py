# 896. Monotonic Array
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# An array is monotonic if it is either monotone increasing or monotone decreasing.

# An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

# Given an integer array nums, return true if the given array is monotonic, or false otherwise.


from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
            #  inc dec
        flags= [0 , 0]
        for i in range (0,len(nums)-1):
            if(nums[i] == nums [i+1]):
                continue
            if(nums[i]<nums[i+1]):
                flags[0] = 1
            elif(nums[i]>nums[i+1]):
                flags[1] =1
            if(flags[0]==1 and flags[1]==1):
                return False
        return True

"""
Approach:
- We initialize two flags to track if the array is increasing or decreasing.
- We iterate through the array and compare each element with the next one.
- If the current element is less than the next, we set the increasing flag.
- If the current element is greater than the next, we set the decreasing flag.
- If both flags are set, it means the array is neither monotone increasing nor monotone decreasing, so we return False.
- If we finish the loop without both flags being set, the array is monotonic, so we return True.
"""
