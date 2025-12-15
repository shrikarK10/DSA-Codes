# 3349. Adjacent Increasing Subarrays Detection I
# Solved
# Easy

# Given an array nums of n integers and an integer k, determine whether there exist two adjacent subarrays of length k such that both subarrays are strictly increasing. Specifically, check if there are two subarrays starting at indices a and b (a < b), where:

# Both subarrays nums[a..a + k - 1] and nums[b..b + k - 1] are strictly increasing.
# The subarrays must be adjacent, meaning b = a + k.
# Return true if it is possible to find two such subarrays, and false otherwise.


class Solution:
    def hasIncreasingSubarrays(self, nums, k: int) -> bool:
        n = len(nums)
        inc_len = [1] * n
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                inc_len[i] = inc_len[i + 1] + 1
            else:
                inc_len[i] = 1

        for a in range(0, n - 2*k + 1):
            if inc_len[a] >= k and inc_len[a + k] >= k:
                return True
        return False
    

""" 
Approach:
- We first calculate the length of the longest increasing subarray starting from each index and store itin an array inc_len.
- We then iterate through the array to check for two adjacent subarrays of length k that are strictly increasing.
- If we find such subarrays, we return True; otherwise, we return False.
"""