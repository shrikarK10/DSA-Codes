# 876. Middle of the Linked List
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def middleNode(self, head) :
        length =0
        pt = head
        while pt:
            length+=1
            pt=pt.next
        pt=head
        mid = length//2
        for _ in range (mid):
            pt=pt.next
            
        return pt


"""
Approach:
- First, we traverse the linked list to calculate its total length.
- Next, we determine the middle index using integer division of the length by 2.
- Finally, we traverse the linked list again up to the middle index and return the corresponding node.
- This approach ensures that if there are two middle nodes, we return the second one as required.
"""
