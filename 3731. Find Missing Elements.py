# 3731. Find Missing Elements
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given an integer array nums consisting of unique integers.

# Originally, nums contained every integer within a certain range. However, some integers might have gone missing from the array.

# The smallest and largest integers of the original range are still present in nums.

# Return a sorted list of all the missing integers in this range. If no integers are missing, return an empty list.

 

class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return sorted(list(set([i for i in range (min(nums) , max(nums))]) - set(nums)))
    

"""
Approach:
- First, we create a set of all integers in the range from the minimum to the maximum value in the input array.
- Then, we convert the input list to a set.
- We subtract the set of input numbers from the complete set to find the missing integers.
- Finally, we convert the resulting set of missing integers to a sorted list and return it.
"""