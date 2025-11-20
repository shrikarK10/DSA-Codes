# 3668. Restore Finishing Order
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given an integer array order of length n and an integer array friends.

# order contains every integer from 1 to n exactly once, representing the IDs of the participants of a race in their finishing order.
# friends contains the IDs of your friends in the race sorted in strictly increasing order. Each ID in friends is guaranteed to appear in the order array.
# Return an array containing your friends' IDs in their finishing order.

 
class Solution(object):
    def recoverOrder(self, order, friends):
        """
        :type order: List[int]
        :type friends: List[int]
        :rtype: List[int]
        """

        ind =sorted([order.index(i) for i in friends])

        return [order[i] for i in ind]


"""
Approach:
- First we find the indices of the friends and then sorting them in the same line as they appear in the order array (as we have to return in the order in which they finished the race).
- Then we create and directly return a new list by iterating through the sorted indices and appending the corresponding values from the order array.

"""