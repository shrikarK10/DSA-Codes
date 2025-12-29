# 1351. Count Negative Numbers in a Sorted Matrix
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

from narwhals import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count=0
        for i in range (0,len(grid)):
            for j in range (0,len(grid[0])):
                if grid[i][j] < 0 :
                    count+=1
        return count
    

"""
Approach:
- Initialize a counter to keep track of negative numbers.
- Iterate through each element in the matrix using nested loops.
- For each element, check if it is negative. If it is, increment the counter.
- After checking all elements, return the counter as the result
"""