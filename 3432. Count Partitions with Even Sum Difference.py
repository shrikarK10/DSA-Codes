# 3432. Count Partitions with Even Sum Difference
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given an integer array nums of length n.

# A partition is defined as an index i where 0 <= i < n - 1, splitting the array into two non-empty subarrays such that:

# Left subarray contains indices [0, i].
# Right subarray contains indices [i + 1, n - 1].
# Return the number of partitions where the difference between the sum of the left and right subarrays is even44

from typing import List

class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        count =0
        for i in range (1,len(nums)):
            if (sum(nums[:i]) - sum(nums[i:])) % 2 == 0 :
                count+=1
        return count

"""
Approach:
- I initialized a counter variable 'count' to zero to keep track of the number of valid partitions.
- I iterated through the array 'nums' from index 1 to len(nums) - 1, treating each index as a potential partition point.
- For each partition point 'i', I calculated the sum of the left subarray (from index 0 to i-1) and the sum of the right subarray (from index i to the end of the array).
- I checked if the difference between the sum of the left and right subarrays is even by using the modulo operator (% 2).
- If the difference is even, I incremented the counter 'count' by 1.
- Finally, I returned the total count of valid partitions.
"""

# optimal :
def countPartitions(self, nums: List[int]) -> int:
    if sum(nums) % 2: return 0
    return len(nums) - 1

"""
Approach:
- First, I calculated the total sum of the array 'nums'.
- I checked if the total sum is odd using the modulo operator (% 2). If it is odd, I returned 0 immediately since it's impossible to partition the array into two subarrays with an even sum difference.
- If the total sum is even, I returned the number of possible partition points, which is len(nums) - 1. This is because there are (n-1) ways to partition an array of length n into two non-empty subarrays.
"""