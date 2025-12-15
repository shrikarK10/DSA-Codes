# 326. Power of Three
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given an integer n, return true if it is a power of three. Otherwise, return false.

# An integer n is a power of three, if there exists an integer x such that n == 3x.


#Initial Approach Large time complexity
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """

        pow = [3**i for i in range (31)]
        if(n not in pow):
            return False
        else:
            return True


#Optimized Approach
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if(n<=0): return False
        if(3**21 % n ==0):
            return True
        else:
            return False
        

"""
Approach:
- So the inital approach was to create a list of all the powers of 3 from 0 to 30 (Which is the constraint limit(2**30))
- Then we simply check if the input number is present in the created list of powers of 3
- But this approach has a large time complexity as we are creating a list of powers of 3
- So to optimize our approach we can use a property named "Prime Factorization"
- Accordiing to this property a power of a prime number can only be divisible by other powers of the same prime number
- for e.g 27 which is 3**3 can only be divisible by 3**0(1),3**1(3),3**2(9),3**3(27)
- So we directly find out largest possible power of 3 within the constraint limit which is 3**21(10460353203)
- Then we check if the input number n can divide 3**21 completely without leaving any remainder
- If it can then it is a power of 3 else it is not
"""