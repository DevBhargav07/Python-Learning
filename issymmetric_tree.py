# checking a tree is symmetric or not
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # using call stack
        def symmetric(p, q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            return symmetric(p.left, q.right) and symmetric(p.right, q.left)
        symmetric(root.left, root.right)

        # using iterative method
        stack = [(root.left, root.right)]
        while stack:
            node1, node2 = stack.pop()
            if not node1 and not node2:
                continue
            if not node1 or not node2 or node1.val != node2.val:
                return False
            stack.append((node1.left, node2.right))
            stack.append((node1.right, node2.left))
        return True