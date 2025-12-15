# 1290. Convert Binary Number in a Linked List to Integer
# Solved
# Easy

# Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

# Return the decimal value of the number in the linked list.

# The most significant bit is at the head of the linked list.



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getDecimalValue(self, head) -> int:
        pointer = head
        bi_str = ""
        while(True):
            if(pointer == None):
                break
            else:
                bi_str +=str(pointer.val)
                pointer = pointer.next
        return int(bi_str , 2)
    


"""
Approach:
- Create a variable node that will also point to the head of the linked list.
- Create a string to store the binary number and later easier conversion to decimal.
- Traverse the linked list until the pointer reaches None i.e the end of the linked list.
- We append the value of each node to the binary string.
- And after that we convert the string to decimal using int function with base 2.
"""