# 3622. Check Divisibility by Digit Sum and Product
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given a positive integer n. Determine whether n is divisible by the sum of the following two values:

# The digit sum of n (the sum of its digits).

# The digit product of n (the product of its digits).

# Return true if n is divisible by this sum; otherwise, return false.

class Solution:
    def checkDivisibility(self, n: int) -> bool:
        n_str = str(n)
        sums,mult=0,1
        for i in n_str :
            sums+=int(i)
            mult*=int(i)
        return n % (sums + mult) == 0
    
"""
Approach:
- First, I converted the integer n to a string to easily iterate over each digit.
- I initialized two variables, sums and mult, to store the digit sum and digit product respectively.
- I then iterated over each character in the string representation of n.
- For each character, I converted it back to an integer and added it to sums and multiplied it to mult.
- Finally, I checked if n is divisible by the sum of sums and mult using the modulus operator and returned the result.
"""
