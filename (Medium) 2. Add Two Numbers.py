# 2. Add Two Numbers
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_val = []
        l2_val = []
        res = []

        x = l1
        while x:
            l1_val.append(x.val)
            x = x.next

        y = l2
        while y:
            l2_val.append(y.val)
            y = y.next

        len1, len2 = len(l1_val), len(l2_val)
        if len1 < len2:
            l1_val.extend([0] * (len2 - len1))
        elif len2 < len1:
            l2_val.extend([0] * (len1 - len2))

        carry = 0
        for i in range(len(l1_val)):
            total = l1_val[i] + l2_val[i] + carry
            res.append(total % 10)
            carry = total // 10

        if carry:
            res.append(carry)

        dummy = ListNode(0)
        cur = dummy
        for v in res:
            cur.next = ListNode(v)
            cur = cur.next

        return dummy.next
    
"""
Approach:
- So basic thought process was it will be difficult to add the numbers directly from the linked list, so I converted the linked lists to arrays for easier manipulation.
- I traversed both linked lists and stored their values in two separate arrays, l1_val and l2_val.
- After all the implemention the issue was i didnt thought about the length of both linked lists being different, so I checked their lengths and padded the shorter array with zeros to make them equal in length.
- Also i didnt keep in mind that there could be a carry after the last addition, so I added a check for any remaining carry after the loop and appended it to the result array if necessary.
- I then iterated through the arrays, adding corresponding digits along with any carry from the previous addition. I calculated the new digit to be added to the result and updated the carry for the next iteration.
- Finally, I constructed a new linked list from the result array and returned it."""