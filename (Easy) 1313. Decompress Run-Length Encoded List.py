# 1313. Decompress Run-Length Encoded List
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# We are given a list nums of integers representing a list compressed with run-length encoding.

# Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).  For each such pair, there are freq elements with value val concatenated in a sublist. Concatenate all the sublists from left to right to generate the decompressed list.

# Return the decompressed list.

from typing import List

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result =[]
        for i in range(0,len(nums),2):
            freq = nums[i]
            val= nums[i+1]
            result.extend([val]*freq)
        return result


"""
Approach:
- So intially I didn't know that we can use [val]*freq to create a list with freq number of val.
- So I was using string multiplication concept to create a string of val repeated freq times and then converting it to list and then mapping it to int.
- But then I realized that we can directly use [val]*freq to create a list with freq number of val.
- So I iterated through the nums list with a step of 2 to get each pair of freq and val.
- For each pair, I created a list with freq number of val using [val]*freq
- Then I used the extend method to add this list to the result list.
- Finally, I returned the result list.
"""