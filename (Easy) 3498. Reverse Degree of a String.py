# 3498. Reverse Degree of a String
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given a string s, calculate its reverse degree.

# The reverse degree is calculated as follows:

# For each character, multiply its position in the reversed alphabet ('a' = 26, 'b' = 25, ..., 'z' = 1) with its position in the string (1-indexed).
# Sum these products for all characters in the string.
# Return the reverse degree of s.


class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        re=0
        pointer = 1
        for i in s:
            re+= (123-ord(i))*pointer
            pointer += 1
        return re
    

"""
Approach:
- So the initial approach was map each character to its respective number by some in-built function like a=1 , b=2 ... z=26 an then somehow reverse it to get a=26, b=25 ... z=1
- When i found out how get numerical conversions of charcters , i came accross the ord() function which gives the ascii value of a character.
- So we basically substract the ascii value of current character from 123 which is ascii value of 'z' + 1 to get the reverse mapping.
- Then we multiply this value with the position of the character in the string (1-indexed) to get the degree of the current character and keep adding it to a result variable. 
- Finally we return the result variable which contains the reverse degree of the string.
"""