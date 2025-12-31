# 771. Jewels and Stones
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

# Letters are case sensitive, so "a" is considered a different type of stone from "A".


from collections import Counter
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freq = Counter(stones)
        g=0
        for i in jewels :
            g+=freq[i]
        return g


"""
Approach:
- Use the Counter class from the collections module to count the frequency of each stone in the stones string.
- Initialize a variable g to keep track of the total number of jewels found in stones.
- Iterate through each character in the jewels string.
- For each jewel, add its frequency from the freq Counter to g.
- Finally, return the total count g.
"""
