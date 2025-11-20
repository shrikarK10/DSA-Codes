# 2138. Divide a String Into Groups of Size k
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# A string s can be partitioned into groups of size k using the following procedure:

# The first group consists of the first k characters of the string, the second group consists of the next k characters of the string, and so on. Each element can be a part of exactly one group.
# For the last group, if the string does not have k characters remaining, a character fill is used to complete the group.
# Note that the partition is done so that after removing the fill character from the last group (if it exists) and concatenating all the groups in order, the resultant string should be s.

# Given the string s, the size of each group k and the character fill, return a string array denoting the composition of every group s has been divided into, using the above procedure.

class Solution:
    def divideString(self, s: str, k: int, fill: str) :
        str_list=[]
        end=k
        start=0
        up_str =""
        if(len(s) % k != 0):
            padding = k - len(s) % k
            up_str = s + fill * padding
        else:
            up_str =s
            
        while (True):
            str_list.append(up_str[start:end])
            start+=k
            end+=k
            if(len(up_str)< end): return str_list
        return str_list

"""
- initialize a list for returning the partitioned strings.
- initialize start and end pointers for slicing the string.
- also initialize a string up_str that will be used add padding if required and padding will be addedd only when we are not able to divide the string completely into k sized groups.
- Check if the string is completely divisible by k or not
- if no then we have to add the padding as the given fill character to make it divisible.
- then iterate over the string making groups of size k using string slicing 
- return the list 
"""
