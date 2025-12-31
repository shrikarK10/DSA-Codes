# 2022. Convert 1D Array Into 2D Array
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given a 0-indexed 1-dimensional (1D) integer array original, and two integers, m and n. You are tasked with creating a 2-dimensional (2D) array with  m rows and n columns using all the elements from original.

# The elements from indices 0 to n - 1 (inclusive) of original should form the first row of the constructed 2D array, the elements from indices n to 2 * n - 1 (inclusive) should form the second row of the constructed 2D array, and so on.

# Return an m x n 2D array constructed according to the above procedure, or an empty 2D array if it is impossible.



from typing import List

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n != len(original):
            return []    
        arr=[]
        i=0
        while(True):
            if i >= len(original):
                return arr
            arr.append(original[i:i+n])
            i+=n


"""
Approach:
- First, check if the product of m and n equals the length of the original array. If not, return an empty array.
- Initialize an empty list arr to hold the 2D array.
- Use a while loop to iterate through the original array in steps of n.
- In each iteration, append a slice of the original array (from index i to i+n) to arr.
- Increment i by n to move to the next row.
- Continue this process until all elements from the original array are used.
"""