from collections import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # using call stack
        def issame(p, q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return True
            return issame(p.left, q.left) and issame(p.right, q.right)
        return issame(p, q)

        # using iterative method
        stack = [(p, q)]
        while stack:
            node1, node2 = stack.pop()
            if not node1 and not node2:
                continue # can be a right node null for both but left is there or viceversa
            if not node1 or not node2 or node1.val != node2.val:
                return False
            stack.append((node1.left, node2.left))
            stack.append((node1.right, node2.right))
        return True

            