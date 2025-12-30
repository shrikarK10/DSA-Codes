# 3226. Number of Bit Changes to Make Two Integers Equal
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given two positive integers n and k.

# You can choose any bit in the binary representation of n that is equal to 1 and change it to 0.

# Return the number of changes needed to make n equal to k. If it is impossible, return -1.



class Solution:
    def minChanges(self, n: int, k: int) -> int:
        nb = bin(n)[2:]
        kb = bin(k)[2:]
        n=len(nb)
        if len(kb)<n:
            kb='0'*(n-len(kb))+kb
        count =0
        for i in range (0,n):
            if (nb[i] == '1') and (kb[i]=='0') :
                nb = nb[:i] +'0'+nb[i+1:]
                count+=1
        if nb==kb:
            return count
        else:
            return -1


"""
Approach:
- Convert both integers n and k to their binary string representations.
- We have to use padding the ensure that the index does not go out of range.
- Loop through each bit of n and k.
- If a bit in n is '1' and the corresponding bit in k is '0', we need to change that bit in n to '0' and increment the count of changes.
- After processing all bits, check if the modified n equals k.
- If they are equal, return the count of changes; otherwise, return -1 indicating it's impossible to make n equal to k.
"""