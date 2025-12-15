# 3461. Check If Digits Are Equal in String After Operations I
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given a string s consisting of digits. Perform the following operation repeatedly until the string has exactly two digits:

# For each pair of consecutive digits in s, starting from the first digit, calculate a new digit as the sum of the two digits modulo 10.
# Replace s with the sequence of newly calculated digits, maintaining the order in which they are computed.
# Return true if the final two digits in s are the same; otherwise, return false.

class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while(True):
            oped = ""
            if (len(s)==2):
                break
            for j in range (0,len(s)-1):
                oped += str((int(s[j]) + int(s[j+1]) ) % 10)
            s = oped
        if s[0]==s[1]:
            return True
        else:
            return False


"""
Approach:
- I used a while loop to repeatedly perform the operations until the string has exactly two digits.
- Inside the loop, I initialized an empty string oped to store the newly calculated digits.
- I checked if the length of the string s is 2; if so, I broke out of the loop.
- I used a for loop to iterate through the string s, calculating the sum of each pair of consecutive digits modulo 10 and appending the result to oped.
- After processing all pairs, I replaced s with oped.
- Once the loop ended, I compared the final two digits in s.
- If they are the same, I returned True; otherwise, I returned False.
- The time complexity of this approach is O(n^2) in the worst case, where n is the length of the input string s. This is because, in each iteration of the while loop, we are creating a new string that is one character shorter than the previous string, leading to a series of operations that sum up to O(n^2).
- The space complexity is O(n) as well, since we are creating new strings during each iteration of the while loop.
"""                 