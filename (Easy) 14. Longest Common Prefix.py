# 14. Longest Common Prefix
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        f=""
        c=strs[0]
        if len(strs)==1:return c
        for i in range (0,len(c)):
            prefix = c[:i+1]
            flag = False
            for j in strs[1:]:
                if prefix == j[:i+1] :
                    flag =True
                    continue
                else:
                    flag = False
                    break
            if flag == False:
                return c[:i]
        return c


"""
Approach:
- Initialize an empty string 'f' to store the longest common prefix.
- Assign the first string in the list 'strs' to variable 'c'.
- If the length of 'strs' is 1, return 'c' as the longest common prefix.
- Iterate through each character index 'i' of the string 'c':
    - Create a substring 'prefix' that includes characters from the start of 'c' up to index 'i'.
    - Initialize a boolean flag 'flag' to track if the current prefix matches all other strings.
    - For each string 'j' in 'strs' starting from the second string:
        - Compare the current 'prefix' with the substring of 'j' up to index 'i'.
        - If they match, set 'flag' to True and continue to the next string.
        - If they do not match, set 'flag' to False and break out of the loop.
    - After checking all strings, if 'flag' is False, return the substring of 'c' up to index 'i' as the longest common prefix.
""" 