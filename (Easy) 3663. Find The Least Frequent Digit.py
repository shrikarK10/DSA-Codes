# 3663. Find The Least Frequent Digit
# Solved
# Easy

# Given an integer n, find the digit that occurs least frequently in its decimal representation. If multiple digits have the same frequency, choose the smallest digit.

# Return the chosen digit as an integer.

# The frequency of a digit x is the number of times it appears in the decimal representation of n.
 

from collections import Counter
class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        number = sorted(list(str(n)))
        freq = Counter(number)
        return int([key for key, value in freq.items() if value == min(freq.values())][0])






"""
Approach:
- Converting the given integer to a string for traversing every digit.
- Converting the string to a list for sorting so we can return the smallest digit in case of a same frequency.
- Using counter to count the frequency of each digit.
- Then we cant simply return the digit with minimum frequency , so we use a for loop to loop through the counter and find the key of minimul index value.
"""