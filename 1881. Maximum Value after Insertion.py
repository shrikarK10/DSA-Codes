# 1881. Maximum Value after Insertion
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# You are given a very large integer n, represented as a string,​​​​​​ and an integer digit x. The digits in n and the digit x are in the inclusive range [1, 9], and n may represent a negative number.

# You want to maximize n's numerical value by inserting x anywhere in the decimal representation of n​​​​​​. You cannot insert x to the left of the negative sign.

# For example, if n = 73 and x = 6, it would be best to insert it between 7 and 3, making n = 763.
# If n = -55 and x = 2, it would be best to insert it before the first 5, making n = -255.
# Return a string representing the maximum value of n​​​​​​ after the insertion.

class Solution:
    def maxValue(self, n: str, x: int) -> str:
        x =str(x)
        if(n[0]!="-"):
            for i in range(0,len(n)):
                if(n[i]<x) :
                    n = n[:i] + x + n[i:]
                    break
                elif i == len(n)-1 :
                    n+= x
        else:
            for i in range(1,len(n)):
                if(n[i]>x):
                    n = n[:i] + x + n[i:]
                    break
                elif i == len(n)-1 :
                    n+= str(x)
        return n
    

"""
Approach:
- First we check if the number is negative or positive by checking the first character of the string.
- If the number is positive, we iterate through each digit of the number from left to right and find the first digit that is less than x. 
- We insert x before that digit and break the loop. 
- If we reach the end of the string without finding such a digit, we append x to the end of the string.
- Same procedure is followed for negative numbers but we look for the first digit that is greater than x and insert x before that digit.
- Finally, we return the modified string representing the maximum value after insertion.
"""
