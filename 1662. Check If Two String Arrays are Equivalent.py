# 1662. Check If Two String Arrays are Equivalent
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

# A string is represented by an array if the array elements concatenated in order forms the string.


from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1) == "".join(word2)


"""
Approach:
- We use the `join` method to concatenate all the strings in the `word1` array into a single string.
- We do the same for the `word2` array.
- We then compare the two resulting strings using the equality operator `==`.
- If the two strings are equal, we return `True`; otherwise, we return `False`.
"""
