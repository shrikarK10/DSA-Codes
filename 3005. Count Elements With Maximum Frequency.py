# 3005. Count Elements With Maximum Frequency
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given an array nums consisting of positive integers.

# Return the total frequencies of elements in nums such that those elements all have the maximum frequency.

# The frequency of an element is the number of occurrences of that element in the array.

from typing import List

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = {}
        unique_val = list(set(nums))

        for i in unique_val:
            freq[i] = nums.count(i)

        mx=max(list(freq.values()))
        count=0
        for i in freq:
            if freq[i] == mx:
                count+=1
        return mx*count


"""
Approach:
- We start by initializing an empty dictionary freq to store the frequency of each unique element in the array.
- We create a list unique_val that contains all the unique elements in the input array nums by converting it to a set and then back to a list.
- We iterate through each unique element i in unique_val and calculate its frequency in the original array nums using the count() method. We store this frequency in the freq dictionary with the element as the key and its frequency as the value.
- After populating the freq dictionary, we find the maximum frequency mx by taking the maximum value from the list of frequencies in the freq dictionary.
- We initialize a counter count to keep track of how many elements have this maximum frequency.
- We iterate through the keys in the freq dictionary and check if their frequency is equal to mx. If it is, we increment the count by 1.
- Finally, we return the product of mx and count, which gives us the total frequencies of elements that have the maximum frequency in the array.
"""
