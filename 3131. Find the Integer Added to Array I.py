# 3131. Find the Integer Added to Array I
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given two arrays of equal length, nums1 and nums2.

# Each element in nums1 has been increased (or decreased in the case of negative) by an integer, represented by the variable x.

# As a result, nums1 becomes equal to nums2. Two arrays are considered equal when they contain the same integers with the same frequencies.

# Return the integer x.


from typing import List


class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()

        return nums2[0] - nums1[0]
    


"""
Approach:
- First, I sorted both input lists nums1 and nums2 to ensure that the elements are in the same order.
- Since both arrays are equal in length and differ by a constant integer x, the difference between the first elements of the sorted arrays will give us the value of x.
- I calculated the difference by subtracting the first element of nums1 from the first element of nums2.
- Finally, I returned the calculated difference as the result.
"""
