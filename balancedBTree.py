# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # check height of left and right add 1 and 
        # abs(left - right) <= 1 and left and right exists
        def dfs(curr):
            if not curr:
                return (True, 0)
            left, right = dfs(curr.left), dfs(curr.right)
            balanced = left and right and abs(left[1] - right[1]) <= 1
            return (balanced, 1+max(left[1], right[1]))
        return dfs(root)[0] # if you want booleaen [0] , if you want the height max [1]