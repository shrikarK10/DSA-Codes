# 145. Binary Tree Postorder Traversal
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given the root of a binary tree, return the postorder traversal of its nodes' values.

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.trav=[]
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.DFS_Post(root)
        return self.trav
    def DFS_Post(self,root):
        if not root :
            return 
        self.DFS_Post(root.left)
        self.DFS_Post(root.right)
        self.trav.append(root.val)

"""
Approach:
- I defined an initializer that creates an empty list 'trav' to store the postorder traversal.
- In the 'postorderTraversal' method, I called a helper function 'DFS_Post' with the root of the tree and returned the 'trav' list after the traversal is complete.
- The 'DFS_Post' function is a recursive function that performs the postorder traversal:
  - If the current node 'root' is None, it returns immediately (base case).
  - It recursively calls itself on the left child of the current node.
  - It recursively calls itself on the right child of the current node.
  - After visiting both children, it appends the value of the current node to the 'trav' list.
- This ensures that the left subtree is processed first, followed by the right subtree, and finally the root node, which is the essence of postorder traversal.
"""