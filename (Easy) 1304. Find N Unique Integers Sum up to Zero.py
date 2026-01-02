# 1304. Find N Unique Integers Sum up to Zero
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an integer n, return any array containing n unique integers such that they add up to 0.


from typing import List

class Solution:
    def sumZero(self, n: int) -> List[int]:
        z=[]
        x=n
        while(len(z)<n):
            if x==1:
                z.append(0)
                break
            z.append(-(x//2))
            z.append(x//2)
            x-=2
        return z



"""
Approach:
- Initialize an empty list z to store the unique integers.
- Set a variable x equal to n to keep track of how many integers we need to add.
- Use a while loop that continues until the length of z is less than n.
- Inside the loop, check if x is equal to 1. If it is, append 0 to z and break the loop.
- If x is not 1, append the negative and positive halves of x to z.
- Decrease x by 2 to account for the two integers added.
- Finally, return the list z containing n unique integers that sum up to zero.
"""
