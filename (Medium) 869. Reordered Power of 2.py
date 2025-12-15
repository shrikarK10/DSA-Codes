# 869. Reordered Power of 2
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# You are given an integer n. We reorder the digits in any order (including the original order) such that the leading digit is not zero.

# Return true if and only if we can do this so that the resulting number is a power of two.


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        pow =["011237","0122579","012356789","0124","0134449", "0145678","01466788","0248","0368888","0469","1","112234778","11266777","122446","125","128","1289","13468","16","2","224588","23","23334455","234455668","23678","256","35566","4","46","8"]

        return "".join(sorted(str(n))) in pow


"""
Approach:
- We create a list `pow` that contains the sorted digit representations of all powers of 2 that can be formed with up to 10 digits (since n can be at most 10^9).
- We convert the input number `n` to a string, sort its digits, and join them back together to form a new string.
- We check if this sorted string representation of `n` exists in the `pow` list"""