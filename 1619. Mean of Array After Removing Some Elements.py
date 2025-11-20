# 1619. Mean of Array After Removing Some Elements
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an integer array arr, return the mean of the remaining integers after removing the smallest 5% and the largest 5% of the elements.

# Answers within 10-5 of the actual answer will be considered accepted.


class Solution(object):
    def trimMean(self, arr):
        """
        :type arr: List[int]
        :rtype: float
        """
        
        arr.sort()
        arr = arr[int(len(arr) * 0.05):-int(len(arr) * 0.05)]
        return float(sum(arr))/float(len(arr))


"""
Approach:
- First we sort the array to easily remove the smallest and largest elements.
- Then we slice the array to remove the smallest 5% and largest 5% of elements.
- Finally we calculate the mean of the remaining elements by dividing the sum of the elements by the number of elements and return the result.
"""