# 2210. Count Hills and Valleys in an Array
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given a 0-indexed integer array nums. An index i is part of a hill in nums if the closest non-equal neighbors of i are smaller than nums[i]. Similarly, an index i is part of a valley in nums if the closest non-equal neighbors of i are larger than nums[i]. Adjacent indices i and j are part of the same hill or valley if nums[i] == nums[j].

# Note that for an index to be part of a hill or valley, it must have a non-equal neighbor on both the left and right of the index.

# Return the number of hills and valleys in nums.

from typing import List

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        j = 0
        k = 2
        i = 1
        while(True):
            if i == len(nums):
                break
            if nums[i] == nums[j]:
                nums.pop(i)
                continue
            else :
                i+=1
                j+=1
        count =0
        j=0
        for i in range (1 , len(nums)-1):
            if (nums[j] > nums [i] < nums[k]) or (nums[j] < nums [i] > nums[k]):
                count+=1
            j+=1
            k+=1

        return count


"""
Approach:
- So Initially I was just going to check three elements i,j,k but then contigious elements can be duplicates which will throw off the Logic.
- So I removed the contigiuous duplicates with .remove() function.
- Then I iterated through the modified array checking for hills and valleys by comparing three elements at a time.
- I initialized two pointers j and k to represent the left and right neighbors of the current index i.
- For each index i from 1 to len(nums)-2, I checked if the current element nums[i] is greater than both its neighbors (nums[j] and nums[k]) to identify a hill, or if it is less than both its neighbors to identify a valley.
- If either condition is met, I incremented the count of hills and valleys.
- This logic felt correct but later I found out that .remove() only removes the first occurence of the element.
- So I changed the logic to use .pop() which remove the element at the specified index.
- Finally, I returned the total count of hills and valleys found in the array.
"""