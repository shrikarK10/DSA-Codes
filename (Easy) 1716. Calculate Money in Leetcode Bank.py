# 1716. Calculate Money in Leetcode Bank
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.

# He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.

# Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.

from typing import List

class Solution:
    def totalMoney(self, n: int) -> int:
        week_no = n // 7
        res = n % 7

        sev = [x*7 for x in range(4,week_no+4)]

        residual = 0

        for i in range (1+week_no , res+week_no+1):
            residual+=i

        return sum(sev) + residual 


"""
Approach:
- At first this problem felt easy like a simple AP problem but then I realized that the increment happens weekly as well as daily.
- So which will be hard to calculate directly.
- So I tooked the problem to paper and pen and tried to find a pattern.
- So , I observed that the sum of current week and next week as net difference of 7.
- And the sume will also increase by 28 each week. (as 1+2+3+4+5+6+7 = 28 and net difference of each week is 7, so the progressing will be 28 + 7*0 , 28+28+7*1 , 28+28+28+7*2 and so on)
- Then wanted to find out a formula for the same.
- So I figured out that if we just take a list of 7's multiples form 4 (as 7*4 = 28) to week_no (week_no = n//7 (which will give the current week)) + 4 and sum it up we will get the total amount saved in complete weeks.
- With this we can find the totalmoney for complete weeks.
- Now we need to find the money saved in the residual days (n%7).
- So for that I just iterated from (1+week_no) to (residual days + week_no + 1) and summed it up.( as the starting day of the week will be (1+week_no) and will go on till residual days + week_no )
- Finally I returned the sum of both complete weeks and residual days.
"""