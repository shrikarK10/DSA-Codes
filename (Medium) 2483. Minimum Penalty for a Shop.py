# 2483. Minimum Penalty for a Shop
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# You are given the customer visit log of a shop represented by a 0-indexed string customers consisting only of characters 'N' and 'Y':

# if the ith character is 'Y', it means that customers come at the ith hour
# whereas 'N' indicates that no customers come at the ith hour.
# If the shop closes at the jth hour (0 <= j <= n), the penalty is calculated as follows:

# For every hour when the shop is open and no customers come, the penalty increases by 1.
# For every hour when the shop is closed and customers come, the penalty increases by 1.
# Return the earliest hour at which the shop must be closed to incur a minimum penalty.

# Note that if a shop closes at the jth hour, it means the shop is closed at the hour j.


class Solution:
    def bestClosingTime(self, customers: str) -> int:
        penalty = customers.count('Y')
        best_hour = 0
        min_penalty = penalty 

        for i in range (0, len(customers)):
            if customers[i] == 'Y':
                penalty -=1
            else:
                penalty +=1
            if penalty < min_penalty :
                min_penalty  = penalty
                best_hour = i+1
        return best_hour
    

"""
Approach:
- First, calculate the initial penalty if the shop closes at hour 0, which is equal to the count of 'Y' in the customers string.
- Initialize variables best_hour to keep track of the hour with the minimum penalty and min_penalty to store the minimum penalty value.
- Iterate through each hour in the customers string.
- For each hour, update the penalty based on whether customers come ('Y') or not ('N'):
    - If customers come, decrease the penalty by 1 (since closing later avoids this penalty).
    - If no customers come, increase the penalty by 1 (since closing later incurs this penalty).
- After updating the penalty for each hour, check if the current penalty is less than the minimum penalty recorded. If it is, update min_penalty and set best_hour to the current hour + 1 (since closing at hour j means the shop is closed at hour j).
- Finally, return best_hour as the earliest hour to close the shop to incur the minimum penalty.
"""