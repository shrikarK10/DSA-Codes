# 2283. Check if Number Has Equal Digit Count and Digit Value
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given a 0-indexed string num of length n consisting of digits.

# Return true if for every index i in the range 0 <= i < n, the digit i occurs num[i] times in num, otherwise return false.

class Solution:
    def digitCount(self, num: str) -> bool:
        for i in range(0,len(num)):
            if num.count(str(i)) != int(num[i]) :
                return False
        return True

"""
Approach:
- I used a for loop to iterate through the string num.
- For each index i, I checked if the count of the digit i in the string num is equal to the value of num[i].
- If the count is not equal to the value of num[i], I returned False.
- If the count is equal to the value of num[i], I returned True.
"""
