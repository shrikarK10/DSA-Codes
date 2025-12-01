# 628. Maximum Product of Three Numbers
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given an integer array nums, find three numbers whose product is maximum and return the maximum product.


from typing import List
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[0] * nums[1] * nums[len(nums)-1] , nums[len(nums)-1] * nums[len(nums)-2] * nums[len(nums)-3])
        

"""
Approach:
- First, I sorted the input array nums in ascending order.
- After sorting, I considered two possible scenarios for the maximum product of three numbers:
  1. The product of the three largest numbers in the sorted array, which are located at the end of the array.
  2. The product of the two smallest numbers (which could be negative) and the largest number. This is because multiplying two negative numbers results in a positive product, which could potentially yield a larger product when combined with the largest positive number.
- I calculated both products and returned the maximum of the two.
"""