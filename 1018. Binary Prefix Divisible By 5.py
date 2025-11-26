# 1018. Binary Prefix Divisible By 5
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given a binary array nums (0-indexed).

# We define xi as the number whose binary representation is the subarray nums[0..i] (from most-significant-bit to least-significant-bit).

# For example, if nums = [1,0,1], then x0 = 1, x1 = 2, and x2 = 5.
# Return an array of booleans answer where answer[i] is true if xi is divisible by 5.

from typing import List
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        s = "".join([str(x) for x in nums])
        total_numbers_flag = []

        for i in range (0,len(nums)):
            x=int(s[:i+1] , 2)
            if x % 5 == 0:
                total_numbers_flag.append(True)
            else:
                total_numbers_flag.append(False)
        return total_numbers_flag
    


"""
Approach:
- First, we convert the binary array into a string representation of the binary number.
- We initialize an empty list total_numbers_flag to store the boolean results.
- We iterate through each index i of the binary array nums.
- For each index i, we extract the substring of the binary string from the start to index i (inclusive) and convert it to its decimal equivalent using int(s[:i+1], 2).
- We then check if the decimal number is divisible by 5 using the modulus operator (%).
- If the number is divisible by 5, we append True to the total_numbers_flag list; otherwise, we append False.
- Finally, we return the total_numbers_flag list containing the boolean results for each prefix.
"""
