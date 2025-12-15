# 2591. Distribute Money to Maximum Children
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given an integer money denoting the amount of money (in dollars) that you have and another integer children denoting the number of children that you must distribute the money to.

# You have to distribute the money according to the following rules:

# All money must be distributed.
# Everyone must receive at least 1 dollar.
# Nobody receives 4 dollars.
# Return the maximum number of children who may receive exactly 8 dollars if you distribute the money according to the aforementioned rules. If there is no way to distribute the money, return -1.


class Solution(object):
    def distMoney(self, money, children):
        """
        :type money: int
        :type children: int
        :rtype: int
        """
        if money < children:
            return -1
        if money == 8 * children:
            return children

        extra = money - children
        res = extra // 7

        if res >= children:
            return children - 1

        if res == children - 1 and extra % 7 == 3:
            return res - 1

        return res


"""
Approach:
- First, we check if the money is less than the number of children. If it is, we return -1 since it's impossible to give each child at least 1 dollar.
- Next, we check if the money is exactly equal to 8 times the number of children. If it is, we return the number of children since each child can receive exactly 8 dollars.
- We then calculate the extra money available after giving each child 1 dollar.
- We calculate the maximum number of children that can receive 8 dollars by dividing the extra money by 7 (since each child needs an additional 7 dollars to reach 8).
- We handle edge cases where giving 8 dollars to the maximum number of children would result in one child receiving 4 dollars.
- Finally, we return the maximum number of children that can receive exactly 8 dollars.
"""