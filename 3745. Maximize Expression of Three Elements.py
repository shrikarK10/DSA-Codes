# 3745. Maximize Expression of Three Elements
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given an integer array nums.

# Choose three elements a, b, and c from nums at distinct indices such that the value of the expression a + b - c is maximized.

# Return an integer denoting the maximum possible value of this expression.


class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        a = max(nums)
        nums.remove(a)
        b = max(nums)
        c = min(nums)
        return a+b-c


"""
Approach:
- I used a simple approach to maximize the expression a + b - c.
- I first found the maximum value in the nums array and stored it in a.
- Then, I removed the maximum value from the nums array.
- Next, I found the maximum value in the modified nums array and stored it in b.
- Finally, I found the minimum value in the modified nums array and stored it in c.
- I returned the value of a + b - c as the result.
"""
