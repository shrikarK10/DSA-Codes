# 700. Search in a Binary Search Tree
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# You are given the root of a binary search tree (BST) and an integer val.

# Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root, val: int):
        # curr = root
        while(root):
            if(val == root.val):
                return root
            elif(val > root.val):
                root = root.right
            elif(val < root.val):
                root = root.left
        return None


"""
Approach:
- We start at the root of the binary search tree (BST).
- We use a while loop to traverse the tree until we find the node with the value equal to `val` or reach a null node.
- Inside the loop, we compare the current node's value with `val`:
  - If they are equal, we return the current node.
  - If `val` is greater than the current node's value, we move to the right child of the current node.
  - If `val` is less than the current node's value, we move to the left child of the current node.
- If we reach a null node, it means the value is not present in the tree, so we return None.
"""