# 2110. Number of Smooth Descent Periods of a Stock
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# You are given an integer array prices representing the daily price history of a stock, where prices[i] is the stock price on the ith day.

# A smooth descent period of a stock consists of one or more contiguous days such that the price on each day is lower than the price on the preceding day by exactly 1. The first day of the period is exempted from this rule.

# Return the number of smooth descent periods.



#optimal 
class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        count = 1
        result = 1
        
        for i in range(1, len(prices)):
            if prices[i] == prices[i -1] - 1:
                count += 1
            else:
                count = 1
            result+= count
        
        return result

# initial approach
# class Solution:
#     def getDescentPeriods(self, prices: List[int]) -> int:
#         n=1
#         total = 0
#         covered = 0
#         for i in range (1,len(prices)):
#             if prices[i] == prices[i-1]-1:
#                 n += 1
#                 if i == len(prices)-1 :
#                     total += (n * (n+1)) // 2
#                     covered+=n
#                     n=1                    
#             else :
#                 total += (n * (n+1)) // 2
#                 covered+=n
#                 n=1
#         return total + (len(prices)-covered)


"""
Initial Approach:
- Used multiple variables to keep track of total arrays and total covered elements.
- In for loop simply checked if the current element is equal to previous element - 1.
- If it is then we increase the count and if it is not then we reset the count to 1.
- Then we add the count to the total and covered variables.
- Finally we return the total + (len(prices)-covered)

Optimal Approach:
- After thinking it for a while I understood that we dont to do extra checks and we dont need to keep track of covered elements.
- Used a single variable to keep track of total arrays.
- In for loop simply checked if the current element is equal to previous element - 1.
- If it is then we increase the count and if it is not then we reset the count to 1.
- Then we add the count to the total.
- Finally we return the total