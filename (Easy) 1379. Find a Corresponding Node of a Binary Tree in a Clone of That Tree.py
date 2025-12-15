# 1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given two binary trees original and cloned and given a reference to a node target in the original tree.

# The cloned tree is a copy of the original tree.

# Return a reference to the same node in the cloned tree.

# Note that you are not allowed to change any of the two trees or the target node and the answer must be a reference to a node in the cloned tree.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original, cloned, target):
        return self.DFS(target.val,cloned)
    
    def DFS(self, target , node):
        if node is None:
            return
        left =self.DFS(target , node.left)
        if left : return left

        if (node.val == target):
            return node

        right=self.DFS(target,node.right)
        if right : return right

"""
Approach:
- We define a method `getTargetCopy` that takes the original tree, the cloned tree, and the target node as inputs.
- We call a helper method `DFS` with the target node's value and the root of the cloned tree.
- In the `DFS` method, we perform a depth-first search on the cloned tree:  
- If the current node is None, we return.
    - We recursively search the left subtree. If we find the target node in the left subtree, we return it.
    - We check if the current node's value matches the target value. If it does, we return the current node.
    - We recursively search the right subtree. If we find the target node in the right subtree, we return it.
"""