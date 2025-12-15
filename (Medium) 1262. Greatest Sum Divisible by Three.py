# 1262. Greatest Sum Divisible by Three
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given an integer array nums, return the maximum possible sum of elements of the array such that it is divisible by three.

from typing import List
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        sum1 = sum(nums)
        
        div1=sorted([ i for i in nums if i % 3 == 1])
        div2=sorted([ i for i in nums if i % 3 == 2])

        if sum1 % 3 == 0:
            return sum1
        elif sum1 % 3 == 1:
            if (len(div2) >= 2 and len(div1) >= 1):
                return sum1 - min(div1[0], div2[0]+div2[1])
            elif (len(div2)<2):
                return sum1 - div1[0]
            else: 
                return sum1 - (div2[0]+div2[1])
        else:
            if (len(div1) >= 2 and len(div2) >= 1):
                return sum1 - min(div2[0], div1[0]+div1[1])
            elif (len(div1) < 2):
                return sum1 - div2[0]
            else:
                return sum1 - (div1[0]+div1[1])
        if len(nums) < 2:
            return 0
        
"""
Approach:
- Initially , I thought lets just sort the original array and try to remove the smallest elements until the sum becomes divisible by 3.
- However, this approach does not guarantee the maximum sum that is divisible by 3, as removing the smallest elements may not always lead to the optimal solution.
- Then I realized by looking at a example that remainder whn divided by 3 will be either 0,1 or 2.
- Then I also realized that to elements who have remainder 1 and two elements who have remainder 2 can be removed to make the sum divisible by 3 when the remainder of total sum is 1.
- Same way when the remainder of total sum is 2 , we can remove one element with remainder 2 or two elements with remainder 1.
- So I created two separate lists div1 and div2 to store elements with remainder 1 and 2 respectively when divided by 3.
- Then I checked the remainder of total sum when divided by 3.
- Based on the remainder value (0, 1, or 2), I applied the appropriate logic to remove elements from div1 or div2 to make the sum divisible by 3 while maximizing the sum.
- Finally, I returned the maximum sum that is divisible by 3.
"""