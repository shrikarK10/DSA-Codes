# 2549. Count Distinct Numbers on Board
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given a positive integer n, that is initially placed on a board. Every day, for 109 days, you perform the following procedure:

# For each number x present on the board, find all numbers 1 <= i <= n such that x % i == 1.
# Then, place those numbers on the board.
# Return the number of distinct integers present on the board after 109 days have elapsed.

# Note:

# Once a number is placed on the board, it will remain on it until the end.
# % stands for the modulo operation. For example, 14 % 3 is 2.

class Solution:
    def distinctIntegers(self, n: int) -> int:
        if n==1:return 1
        else: return n-1
    
"""
Approach:
- If n is 1, the only number on the board is 1 itself, so we return 1.
- For any n greater than 1, we can always generate all integers from 1 to n-1 through the given procedure.
- Therefore, for n > 1, the number of distinct integers on the board after 10^9 days will be n-1.
- Thus, we return n-1 for n > 1.
"""