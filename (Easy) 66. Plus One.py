# 66. Plus One
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.


from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x = int("".join(map(str,digits)))
        return list(map(int,str(x+1)))
    

"""
Approach:
- Convert the list of digits into a string by mapping each digit to a string and joining them together.
- Convert the resulting string into an integer.
- Increment the integer by one.
- Convert the incremented integer back into a string, then map each character back to an integer and convert it into a list.
- Return the final list of digits.
"""
