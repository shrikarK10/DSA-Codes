# 104. Maximum Depth of Binary Tree
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def __init__(self):
        self.depth =[]

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.DFS(root ,0)
        return max(self.depth)

    def DFS(self,node,count):
        if (node == None):
            self.depth.append(count)
            # count=0
            return
        count+=1
        self.DFS(node.left,count)
        self.DFS(node.right,count)


"""
Approach:
- I used a Depth-First Search (DFS) approach to traverse the binary tree.
- I defined a helper function DFS that takes a node and the current depth count as parameters.
- If the current node is None, it means we've reached a leaf node, so I appended the current depth count to the depth list and returned.
- If the current node is not None, I incremented the depth count and recursively called the DFS function for the left and right child nodes.
- After the DFS traversal is complete, I returned the maximum value from the depth list, which represents the maximum depth of the binary tree.  
"""