# 643. Maximum Average Subarray I
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum_curr = sum(nums[0:k])
        sum_sub = sum_curr
        for i in range (k, len(nums)):
            
            sum_curr +=  nums[i] - nums[i-k]
            sum_sub = max(sum_sub,sum_curr)

        return sum_sub/k


"""
Approach:
- First , I was doing a brute force approach where I was calculating the sum of every subarray of length k and keeping track of the maximum sum found.
- But my approach was giving TLE for large inputs.
- So I optimized my approach using the sliding window technique.
- I initialized sum_curr with the sum of the first k elements of the array.
- I also initialized sum_sub with the same value to keep track of the maximum sum found.
- Then, I iterated through the array starting from the k-th element to the end of the array.
- In each iteration, I updated sum_curr by adding the current element and subtracting the element that is k positions behind.
- I then updated sum_sub with the maximum value between sum_sub and sum_curr.
- Finally, I returned the maximum average by dividing sum_sub by k.
"""
