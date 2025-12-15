# 1925. Count Square Sum Triples
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# A square triple (a,b,c) is a triple where a, b, and c are integers and a2 + b2 = c2.

# Given an integer n, return the number of square triples such that 1 <= a, b, c <= n.


import math
class Solution:
    def countTriples(self, n: int) -> int:
        count=0
        for i in range (3,n):
            for j in range (3,n):
                c = math.sqrt((i**2) + (j**2))
                if c == int(c) and c <= n:
                    count+=1
        return count


"""
Approach:
- I used a nested loop to iterate through all possible combinations of a and b.
- For each combination, I calculated the value of c using the Pythagorean theorem (c = sqrt(a^2 + b^2)).
- If Integer value of c is equal to c (Which means c is a square triple) and less than or equal to n and , I incremented the count.
- Finally, I returned the count as the result.
"""

