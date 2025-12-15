# 3228. Maximum Number of Operations to Move Ones to the End
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# You are given a binary string s.

# You can perform the following operation on the string any number of times:

# Choose any index i from the string where i + 1 < s.length such that s[i] == '1' and s[i + 1] == '0'.
# Move the character s[i] to the right until it reaches the end of the string or another '1'. For example, for s = "010010", if we choose i = 1, the resulting string will be s = "000110".
# Return the maximum number of operations that you can perform.

class Solution:
    def maxOperations(self, s: str) -> int:
        count_one=0
        prev ="-1"
        ops =0
        for i in range (0,len(s)):
            if(s[i]=="1" and prev =="1"):
                count_one +=1
                prev =s[i]
            elif((s[i]=="1" or i+1 == len(s)) and (prev == "0" or i+1 ==len(s))):
                ops+=count_one
                count_one+=1
                prev=s[i]
            elif(s[i]=="1" and prev=="-1"):
                count_one = 1
                prev = s[i]
            else:
                prev=s[i]
                continue
        return ops      


# Same approach with cleaner code and less conditions
class Solution:
    def maxOperations(self, s: str) -> int:
        count_one = 0
        ops = 0
        n = len(s)
        for i, ch in enumerate(s):
            if ch == '1':
                count_one += 1
            else:
                if i + 1 == n or s[i + 1] == '1':
                    ops += count_one
        return ops      
    
"""
Approach:
- We will traverse the string whilw keeping tracks of number of ones and previos element.
- The approach is to add the number of ones encountered so far to the operations count whenever we encounter a zero after one or reach the end of string after one.
- This is because each one can be moved past the zero or to the end of the string.
- We also handle the case when we encounter consecutive ones by just incrementing the count of ones
- Finally we return the total operations count.
"""