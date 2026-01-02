# 3232. Find if Digit Game Can Be Won
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given an array of positive integers nums.

# Alice and Bob are playing a game. In the game, Alice can choose either all single-digit numbers or all double-digit numbers from nums, and the rest of the numbers are given to Bob. Alice wins if the sum of her numbers is strictly greater than the sum of Bob's numbers.

# Return true if Alice can win this game, otherwise, return false.

from typing import List
class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single =[x for x in nums if x<10]
        double =[x for x in nums if x >=10]

        return sum(single) != sum(double)
    

"""
Approach:
- Create a list 'single' that contains all single-digit numbers from the input list 'nums'.
- Create a list 'double' that contains all double-digit numbers from the input list 'nums'.
- Calculate the sum of the 'single' list and the sum of the 'double' list.
- Return True if the sums are not equal, indicating that Alice can choose a set of numbers that gives her a strictly greater sum than Bob's. Otherwise, return False.
"""
