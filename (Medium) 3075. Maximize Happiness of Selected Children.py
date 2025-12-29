# 3075. Maximize Happiness of Selected Children
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# You are given an array happiness of length n, and a positive integer k.

# There are n children standing in a queue, where the ith child has happiness value happiness[i]. You want to select k children from these n children in k turns.

# In each turn, when you select a child, the happiness value of all the children that have not been selected till now decreases by 1. Note that the happiness value cannot become negative and gets decremented only if it is positive.

# Return the maximum sum of the happiness values of the selected children you can achieve by selecting k children.


from typing import List

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        max_hapi=0
        for i in range (0,k):
            max_hapi += max(happiness[i] - i, 0 )
        return max_hapi
    

"""
Approach:
- First, sort the happiness array in descending order to prioritize children with higher happiness values.
- Initialize a variable max_hapi to keep track of the maximum happiness sum.
- Iterate through the first k children in the sorted happiness array.
- For each child, calculate the effective happiness value after considering the decrement due to previous selections (i.e., happiness[i] - i).
- Use max(happiness[i] - i, 0) to ensure that the happiness value does not go below zero.
- Accumulate the effective happiness values into max_hapi.
- Finally, return max_hapi as the maximum sum of happiness values for the selected children.
"""