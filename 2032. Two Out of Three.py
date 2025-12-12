# 2032. Two Out of Three
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given three integer arrays nums1, nums2, and nums3, return a distinct array containing all the values that are present in at least two out of the three arrays. You may return the values in any order.
 


class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        atleast_two = []
        for i in range (0,len(nums1)):
            if nums1[i] in nums2 :
                atleast_two.append(nums1[i])
            elif nums1[i] in nums3:
                atleast_two.append(nums1[i])

        for i in range (0,len(nums2)):
            if nums2[i] in nums3:
                atleast_two.append(nums2[i])
        return list(set(atleast_two))



"""
Approach:
- I used a simple approach to find the values that are present in at least two out of the three arrays.
- I initialized an empty list called atleast_two to store the values that are present in at least two out of the three arrays.
- I used a for loop to iterate through the nums1 array.
- For each element in nums1, I checked if it is present in nums2 or nums3.
- If it is present in nums2 or nums3, I appended it to the atleast_two list.
- Next, I used another for loop to iterate through the nums2 array.
- For each element in nums2, I checked if it is present in nums3.
- If it is present in nums3, Its already in the list so I skipped it.
- Finally, I returned the list of distinct values that are present in at least two out of the three arrays.
"""

