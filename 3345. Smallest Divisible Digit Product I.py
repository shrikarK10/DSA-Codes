# 3345. Smallest Divisible Digit Product I
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given two integers n and t. Return the smallest number greater than or equal to n such that the product of its digits is divisible by t.


class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        strn= str(n)
        if (len(strn)==3):
            return n
        elif(len(strn)==2):
            while(True):
                prod=int(strn[0]) * int(strn[1])
                if(prod%t==0): return n
                else:
                    n+=1
                    strn=str(n)
        else:
            if (n < t): return t
            while(True):
                prod=int(strn[0])
                if(prod%t==0): return n
                else:
                    n+=1
                    strn=str(n)
                    if len(strn) > 1 : return n

"""
Approach:
- So the intuaition was converting the integer to string to easily traverse and aceess each element.
- but there was issue which was the length of the string.
- so if we carefully observe the constraints given in the problem statement we can see that the number can't be greater than 100
- so the max length the string can have is 3.
- so we do 3 checks based on that the length.
- if the length is 3 we directly return n as it will 100 not more than that and its product will always be 0 and divisible by t , so we return n itself.
- if the length is 2 we calculate the product of the two digits and check if its divisible by t, if yes we return n else we increment n and repeat the process.
- Now the problem with length 1 is that there can be some conditions where n can become 2 digit and the defeats the entire purpose of our 3 times cheking.
- so what we do is if n<t we directly return t as we eventually increment n till t and t is divisible by itself.
- and if n > t we do the same process as length 2 but with only one digit as the digits present is one.
- now first I thought that if the integer becomes 2 digit we have do the whole loop we did during the length 2 case 
- but after carefully observing that the when n increments from single digit to 2 digit , first 2 digit number will be 10 and whose product is zero so it is divisible by any number includidng t.
- so we return n which is 10 at that point.
"""