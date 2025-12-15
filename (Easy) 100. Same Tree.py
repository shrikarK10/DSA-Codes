# 100. Same Tree
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.values_p = []
        self.values_q = []

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.values_p = []
        self.values_q = []

        self.DFS(p, self.values_p)
        self.DFS(q, self.values_q)

        return self.values_p == self.values_q

    def DFS(self, node: Optional[TreeNode], acc: list):
        if node is None:
            acc.append('#')         
            return
        acc.append(node.val)        
        self.DFS(node.left, acc)
        self.DFS(node.right, acc)


"""
Approach:
- I used a Depth-First Search (DFS) approach to traverse both binary trees.
- I defined a helper function DFS that takes a node and an accumulator list as parameters.
- So logic was alright until I tested it on some cases where two trees had same values but different structures.
- So to overcome that I decided to append a "#" to point out None nodes in the traversal.
- And then I appended the value in "Inorder Traversal" manner.
- After traversing both trees, I compared the two lists of values.
- If the lists are identical, it means the trees are the same, so I returned True; otherwise, I returned False.
- But there was a issue with a edge case where the structure of both trees were different but I was getting the same values in the list.
- So the main culprit behind this was "Inorder Traversal"
- So to fix this I changed the traversal to "Preorder Traversal" manner which resolved the issue.
"""