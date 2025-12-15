# 3194. Minimum Average of Smallest and Largest Elements
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You have an array of floating point numbers averages which is initially empty. You are given an array nums of n integers where n is even.

# You repeat the following procedure n / 2 times:

# Remove the smallest element, minElement, and the largest element maxElement, from nums.
# Add (minElement + maxElement) / 2 to averages.
# Return the minimum element in averages.

from ast import List


class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        average = 9999
        while nums:
            avg_curr = (nums[0] + nums[len(nums)-1]) / 2
            if (avg_curr < average):
                average = avg_curr
            nums.remove(nums[0])
            nums.remove(nums[len(nums)-1])

        return average
    

"""
Approach:
- First, I sorted the input list nums to easily access the smallest and largest elements.
- I initialized a variable average with a large value to keep track of the minimum average found.
- I used a while loop to repeatedly remove the smallest and largest elements from nums until it is empty.
- In each iteration, I calculated the average of the smallest and largest elements.
- I compared this average with the current minimum average and updated it if the new average is smaller.
- I removed the smallest and largest elements from nums using the remove method.
- Finally, I returned the minimum average found.
"""
