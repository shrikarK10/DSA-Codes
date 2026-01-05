# 1390. Four Divisors
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors. If there is no such integer in the array, return 0.

from typing import List
import math

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        final = 0

        for i in nums:
            curr = 0
            count = 0
            limit = int(math.sqrt(i))

            for k in range(1, limit + 1):
                if i % k == 0:
                    d = i // k

                    if k == d:
                        curr += k
                        count += 1
                    else:
                        curr += k + d
                        count += 2

                    if count > 4:
                        break

            if count == 4:
                final += curr

        return final


"""
Approach:
- Initialize a variable 'final' to store the cumulative sum of divisors.
- Iterate through each number 'i' in the input list 'nums'.
- For each number, initialize 'curr' to store the sum of its divisors and 'count' to count the number of divisors.
- Calculate the integer square root of 'i' to limit the range of divisor checks.
- For each integer 'k' from 1 to the square root of 'i':
    - Check if 'k' is a divisor of 'i'.
    - If it is, calculate the corresponding divisor 'd' as 'i // k'.
    - If 'k' and 'd' are the same, add 'k' to 'curr' and increment 'count' by 1.
    - If they are different, add both 'k' and 'd' to 'curr' and increment 'count' by 2.
    - If at any point 'count' exceeds 4, break out of the loop early.
- After checking all potential divisors, if 'count' equals 4, add 'curr' to 'final'.
- Finally, return 'final' as the result.
"""