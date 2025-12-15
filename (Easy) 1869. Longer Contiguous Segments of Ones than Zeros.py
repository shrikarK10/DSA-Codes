# 1869. Longer Contiguous Segments of Ones than Zeros
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given a binary string s, return true if the longest contiguous segment of 1's is strictly longer than the longest contiguous segment of 0's in s, or return false otherwise.

# For example, in s = "110100010" the longest continuous segment of 1s has length 2, and the longest continuous segment of 0s has length 3.
# Note that if there are no 0's, then the longest continuous segment of 0's is considered to have a length 0. The same applies if there is no 1's.



class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        ones=[0]
        zeroes=[0]
        zero=0
        one=0
        for i in range(0,len(s)) :
            if s[i] == "1":
                one+=1
                if zero > 0:
                    zeroes.append(zero)
                    zero=0
            elif s[i] == "0":
                zero+=1
                if one>0:
                    ones.append(one)
                    one=0
            if i == len(s) - 1 and (zero!=0 or one!=0):
                zeroes.append(zero)
                ones.append(one)
        return max(ones) > max(zeroes) 
    


"""
Approach:
- We initialize two lists, ones and zeroes, to keep track of the lengths of contiguous segments of 1's and 0's respectively.
- We also initialize two counters, one and zero, to count the current lengths of contiguous segments of 1's and 0's.
- We iterate through each character in the string s.
- If the character is '1', we increment the one counter and check if there was a contiguous segment of 0's before it. If so, we append the length of that segment to the zeroes list and reset the zero counter.
- If the character is '0', we increment the zero counter and check if there was a contiguous segment of 1's before it. If so, we append the length of that segment to the ones list and reset the one counter.
- At the end of the iteration, we check if there are any remaining counts in the one or zero counters and append them to their respective lists.
- Finally, we compare the maximum lengths of contiguous segments of 1's and 0's and return true if the maximum length of 1's is greater than that of 0's, otherwise return false.
"""