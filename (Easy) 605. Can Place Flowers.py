# 605. Can Place Flowers
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.


from ast import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        
        length = len(flowerbed)
        
        for i in range(length):
            if flowerbed[i] == 0:
                empty_left = (i == 0) or (flowerbed[i - 1] == 0)
                empty_right = (i == length - 1) or (flowerbed[i + 1] == 0)
                
                if empty_left and empty_right:
                    flowerbed[i] = 1      # mark as planted
                    n -= 1
                    if n == 0:
                        return True
        
        return False
    

"""
Approach:
- We first check if `n` is 0. If it is, we can immediately return `True` since no flowers need to be planted.
- We then get the length of the `flowerbed` array.
- We iterate through each plot in the `flowerbed` using a for loop.
- For each plot, we check if it is empty (0). If it is, we then check the adjacent plots:
  - We determine if the left plot is empty or if the current plot is the first plot (i.e., `i == 0`).
  - We determine if the right plot is empty or if the current plot is the last plot (i.e., `i == length - 1`).
- If both adjacent plots are empty, we can plant a flower in the current plot by setting it to 1 and decrementing `n` by 1.
- After planting a flower, we check if `n` has reached 0. If it has, we return `True`.
- If we finish iterating through the `flowerbed` and still have not planted all `n` flowers, we return `False`.
"""
