# 242. Valid Anagram
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(list(s)) == sorted(list(t))


"""
Approach:
- Convert both strings into lists of characters.
- Sort both lists.
- Compare the sorted lists; if they are equal, t is an anagram of s.
- Return the result of the comparison.
"""