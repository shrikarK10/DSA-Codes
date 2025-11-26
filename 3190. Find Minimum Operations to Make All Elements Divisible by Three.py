# 3190. Find Minimum Operations to Make All Elements Divisible by Three
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given an integer array nums. In one operation, you can add or subtract 1 from any element of nums.

# Return the minimum number of operations to make all elements of nums divisible by 3.


from typing import List
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count =0
        for i in nums :
            x = i % 3
            if x==1:
                count+=1
            elif x==2:
                count+=1
        return count


"""
Approach:
- We need to make all elements of the array divisible by 3.
- For each element in the array, we check its remainder when divided by 3 using the modulus operator (%).
- If the remainder is 0, the element is already divisible by 3, and we do not need to perform any operations.
- If the remainder is 1, we can either add 2 or subtract 1 to make it divisible by 3. In both cases, it takes 1 operation.
- If the remainder is 2, we can either add 1 or subtract 2 to make it divisible by 3. Again, it takes 1 operation.
- We maintain a count of the total number of operations needed.
- Finally, we return the total count of operations required to make all elements divisible by 3.
"""
