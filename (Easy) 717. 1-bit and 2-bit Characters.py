# 717. 1-bit and 2-bit Characters
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# We have two special characters:

# The first character can be represented by one bit 0.
# The second character can be represented by two bits (10 or 11).
# Given a binary array bits that ends with 0, return true if the last character must be a one-bit character.


from typing import List
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        count_one = 0 
        if len(bits) ==1: return True
        for i in range (-2,-len(bits)-1,-1):
            if bits[i]==1:
                count_one+=1
            if bits[i]==0 or i ==-len(bits):
                if count_one % 2 == 0 :
                    return True
                else :
                    return False

"""
Approach:
- I looked at the description and noticed that the last character is always a one-bit character (0).
- And the approach was to traverse the array from the second last element (as we know the last is always 0) to the next zero or the start of the array.
- I initialized a counter count_one to keep track of the number of consecutive 1s encountered.
- As I traversed the array backwards, I incremented the count_one each time I encountered a 1.
- When I encountered a 0 or reached the start of the array, I checked the count_one.
- If count_one is even, it means the last character is a one-bit character, so I returned True.
- If count_one is odd, it means the last character is part of a two-bit character, so I returned False.
"""