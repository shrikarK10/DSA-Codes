# 268. Missing Number
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

 

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        return list(set([x for x in range (0,len(nums)+1)])-set(nums))[0]


"""Approach:
- The approach was to create a set of all numbers from 0 to n
- Then convert the input list to a set
- Then subtract the two sets to find the missing number
- But upon closer inspection we can see that our approach will not check for the last number if it is missing
- So to handle that we create the set from 0 to n+1 instead of n and then subtract the two sets
- Finally we convert the resulting set to a list and return the first element as the missing number
"""