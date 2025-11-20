# 2784. Check if Array is Good
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given an integer array nums. We consider an array good if it is a permutation of an array base[n].

# base[n] = [1, 2, ..., n - 1, n, n] (in other words, it is an array of length n + 1 which contains 1 to n - 1 exactly once, plus two occurrences of n). For example, base[1] = [1, 1] and base[3] = [1, 2, 3, 3].

# Return true if the given array is good, otherwise return false.

# Note: A permutation of integers represents an arrangement of these numbers.


from ast import List


class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums_sorted = sorted(nums)

        for i in range (1,len(nums_sorted)):
            if(i==nums_sorted[i-1]):
                continue
            else:
                return False
        
        if(nums_sorted[-1] == len(nums_sorted)-1 ):
            return True
        else:
            return False



"""
Approach:
- We first sort the input array `nums` to get `nums_sorted`.
- We then iterate through the sorted array starting from index 1 to the end of the array.
- For each index `i`, we check if the value at `nums_sorted[i-1]` is equal to `i`. This checks if the numbers from 1 to n-1 are present exactly once.
- If we find any number that does not match this condition, we return `False` immediately.
- After the loop, we check if the last element of the sorted array is equal to the length of the array minus 1. This checks if the number n appears exactly twice.
- If both conditions are satisfied, we return `True`, indicating that the array is good. Otherwise, we return `False`.
"""