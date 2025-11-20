# 1331. Rank Transform of an Array
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an array of integers arr, replace each element with its rank.

# The rank represents how large the element is. The rank has the following rules:

# Rank is an integer starting from 1.
# The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
# Rank should be as small as possible.
 
class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        unique_sorted = sorted(set(arr))           
        rank_map = {val: i+1 for i, val in enumerate(unique_sorted)}  
        return [rank_map[x] for x in arr]        


"""
Approach:
- First we create a sorted list of unique elements from the input array.
- Then we create a mapping of each unique element to its rank using a dictionary comprehension.
- Finally, we replace each element in the original array with its corresponding rank from the mapping and return the transformed array.
"""