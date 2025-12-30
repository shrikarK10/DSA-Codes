# 1523. Count Odd Numbers in an Interval Range
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2 !=0 and high % 2 != 0:
            return (((high - low)+1)//2)+1
        else:
            return (((high - low)+1)//2)


"""
Approach:
- Check if both low and high are odd numbers.
- If both are odd, calculate the count of odd numbers using the formula ((high - low) + 1) // 2 + 1.
- If either low or high is even, calculate the count of odd numbers using the formula ((high - low) + 1) // 2.
- Return the calculated count of odd numbers.
"""
