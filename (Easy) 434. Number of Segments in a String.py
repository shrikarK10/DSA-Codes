# 434. Number of Segments in a String
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given a string s, return the number of segments in the string.

# A segment is defined to be a contiguous sequence of non-space characters.




class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())


"""
Approach:
- I used a simple approach to count the number of segments in the string.
- I used the split() method to split the string into segments based on spaces.
- I returned the length of the resulting list as the count of segments.
"""
