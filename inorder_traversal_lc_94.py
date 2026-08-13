# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        # nodes = []
        # def traversal(node):
        #     if not node:
        #         return
        #     traversal(node.left)
        #     nodes.append(node.val)
        #     traversal(node.right)
        # traversal(root)
        # return nodes
        # without using recursion
        stack = []
        result = []
        current = root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            
            current = stack.pop()

            result.append(current.val)
            current = current.right
        return result