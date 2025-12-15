# 2848. Points That Intersect With Cars
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given a 0-indexed 2D integer array nums representing the coordinates of the cars parking on a number line. For any index i, nums[i] = [starti, endi] where starti is the starting point of the ith car and endi is the ending point of the ith car.

# Return the number of integer points on the line that are covered with any part of a car.

from typing import List
class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        flattend =[]
        for i in nums :
            flattend.extend([x for x in range (i[0],i[1]+1)])
        return len(set(flattend))
    

"""
Approach:
- First, I initialized an empty list flattend to store all the integer points covered by the cars.
- I then iterated over each car's coordinates in the nums list.
- For each car, I used a list comprehension to generate a list of all integer points from starti to endi (inclusive) and extended the flattend list with these points.
- After processing all cars, I converted the flattend list to a set to remove duplicate points, as some points may be covered by multiple cars.
- Finally, I returned the length of the set, which represents the total number of unique integer points covered by any car.
"""
