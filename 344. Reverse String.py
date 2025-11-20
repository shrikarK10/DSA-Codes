# 344. Reverse String
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.




from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:]=s[::-1]


"""
Approach:
- The problem is straightforward, we need to reverse the input list of characters in place.
- I used Python's slicing feature to reverse the list.
- s[::-1] creates a reversed copy of the list s.
- Then I assigned this reversed list back to s using s[:] = s[::-1] to modify the original list in place.
- This approach has a time complexity of O(n) and a space complexity of O(1) since we are modifying the list in place.
- This is a concise and efficient way to reverse a list in Python.
"""