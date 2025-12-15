# 2540. Minimum Common Value
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.

# Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.



class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return -1




"""
Approach:
- I used a two-pointer approach to find the minimum common value.
- I initialized two pointers i and j to 0 and used a while loop to iterate through both arrays.
- If the elements at the current positions of both arrays are equal, I returned the element as it is the minimum common value.
- If the element at the current position of nums1 is less than the element at the current position of nums2, I incremented i.
- Otherwise, I incremented j.
- If no common value is found, I returned -1.
"""

