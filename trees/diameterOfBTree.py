# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # finding the height and using the height to find the max height will solve it.
        # self.res = 0
        res = 0
        def height(curr):
            if curr is None:
                return  0
            left = height(curr.left)
            right = height(curr.right)
            nonlocal res

            res = max(res, (left+right)) # diameter findig both arms

            return 1 + max(left, right)
        height(root)
        return res
