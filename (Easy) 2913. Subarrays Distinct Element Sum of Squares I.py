# 2913. Subarrays Distinct Element Sum of Squares I
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given a 0-indexed integer array nums.

# The distinct count of a subarray of nums is defined as:

# Let nums[i..j] be a subarray of nums consisting of all the indices from i to j such that 0 <= i <= j < nums.length. Then the number of distinct values in nums[i..j] is called the distinct count of nums[i..j].
# Return the sum of the squares of distinct counts of all subarrays of nums.

# A subarray is a contiguous non-empty sequence of elements within an array.


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        s=0
        for i in range (0,len(nums)):
            arr = set()
            for j in range(i,len(nums)):
                arr.add(nums[j])
                s += len(arr) * len(arr) # gives lower TC than **2
        return s


"""
Approach:
- The approach was to use a nested loop to iterate through all possible subarrays of the input array nums.
- For each subarray, we used a set to store the distinct elements and calculated the distinct count by taking the square of the size of the set.
- We then added the distinct count to the sum s.
- Finally, we returned the sum s as the result.
(Initalizing the set outside of the nested loop reduces TC , also using len(arr)*len(arr) instead of **2 also reduced TC)
"""
