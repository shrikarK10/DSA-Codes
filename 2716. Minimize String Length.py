# 2716. Minimize String Length
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given a string s, you have two types of operation:

# Choose an index i in the string, and let c be the character in position i. Delete the closest occurrence of c to the left of i (if exists).
# Choose an index i in the string, and let c be the character in position i. Delete the closest occurrence of c to the right of i (if exists).
# Your task is to minimize the length of s by performing the above operations zero or more times.

# Return an integer denoting the length of the minimized string.


class Solution:
    def minimizedStringLength(self, s: str) -> int:
        return len(set(s))


"""
Approach:
- Problem looks decently complicated given the conditions.
- But if we take a closer look , it is basically remove dublicate characters from the string.
- So we can use a set to store unique characters from the string.
- Finally, we return the length of the set which gives us the minimized string length.
"""