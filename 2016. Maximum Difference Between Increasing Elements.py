# 2016. Maximum Difference Between Increasing Elements
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given a 0-indexed integer array nums of size n, find the maximum difference between nums[i] and nums[j] (i.e., nums[j] - nums[i]), such that 0 <= i < j < n and nums[i] < nums[j].

# Return the maximum difference. If no such i and j exists, return -1.

class Solution:
    def maximumDifference(self, nums) -> int:
        min=0
        max_diff = -1
        for i in range (1 , len(nums)):
            if(nums[min]<nums[i] and nums[i] - nums[min] > max_diff):
                max_diff = nums[i] - nums[min]
            elif (nums[i]<nums[min]):
                min = i
        return max_diff

"""
Approach:
- We use two variables min and max_diff like a two pointer approach.
- min keeps track of the index of minimum element so far.
- max_diff keeps track of the maximum difference found so far.
- We traverse the array from index 1 to n-1 as min is initialized to 0.
- We check if the current number is smaller than the current min 
- if it is smaller then we also check if the there is a greater difference than max_diff
- if it is then we update max_diff.
- if the current number is smaller than the number at index min then we update min to current index.
- Finally we return max_diff.
"""