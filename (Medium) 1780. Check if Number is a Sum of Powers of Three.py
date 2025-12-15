# 1780. Check if Number is a Sum of Powers of Three
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given an integer n, return true if it is possible to represent n as the sum of distinct powers of three. Otherwise, return false.
# An integer y is a power of three if there exists an integer x such that y == 3x.


class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while (True):
            rem = n % 3
            if rem > 1 : 
                return False
            n = n // 3
            if n == 0:
                return True


"""
Approach:
- The problem can be solved by checking the base-3 representation of the number n.
- In base-3, a number can be represented using the digits 0, 1, and 2.
- If any digit in the base-3 representation is 2, it means that the number cannot be expressed as a sum of distinct powers of three, since we would need to use the same power of three more than once.
- Therefore, we can repeatedly divide the number n by 3 and check the remainder.
- If the remainder is 2 at any point, we return False.
- If we reach 0 without encountering a remainder of 2, we return True.
- The while loop continues until we either find a remainder of 2 or reduce n to 0.
- This approach has a time complexity of O(log n) since we are dividing n by 3 in each iteration.
"""
