# 942. DI String Match
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# A permutation perm of n + 1 integers of all the integers in the range [0, n] can be represented as a string s of length n where:

# s[i] == 'I' if perm[i] < perm[i + 1], and
# s[i] == 'D' if perm[i] > perm[i + 1].
# Given a string s, reconstruct the permutation perm and return it. If there are multiple valid permutations perm, return any of them


from typing import List

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        x = [i for i in range(0 , len(s)+1)]
        re=[]

        for i in s :
            if i == 'I':
                re.append(x[0])
                x = x[1:]
            elif i =='D':
                re.append(x[len(x)-1])
                x = x[:-1]
            
        re.append(x[0])
        return re



"""
Approach:
- We start by creating a list x that contains all integers from 0 to n (where n is the length of the input string s). This list represents the available numbers for constructing the permutation.
- We initialize an empty list re to store the resulting permutation.
- We iterate through each character i in the input string s.
- If the character is 'I', we append the smallest available number (the first element of x) to the result list re and remove that number from x.
- If the character is 'D', we append the largest available number (the last element of x) to the result list re and remove that number from x.
- After processing all characters in s, there will be one number left in x. We append this remaining number to the result list re.
- Finally, we return the result list re, which contains the reconstructed permutation that satisfies the conditions defined by the input string s.
"""
