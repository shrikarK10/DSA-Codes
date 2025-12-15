# 2011. Final Value of Variable After Performing Operations
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# There is a programming language with only four operations and one variable X:

# ++X and X++ increments the value of the variable X by 1.
# --X and X-- decrements the value of the variable X by 1.
# Initially, the value of X is 0.

# Given an array of strings operations containing a list of operations, return the final value of X after performing all the operations.


class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        x=0
        for i in operations:
            if(i[0]=="-" or i[0]=="+"):
                if(i[0]=="-"):
                    x-=1
                if(i[0]=="+"):
                    x+=1
            else:
                if(i[1]=="-"):
                    x-=1
                if(i[1]=="+"):
                    x+=1
        return x

"""
Approach:
- So we find out by observing the input that if we check the first charcter we can find out whether to increment or decrement the variable X.
- And also if the first character is not + or - then the second character will be + or -.
- So we iterate through the list of operations and check the first character of each operation.
- If it is + we increment X by 1 else we decrement X by 1.
- If the first character is not + or - then the character will obviously X so we check the second character and do the same operation.
- Finally we return the value of X after performing all the operations.
"""