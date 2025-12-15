# 2511. Maximum Enemy Forts That Can Be Captured
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given a 0-indexed integer array forts of length n representing the positions of several forts. forts[i] can be -1, 0, or 1 where:

# -1 represents there is no fort at the ith position.
# 0 indicates there is an enemy fort at the ith position.
# 1 indicates the fort at the ith the position is under your command.
# Now you have decided to move your army from one of your forts at position i to an empty position j such that:

# 0 <= i, j <= n - 1
# The army travels over enemy forts only. Formally, for all k where min(i,j) < k < max(i,j), forts[k] == 0.
# While moving the army, all the enemy forts that come in the way are captured.

# Return the maximum number of enemy forts that can be captured. In case it is impossible to move your army, or you do not have any fort under your command, return 0.


from typing import List


class Solution:
    def captureForts(self, forts: List[int]) -> int:
        last = -1  
        ans = 0
        
        for i, v in enumerate(forts):
            if v != 0:   
                if last != -1 and forts[last] != v:
                    ans = max(ans, i - last - 1)
                last = i   
        return ans
    


"""
Approach:
- We initialize a variable `last` to keep track of the last position of our fort (1) or no fort (-1) and a variable `ans` to store the maximum number of enemy forts that can be captured.
- We iterate through the `forts` array using `enumerate` to get both the index and value.
- Whenever we encounter a position that is not an enemy fort (0), we check if `last` is not -1 (indicating we have seen a fort before) and if the current fort is different from the last fort (one is ours and the other is empty).
- If both conditions are met, we calculate the number of enemy forts between the last fort and the current position and update `ans` if this number is greater than the current `ans`.
- Finally, we update `last` to the current index and continue the iteration.
- After the loop, we return `ans`, which contains the maximum number of enemy forts that can be captured.
"""