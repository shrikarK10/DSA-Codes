# 3021. Alice and Bob Playing Flower Game
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Alice and Bob are playing a turn-based game on a field, with two lanes of flowers between them. There are x flowers in the first lane between Alice and Bob, and y flowers in the second lane between them.



# The game proceeds as follows:

# Alice takes the first turn.
# In each turn, a player must choose either one of the lane and pick one flower from that side.
# At the end of the turn, if there are no flowers left at all in either lane, the current player captures their opponent and wins the game.
# Given two integers, n and m, the task is to compute the number of possible pairs (x, y) that satisfy the conditions:

# Alice must win the game according to the described rules.
# The number of flowers x in the first lane must be in the range [1,n].
# The number of flowers y in the second lane must be in the range [1,m].
# Return the number of possible pairs (x, y) that satisfy the conditions mentioned in the statement.


class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        # (n*(m/2) + m*(n/2)) /2 -> (nm/2 + nm/2 )/2 -> (2nm/2)/2 -> nm/2
        return (n*m)//2
    

"""
Approach:
- So I explored more test cases and found a pattern that Alice wins when the total number of flowers is odd.
- But it still doesn't give the count of pairs (x,y).
- So I tested more cases and their answers to find a relation between n,m and the answer.
- Later I found out that total numbers of pairs will be (n*m/2 + m*n/2) as for n numbers there will be m/2 odd numbers and vice versa.
- But this will count each pair twice so I divided the result by 2.
- So if we simplify the equation (n*(m/2) + m*(n/2)) /2 we get (n*m)/2
- So the final answer will be (n*m)/2
"""