# 3000. Maximum Area of Longest Diagonal Rectangle
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given a 2D 0-indexed integer array dimensions.

# For all indices i, 0 <= i < dimensions.length, dimensions[i][0] represents the length and dimensions[i][1] represents the width of the rectangle i.

# Return the area of the rectangle having the longest diagonal. If there are multiple rectangles with the longest diagonal, return the area of the rectangle having the maximum area.


from typing import List
import math
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        diags =[]
        max_ind=[]
        areas=[]
        for i in dimensions :
            diags.append(math.sqrt((i[0]**2)+(i[1]**2)))
        
        ind_m = diags.index(max(diags))
        for i in range(ind_m,len(diags)):
            if (diags[ind_m]==diags[i]):
                max_ind.append(i)
        
        for i in max_ind :
            areas.append(dimensions[i][0]*dimensions[i][1])
        
        return max(areas)
    

"""
Approach:
- I started by initializing three empty lists: diags to store the lengths of the diagonals, max_ind to store the indices of rectangles with the maximum diagonal length, and areas to store the areas of those rectangles.
- I then iterated through each rectangle in the dimensions list.
- For each rectangle, I calculated the length of its diagonal using the Pythagorean theorem (sqrt(length^2 + width^2)) and appended it to the diags list.
- After calculating the diagonals for all rectangles, I found the index of the maximum diagonal length in the diags list.
- I then iterated through the diags list starting from the index of the maximum diagonal length to find all rectangles that have the same maximum diagonal length and stored their indices in the max_ind list.
- Next, I calculated the area of each rectangle corresponding to the indices in max_ind and stored these areas in the areas list.
- Finally, I returned the maximum area from the areas list.
"""