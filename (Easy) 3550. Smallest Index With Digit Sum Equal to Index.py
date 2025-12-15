# 3550. Smallest Index With Digit Sum Equal to Index
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given an integer array nums.

# Return the smallest index i such that the sum of the digits of nums[i] is equal to i.

# If no such index exists, return -1.


class Solution:
    def smallestIndex(self, nums: List[int]) -> int:

        #With string conversion (slower -> 4 to 7 ms)

        # for i in range (0,len(nums)):
        #     s = list(str(nums[i]))
        #     n=0
        #     for j in range(0,len(s)):
        #         n+=int(s[j])
        #     if n == i:
        #         return i
        # return -1

"""
Approach:
- Convert each number in the nums to string and string to list for better iteration.
- Then iterate over the list of converted number and convert them into integer for addition.
- If the sum of the digits of nums[i] is equal to i then return i.(Initially I was checking till the end of the array if any next element is smaller than the currently found element but if you look carefully you can see that the first element which satisfies the condition is the smallest index)
- If no such index exists, return -1.
- This is a slower approach as multiple conversions are required.
"""

        # with modulo (Faster -> 0 ms)

        for i , n in enumerate (nums):
            s=0
            while(n > 0):
                s+=n%10
                n = n//10
            if s == i : return i
        return -1

"""
Approach:
- Iterate over the array and for each element find the sum of its digits using modulo and division.
- If the sum of the digits of nums[i] is equal to i then return i.(Initially I was checking till the end of the array if any next element is smaller than the currently found element but if you look carefully you can see that the first element which satisfies the condition is the smallest index)
- If no such index exists, return -1.
- This is a faster approach as we are not converting the number to string and then to list and then to integer.
""
            