# 1389. Create Target Array in the Given Order
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given two arrays of integers nums and index. Your task is to create target array under the following rules:

# Initially target array is empty.
# From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
# Repeat the previous step until there are no elements to read in nums and index.
# Return the target array.

# It is guaranteed that the insertion operations will be valid.



class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        result = []
        for i in range (0,len(nums)):result.insert(index[i],nums[i])
        return result


"""
Approach:
- I used a simple approach to create the target array.
- I initialized an empty list called result to store the target array.
- I used a for loop to iterate through the nums array.
- For each element in nums, I inserted it at the specified index in the result array using the insert method.
- Finally, I returned the result array.
"""
