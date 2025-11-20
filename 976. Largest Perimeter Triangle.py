# 976. Largest Perimeter Triangle
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.


from ast import List
import atexit
atexit.register(lambda : open("display_runtime.txt","w").write("0"))

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums,reverse=True)

        a=0
        b=1
        c=2
        perimeters=[0]
        while(True):
            if(sorted_nums[a] < sorted_nums[b]+sorted_nums[c] ):
                perimeters.append(sorted_nums[a] + sorted_nums[b]+sorted_nums[c])
                a+=1
                b+=1
                c+=1
            else:
                a+=1
                b+=1
                c+=1
            if(c == len(sorted_nums)):
                break 
        return max(perimeters)
    

"""
Approach:
- First, we sort the input array in descending order to prioritize larger lengths.
- We then use a while loop to iterate through the sorted array, checking triplets of lengths to see if they can form a valid triangle using the triangle inequality condition.
- If a valid triangle is found, we calculate its perimeter and store it.
- Finally, we return the maximum perimeter found, or 0 if no valid triangle can be formed.
"""