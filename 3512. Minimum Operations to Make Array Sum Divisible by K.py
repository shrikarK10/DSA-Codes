# 3512. Minimum Operations to Make Array Sum Divisible by K
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given an integer array nums and an integer k. You can perform the following operation any number of times:

# Select an index i and replace nums[i] with nums[i] - 1.
# Return the minimum number of operations required to make the sum of the array divisible by k.


from ast import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(nums) % k
    

"""
Approach:
- We calculate the sum of the array `nums` using the built-in `sum` function.
- We then take the modulo of this sum with `k` using the `%` operator.
- The result of this operation gives us the minimum number of operations required to make the sum of the array divisible by `k`, since each operation reduces the sum by 1.
- Finally, we return this result.
"""