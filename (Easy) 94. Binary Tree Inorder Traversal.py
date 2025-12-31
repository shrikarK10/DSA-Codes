# 94. Binary Tree Inorder Traversal
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given the root of a binary tree, return the inorder traversal of its nodes' values.


from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.trv = []
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.dfs(root)
        return self.trv
    def dfs(self, root):
        if root:
            self.dfs(root.left)
            self.trv.append(root.val)
            self.dfs(root.right)
        

"""
Approach:
- Initialize an empty list trv to store the inorder traversal.
- Define a helper function dfs that takes a node as input.
- In the dfs function, check if the current node is not None.
- Recursively call dfs on the left child of the current node.
- Append the value of the current node to trv.
- Recursively call dfs on the right child of the current node.
- Start the traversal by calling dfs with the root node.
- Finally, return the trv list containing the inorder traversal of the tree.
"""
