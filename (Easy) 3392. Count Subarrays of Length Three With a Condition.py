# 3392. Count Subarrays of Length Three With a Condition
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an integer array nums, return the number of subarrays of length 3 such that the sum of the first and third numbers equals exactly half of the second number.

 

class Solution:
    def countSubarrays(self, nums) -> int:
        # pointer = 0
        pointer2 = 2
        count=0
        for pointer in range (0,len(nums)-2):
            if((nums[pointer] + nums[pointer2])*2 == nums[pointer+1]):
                count+=1
            pointer2+=1
        return count

"""
Approach:
- We initialize a pointer2 to point to the third element of the subarray.
- We also initialize a count variable to keep track of how many subarrays satisfy the given conditions.
- Then we iterate through the array till third last element as we have pointer2 that is point 3 places ahead for the for loop pointer.
- For each position of the pointer, we check if the sum of the elements at pointer and pointer2 multiplied by 2 is equal to the element at pointer+1.
- which is the condition given in the problem.
- If the condition is satisfied, we increment the count.
- we return the count of such subarrays.
"""